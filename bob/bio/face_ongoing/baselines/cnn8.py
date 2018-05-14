#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline

class cnn8(Baseline):
    """        
    CNN 8
    """

    def __init__(self):
        self.name = "cnn8"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/cnn8/extractor.py")
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.preprocessors = dict()
        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/cnn8/default_crop.py")
        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/cnn8/eyes_crop.py")

baseline = cnn8()
