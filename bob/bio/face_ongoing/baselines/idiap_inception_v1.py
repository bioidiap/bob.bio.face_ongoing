#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline


class idiap_casia_inception_v1_centerloss_gray(Baseline):
    """
    idiap_casia_inception_v1_centerloss_gray
    """

    def __init__(self):
        self.name = "idiap_casia_inception_v1_centerloss_gray"
        self.baseline_type = "Casia Webface"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_gray.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_mobio_gray.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_gray.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_lfw_gray.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_gray.py")


class idiap_casia_inception_v1_centerloss_rgb(Baseline):
    """
    idiap_casia_inception_v1_centerloss_rgb
    """

    def __init__(self):
        self.name = "idiap_casia_inception_v1_centerloss_rgb"
        self.baseline_type = "Casia Webface"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_rgb.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_mobio_rgb.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_lfw_rgb.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")

