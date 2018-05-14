#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline


class facenet(Baseline):
    """
    Facenet David Sanderberg
    """

    def __init__(self):
        self.name = "facenet"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_sandberg/inception_v1.py")
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.preprocessors = dict()
        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/default_rgb_crop.py")
        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["casia_webface"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/casia_webface_crop.py")

baseline = facenet()
