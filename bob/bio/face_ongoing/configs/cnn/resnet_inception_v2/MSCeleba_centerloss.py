#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
from glob import glob
from tensorflow.keras import layers
from bob.learn.tensorflow.models.inception_resnet_v2 import InceptionResNetV2
from functools import partial


def main():

    train_tf_record_paths = sorted(
        glob(
            "/idiap/project/hface/databases/tfrecords/msceleba/"
            "tfrecord_182x_hand_prunned_44/*.tfrecord"
        )
    )
    N_CLASSES = 87662
    DATA_SHAPE = (182, 182, 3)  # size of faces
    OUTPUT_SHAPE = (160, 160)
    DATA_TYPE = tf.uint8
    TFRECORD_PARALLEL_READ = 4

    SHUFFLE_BUFFER = int(2e4)

    LEARNING_RATE = 0.1
    BATCH_SIZE = 90
    EPOCHS = 5

    VALIDATION_BATCH_SIZE = 38
    EMBEDDING_VALIDATION = True

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

    preprocessing = tf.keras.Sequential(
        [
            layers.experimental.preprocessing.Rescaling(scale=1.0 / 255),  # 0 - 1
            layers.experimental.preprocessing.RandomCrop(
                height=OUTPUT_SHAPE[0], width=OUTPUT_SHAPE[1]
            ),
            layers.experimental.preprocessing.RandomFlip("horizontal"),
            layers.experimental.preprocessing.RandomRotation(
                5 / 360
            ),  # math.pi * 5 /180
            layers.experimental.preprocessing.Rescaling(
                scale=1.0, offset=-0.5
            ),  # -0.5 - 0.5
        ]
    )

    def preprocess(features, training=True):
        image = features["data"]
        label = features["label"]
        image = preprocessing(image, training=training)
        return image, label

    def prepare_dataset(tf_record_paths, shuffle=False, augment=False):
        ds = tf.data.TFRecordDataset(
            tf_record_paths, num_parallel_reads=TFRECORD_PARALLEL_READ
        )
        ds = ds.map(decode_tfrecords)
        if shuffle:
            ds = ds.shuffle(SHUFFLE_BUFFER)
        ds = ds.batch(BATCH_SIZE).map(partial(preprocess, training=augment))

        # Use buffered prefecting on all datasets
        return ds.prefetch(buffer_size=AUTOTUNE)

    train_ds = prepare_dataset(train_tf_record_paths, shuffle=True, augment=True)
    train_ds

    model = InceptionResNetV2(
        include_top=True, classes=N_CLASSES, input_shape=OUTPUT_SHAPE + (3,)
    )

    model.compile(
        optimizer=tf.keras.optimizers.RMSprop(
            learning_rate=LEARNING_RATE, rho=0.9, momentum=0.9, epsilon=1.0
        ),
        loss=tf.keras.losses.sparse_categorical_crossentropy,
    )

    model.fit(train_ds, epochs=EPOCHS)


if __name__ == "__main__":
    main()
