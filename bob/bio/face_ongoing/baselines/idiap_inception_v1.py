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
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_gray.py")
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.preprocessors = dict()        
        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/default_rgb_crop.py")
        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["casia_webface"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/casia_webface_crop.py")


class idiap_casia_inception_v1_centerloss_rgb(Baseline):
    """
    idiap_casia_inception_v1_centerloss_rgb
    """

    def __init__(self):
        self.name = "idiap_casia_inception_v1_centerloss_rgb"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_rgb.py")
        self.algorithm = 'distance-cosine' # Resource registed in bob.bio.base
        self.preprocessors = dict()
        self.preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/default_rgb_crop.py")
        self.preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
        self.preprocessors["casia_webface"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/casia_webface_crop.py")


baseline_idiap_casia_inception_v1_centerloss_gray = idiap_casia_inception_v1_centerloss_gray()
baseline_idiap_casia_inception_v1_centerloss_rgb = idiap_casia_inception_v1_centerloss_rgb()

