#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline


class facenet_msceleba_inception_v1(Baseline):
    """
    facenet_msceleba_inception_v1
    
    Original facenet
    """

    def __init__(self):
        self.name = "vgg16"
        self.baseline_type = "VGG"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/vgg16.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_mobio.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_ijba.py")

