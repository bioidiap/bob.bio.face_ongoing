#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import bob.ip.tensorflow_extractor
import bob.bio.face
from bob.learn.tensorflow.network import inception_resnet_v2
import tensorflow as tf
from bob.bio.base.extractor import Extractor
import numpy


model_filename = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2/centerloss_alpha-0.95_factor-0.02_lr-0.01/"


class TensorflowEmbedding(Extractor):

    """
    """

    def __init__(
            self,
            tf_extractor
    ):
        Extractor.__init__(self, skip_extractor_training=True)
        self.tf_extractor = tf_extractor

    def __call__(self, image):
        """__call__(image) -> feature

        Extract features

        **Parameters:**

        image : 3D :py:class:`numpy.ndarray` (floats)
          The image to extract the features from.

        **Returns:**

        feature : 2D :py:class:`numpy.ndarray` (floats)
          The extracted features
        """

        if image.ndim>2:
            image = bob.io.image.to_matplotlib(image)
            image = numpy.reshape(image, tuple([1] + list(image.shape)) )
            image = image.astype("float32")            
        else:
            image = numpy.reshape(image, tuple([1] + list(image.shape) + [1]) )
        
        features = self.tf_extractor(image)

        return features[0]

    # re-define the train function to get it non-documented
    def train(*args, **kwargs): raise NotImplementedError("This function is not implemented and should not be called.")

    def load(*args, **kwargs): pass


#########
# Extraction
#########
inputs = tf.placeholder(tf.float32, shape=(1, 160, 160, 3))

# Taking the embedding
prelogits = inception_resnet_v2(tf.stack([tf.image.per_image_standardization(i) for i in tf.unstack(inputs)]), mode=tf.estimator.ModeKeys.PREDICT)[0]
embedding = tf.nn.l2_normalize(prelogits, dim=1, name="embedding")

extractor = TensorflowEmbedding(bob.ip.tensorflow_extractor.Extractor(model_filename, inputs, embedding))


#########
# Alg
#########
algorithm = 'distance-cosine'

