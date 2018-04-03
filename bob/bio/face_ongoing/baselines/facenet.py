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
        self.name = "facenet_msceleba_inception_v1"
        self.baseline_type = "MSCeleb"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_sandberg/inception_v1.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_mobio_rgb.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_lfw_rgb.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")

