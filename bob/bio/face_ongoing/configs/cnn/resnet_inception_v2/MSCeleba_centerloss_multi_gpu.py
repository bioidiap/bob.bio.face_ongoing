#!/usr/bin/env python
# coding: utf-8

import json
import os
from functools import partial

import pkg_resources
import tensorflow as tf
from bob.learn.tensorflow.losses import CenterLoss
from bob.learn.tensorflow.models.inception_resnet_v2 import InceptionResNetV2
from bob.learn.tensorflow.utils import predict_using_tensors
from tensorflow.keras import layers

TRAIN_TF_RECORD_PATHS = (
    "/idiap/project/hface/databases/tfrecords/msceleba/"
    "tfrecord_182x_hand_prunned_44/*.tfrecord"
)
VALIDATION_TF_RECORD_PATHS = (
    "/idiap/project/hface/databases/tfrecords/lfw/182x/RGB/*.tfrecord"
)
# there are 2812 samples in the validation set
VALIDATION_SAMPLES = 2812

CHECKPOINT = (
    "/idiap/temp/amohammadi/models/inception_v2_batchnorm_rgb_msceleba_mutli_gpu"
)

AUTOTUNE = tf.data.experimental.AUTOTUNE
N_CLASSES = 87662
DATA_SHAPE = (182, 182, 3)  # size of faces
DATA_TYPE = tf.uint8
OUTPUT_SHAPE = (160, 160)
TFRECORD_PARALLEL_READ = 4

SHUFFLE_BUFFER = int(2e4)

LEARNING_RATE = 0.1
BATCH_SIZE = 90
EPOCHS = 5

VALIDATION_BATCH_SIZE = 38

# number of training steps to do before validating a model. This also defines an epoch
# for keras which is not really true.
STEPS_PER_EPOCH = 2000


FEATURES = {
    "data": tf.io.FixedLenFeature([], tf.string),
    "label": tf.io.FixedLenFeature([], tf.int64),
    "key": tf.io.FixedLenFeature([], tf.string),
}
LOSS_WEIGHTS = {"cross_entropy": 1.0, "center_loss": 0.01}


def decode_tfrecords(x):
    features = tf.io.parse_single_example(x, FEATURES)
    image = tf.io.decode_raw(features["data"], DATA_TYPE)
    image = tf.reshape(image, DATA_SHAPE)
    features["data"] = image
    return features


def get_preprocessor():
    preprocessor = tf.keras.Sequential(
        [
            # rotate before cropping
            # 5 random degree rotation
            layers.experimental.preprocessing.RandomRotation(5 / 360),
            layers.experimental.preprocessing.RandomCrop(
                height=OUTPUT_SHAPE[0], width=OUTPUT_SHAPE[1]
            ),
            layers.experimental.preprocessing.RandomFlip("horizontal"),
            # FIXED_STANDARDIZATION from https://github.com/davidsandberg/facenet
            # [-0.99609375, 0.99609375]
            layers.experimental.preprocessing.Rescaling(
                scale=1 / 128, offset=-127.5 / 128
            ),
        ]
    )
    return preprocessor


def preprocess(preprocessor, features, augment=False):
    image = features["data"]
    label = features["label"]
    image = preprocessor(image, training=augment)
    return image, label


def prepare_dataset(tf_record_paths, batch_size, shuffle=False, augment=False):
    ds = tf.data.Dataset.list_files(tf_record_paths, shuffle=shuffle)
    ds = tf.data.TFRecordDataset(ds, num_parallel_reads=TFRECORD_PARALLEL_READ)
    ds = ds.map(decode_tfrecords)
    if shuffle:
        ds = ds.shuffle(SHUFFLE_BUFFER).repeat(EPOCHS)
    preprocessor = get_preprocessor()
    ds = ds.batch(batch_size).map(
        partial(preprocess, preprocessor, augment=augment), num_parallel_calls=AUTOTUNE,
    )

    # Use buffered prefecting on all datasets
    return ds.prefetch(buffer_size=AUTOTUNE)


def accuracy_from_embeddings(labels, prelogits):
    labels = tf.reshape(labels, (-1,))
    embeddings = tf.nn.l2_normalize(prelogits, 1)
    predictions = predict_using_tensors(embeddings, labels)
    return tf.math.equal(labels, predictions)


class CustomModel(tf.keras.Model):
    def compile(
        self,
        cross_entropy,
        center_loss,
        loss_weights,
        train_loss,
        train_cross_entropy,
        train_center_loss,
        test_acc,
        global_batch_size,
        **kwargs,
    ):
        super().compile(**kwargs)
        self.cross_entropy = cross_entropy
        self.center_loss = center_loss
        self.loss_weights = loss_weights
        self.train_loss = train_loss
        self.train_cross_entropy = train_cross_entropy
        self.train_center_loss = train_center_loss
        self.test_acc = test_acc
        self.global_batch_size = global_batch_size

    def train_step(self, data):
        images, labels = data
        with tf.GradientTape() as tape:
            logits, prelogits = self(images, training=True)
            loss_cross = self.cross_entropy(labels, logits)
            loss_center = self.center_loss(labels, prelogits)
            loss = (
                loss_cross * self.loss_weights[self.cross_entropy.name]
                + loss_center * self.loss_weights[self.center_loss.name]
            )
            loss = tf.nn.compute_average_loss(loss, global_batch_size=self.global_batch_size)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        self.train_loss(loss)
        self.train_cross_entropy(loss_cross)
        self.train_center_loss(loss_center)
        return {
            m.name: m.result()
            for m in [self.train_loss, self.train_cross_entropy, self.train_center_loss]
        }

    def test_step(self, data):
        images, labels = data
        logits, prelogits = self(images, training=False)
        self.test_acc(accuracy_from_embeddings(labels, prelogits))
        return {m.name: m.result() for m in [self.test_acc]}


def create_model():

    model = InceptionResNetV2(
        include_top=True,
        classes=N_CLASSES,
        bottleneck=True,
        input_shape=OUTPUT_SHAPE + (3,),
    )
    prelogits = model.layers[-2].output
    logits = model.layers[-1].output
    model = CustomModel(
        inputs=model.input, outputs=[logits, prelogits], name=model.name
    )
    return model


def build_and_compile_model(global_batch_size):
    model = create_model()

    cross_entropy = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True, name="cross_entropy", reduction=tf.keras.losses.Reduction.NONE
    )
    center_loss = CenterLoss(
        n_classes=N_CLASSES, n_features=128, alpha=0.9, name="center_loss", reduction=tf.keras.losses.Reduction.NONE
    )

    optimizer = tf.keras.optimizers.RMSprop(
        learning_rate=LEARNING_RATE, rho=0.9, momentum=0.9, epsilon=1.0
    )

    train_loss = tf.keras.metrics.Mean(name="loss")
    train_cross_entropy = tf.keras.metrics.Mean(name="cross_entropy")
    train_center_loss = tf.keras.metrics.Mean(name="center_loss")

    test_acc = tf.keras.metrics.Mean(name="accuracy")

    model.compile(
        optimizer=optimizer,
        cross_entropy=cross_entropy,
        center_loss=center_loss,
        loss_weights=LOSS_WEIGHTS,
        train_loss=train_loss,
        train_cross_entropy=train_cross_entropy,
        train_center_loss=train_center_loss,
        test_acc=test_acc,
        global_batch_size=global_batch_size,
    )
    return model


def train_and_evaluate():

    per_worker_batch_size = BATCH_SIZE
    num_workers = 4

    strategy = tf.distribute.MirroredStrategy()

    global_batch_size = per_worker_batch_size * num_workers
    train_ds = prepare_dataset(
        TRAIN_TF_RECORD_PATHS, batch_size=global_batch_size, shuffle=True, augment=True
    )

    val_global_batch_size = VALIDATION_BATCH_SIZE * num_workers

    val_ds = prepare_dataset(
        VALIDATION_TF_RECORD_PATHS,
        batch_size=val_global_batch_size,
        shuffle=False,
        augment=False,
    )

    with strategy.scope():
        model = build_and_compile_model(global_batch_size=global_batch_size)

    val_metric_name = "val_accuracy"

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(f"{CHECKPOINT}/latest",),
        tf.keras.callbacks.ModelCheckpoint(
            f"{CHECKPOINT}/best",
            monitor=val_metric_name,
            save_best_only=True,
            mode="max",
        ),
        tf.keras.callbacks.TensorBoard(
            log_dir=f"{CHECKPOINT}/logs", update_freq=15, profile_batch="10,50"
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor=val_metric_name, factor=0.2, patience=5, min_lr=0.001
        ),
        tf.keras.callbacks.TerminateOnNaN(),
        tf.keras.callbacks.experimental.BackupAndRestore(
            backup_dir=f"{CHECKPOINT}/backup"
        ),
    ]

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=int(1e10),
        steps_per_epoch=STEPS_PER_EPOCH,
        validation_steps=VALIDATION_SAMPLES // VALIDATION_BATCH_SIZE,
        callbacks=callbacks,
        verbose=2 if os.environ.get("SGE_TASK_ID", "") else 1,
    )
