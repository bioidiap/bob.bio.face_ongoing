#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import bob.ip.tensorflow_extractor
import bob.bio.face
import tensorflow as tf
from bob.bio.base.extractor import Extractor
import numpy
import re
from bob.io.image import to_matplotlib
import os
import logging
logger = logging.getLogger(__name__)
model_filename = facenet


def prewhiten(img):
    mean = numpy.mean(img)
    std = numpy.std(img)
    std_adj = numpy.maximum(std, 1.0 / numpy.sqrt(img.size))
    y = numpy.multiply(numpy.subtract(img, mean), 1 / std_adj)
    return y


def get_model_filenames(model_dir):
    # code from https://github.com/davidsandberg/facenet
    files = os.listdir(model_dir)
    meta_files = [s for s in files if s.endswith('.meta')]
    if len(meta_files) == 0:
        raise ValueError(
            'No meta file found in the model directory (%s)' % model_dir)
    elif len(meta_files) > 1:
        raise ValueError(
            'There should not be more than one meta file in the model '
            'directory (%s)' % model_dir)
    meta_file = meta_files[0]
    meta_files = [s for s in files if '.ckpt' in s]
    max_step = -1
    for f in files:
        step_str = re.match(r'(^model-[\w\- ]+.ckpt-(\d+))', f)
        if step_str is not None and len(step_str.groups()) >= 2:
            step = int(step_str.groups()[1])
            if step > max_step:
                max_step = step
                ckpt_file = step_str.groups()[0]
    return meta_file, ckpt_file


class FaceNet(Extractor):
    """bob.bio.base wrapper for the free FaceNet variant:
    https://github.com/davidsandberg/facenet"""

    def __init__(self,
                 model_path,
                 image_size=160,
                 **kwargs):
        super(FaceNet, self).__init__(
            requires_training=False,
            model_path=model_path,
            **kwargs)
        self.model_path = model_path
        self.image_size = image_size
        self.session = None
        self.embeddings = None

    def _check_feature(self, img):
        img = numpy.ascontiguousarray(img)
        if img.ndim == 2:
            img = gray_to_rgb(img)
        assert img.shape[-1] == self.image_size
        assert img.shape[-2] == self.image_size
        img = to_matplotlib(img)
        img = prewhiten(img)
        return img[None, ...]

    def load_model(self):
        # code from https://github.com/davidsandberg/facenet
        model_exp = os.path.expanduser(self.model_path)
        if (os.path.isfile(model_exp)):
            logger.info('Model filename: %s' % model_exp)
            with tf.gfile.FastGFile(model_exp, 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                tf.import_graph_def(graph_def, name='')
        else:
            logger.info('Model directory: %s' % model_exp)
            meta_file, ckpt_file = get_model_filenames(model_exp)

            logger.info('Metagraph file: %s' % meta_file)
            logger.info('Checkpoint file: %s' % ckpt_file)

            saver = tf.train.import_meta_graph(
                os.path.join(model_exp, meta_file))
            saver.restore(tf.get_default_session(),
                          os.path.join(model_exp, ckpt_file))
        # Get input and output tensors
        self.images_placeholder = self.graph.get_tensor_by_name("input:0")
        self.embeddings = self.graph.get_tensor_by_name("embeddings:0")
        self.phase_train_placeholder = self.graph.get_tensor_by_name(
            "phase_train:0")

    def __call__(self, img):
        images = self._check_feature(img)
        if self.session is None:
            self.session = tf.InteractiveSession()
            self.graph = tf.get_default_graph()
        if self.embeddings is None:
            self.load_model()
        feed_dict = {self.images_placeholder: images,
                     self.phase_train_placeholder: False}
        features = self.session.run(
            self.embeddings, feed_dict=feed_dict)
        return features.flatten()


#########
# Extraction
#########
extractor = FaceNet(model_filename)


