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
        self.baseline_type = "DRGan"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/extractor.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/crop_mobio.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/crop_ijba.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/crop_lfw.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/drgan/crop_ijba.py")

