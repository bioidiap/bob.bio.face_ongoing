#!/usr/bin/env python
# coding: utf-8

from functools import partial
from glob import glob

import pkg_resources
import tensorflow as tf
from bob.learn.tensorflow.losses import CenterLoss
from bob.learn.tensorflow.models.inception_resnet_v2 import InceptionResNetV2
from bob.learn.tensorflow.utils import predict_using_tensors
from tensorflow.keras import layers


def main():

    train_tf_record_paths = sorted(
        glob(
            "/idiap/project/hface/databases/tfrecords/msceleba/"
            "tfrecord_182x_hand_prunned_44/*.tfrecord"
        )
    )
    validation_tf_record_paths = sorted(
        glob("/idiap/project/hface/databases/tfrecords/lfw/182x/RGB/*.tfrecord")
    )
    checkpoint = "/idiap/temp/amohammadi/models/inception_v2_batchnorm_rgb_msceleba"

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

    DEFAULT_FEATURE = {
        "data": tf.io.FixedLenFeature([], tf.string),
        "label": tf.io.FixedLenFeature([], tf.int64),
        "key": tf.io.FixedLenFeature([], tf.string),
    }
    AUTOTUNE = tf.data.experimental.AUTOTUNE

    def decode_tfrecords(x):
        features = tf.io.parse_single_example(x, DEFAULT_FEATURE)
        image = tf.io.decode_raw(features["data"], DATA_TYPE)
        image = tf.reshape(image, DATA_SHAPE)
        features["data"] = image
        return features

    preprocessor = tf.keras.Sequential(
        [
            # rotate before cropping
            layers.experimental.preprocessing.RandomRotation(
                5 / 360
            ),  # math.pi * 5 /180
            layers.experimental.preprocessing.RandomCrop(
                height=OUTPUT_SHAPE[0], width=OUTPUT_SHAPE[1]
            ),
            layers.experimental.preprocessing.RandomFlip("horizontal"),
            # FIXED_STANDARDIZATION from https://github.com/davidsandberg/facenet
            layers.experimental.preprocessing.Rescaling(
                scale=1 / 128, offset=-127.5 / 128
            ),  # [-0.99609375, 0.99609375]
        ]
    )

    def preprocess(features, augment=False):
        image = features["data"]
        label = features["label"]
        image = preprocessor(image, training=augment)
        return image, label

    def prepare_dataset(tf_record_paths, batch_size, shuffle=False, augment=False):
        ds = tf.data.TFRecordDataset(
            tf_record_paths, num_parallel_reads=TFRECORD_PARALLEL_READ
        )
        ds = ds.map(decode_tfrecords)
        if shuffle:
            ds = ds.shuffle(SHUFFLE_BUFFER)
        ds = ds.batch(batch_size).map(
            partial(preprocess, augment=augment), num_parallel_calls=AUTOTUNE
        )

        # Use buffered prefecting on all datasets
        return ds.prefetch(buffer_size=AUTOTUNE)

    train_ds = prepare_dataset(
        train_tf_record_paths, batch_size=BATCH_SIZE, shuffle=True, augment=True
    ).repeat(EPOCHS)

    val_ds = prepare_dataset(
        validation_tf_record_paths,
        batch_size=VALIDATION_BATCH_SIZE,
        shuffle=False,
        augment=False,
    )

    model = InceptionResNetV2(
        include_top=True,
        classes=N_CLASSES,
        bottleneck=True,
        input_shape=OUTPUT_SHAPE + (3,),
    )
    prelogits = model.layers[-2].output
    logits = model.layers[-1].output
    model = tf.keras.Model(
        inputs=model.input, outputs=[logits, prelogits], name=model.name
    )

    cross_entropy = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    center_loss = CenterLoss(
        n_classes=N_CLASSES, n_features=prelogits.shape[-1], alpha=0.9
    )

    def weighted_center_loss(y_true, y_pred):
        loss = center_loss(y_true, y_pred)
        return 0.01 * loss

    def accuracy_from_embeddings(labels, prelogits):
        labels = tf.reshape(labels, (-1,))
        embeddings = tf.nn.l2_normalize(prelogits, 1)
        predictions = predict_using_tensors(embeddings, labels)
        return tf.math.equal(labels, predictions)

    model.compile(
        optimizer=tf.keras.optimizers.RMSprop(
            learning_rate=LEARNING_RATE, rho=0.9, momentum=0.9, epsilon=1.0
        ),
        loss={"logits": cross_entropy, "Bottleneck/BatchNorm": weighted_center_loss},
        metrics={"Bottleneck/BatchNorm": accuracy_from_embeddings},
        run_eagerly=True,
    )

    val_metric_name = "val_Bottleneck/BatchNorm_accuracy_from_embeddings"

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            checkpoint,
            monitor=val_metric_name,
            save_best_only=False,
            mode="max",
            save_freq="epoch",
        ),
        tf.keras.callbacks.ModelCheckpoint(
            f"{checkpoint}/best",
            monitor=val_metric_name,
            save_best_only=True,
            mode="max",
            save_freq="epoch",
        ),
        tf.keras.callbacks.TensorBoard(
            log_dir=f"{checkpoint}/logs",
            update_freq=2,
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor=val_metric_name, factor=0.2, patience=5, min_lr=0.001
        ),
        tf.keras.callbacks.TerminateOnNaN(),
    ]
    model.fit(
        train_ds, validation_data=val_ds, epochs=int(1e10), steps_per_epoch=2000, callbacks=callbacks, verbose=2
    )


if __name__ == "__main__":
    main()
