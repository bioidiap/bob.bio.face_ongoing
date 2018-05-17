#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import pkg_resources
from bob.bio.base.baseline import Baseline

# idiap_casia_inception_v2_centerloss_gray
preprocessors = dict()        
preprocessors["default"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/default_crop.py")
preprocessors["mobio"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/mobio_crop.py")

vgg16 = Baseline(name = "vgg16",\
                 extractor = 'vgg_features',\
                 algorithm = 'distance-cosine',\
                 preprocessors=preprocessors)
