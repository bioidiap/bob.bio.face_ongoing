#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline


class drgan(Baseline):
    """
    Original DRGan
    """

    def __init__(self):
        self.name = "drgan"
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/extractor.py")
        self.preprocessors = dict()
        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/default_crop.py")
        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/eyes_crop.py")
        self.preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/eyes_crop.py")

baseline = drgan()

