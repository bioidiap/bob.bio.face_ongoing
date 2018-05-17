#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import pkg_resources
from bob.bio.base.baseline import Baseline


# idiap_casia_inception_v1_centerloss_gray
preprocessors = dict()        
preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/default_rgb_crop.py")
preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
preprocessors["casia_webface"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/casia_webface_crop.py")

idiap_casia_inception_v1_centerloss_gray = Baseline(name = "idiap_casia_inception_v1_centerloss_gray",\
                                                    extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_gray.py"),\
                                                    algorithm = 'distance-cosine',\
                                                    preprocessors=preprocessors
)


# idiap_casia_inception_v1_centerloss_rgb
preprocessors = dict()
preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/default_rgb_crop.py")
preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
preprocessors["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/eyes_rgb_crop.py")
preprocessors["casia_webface"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/casia_webface_crop.py")

idiap_casia_inception_v1_centerloss_rgb = Baseline(name = "idiap_casia_inception_v1_centerloss_rgb",\
                                                   extractor=pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v1/centerloss_rgb.py"),\
                                                   algorithm = 'distance-cosine',\
                                                   preprocessors=preprocessors)

