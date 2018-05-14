#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline

class vgg16(Baseline):
    """        
    VGG 16
    """

    def __init__(self):
        self.name = "vgg16"
        self.extractor = 'vgg_features' # Resource registed in bob.bio.caffe_face
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.preprocessors = dict()

        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/default_crop.py")

        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/mobio_crop.py")

baseline = vgg16()
