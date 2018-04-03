#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import pkg_resources
from .baseline import Baseline


class idiap_casia_inception_v2_centerloss_gray(Baseline):
    """
    idiap_casia_inception_v2_centerloss_gray
    """

    def __init__(self):
        self.name = "idiap_casia_inception_v2_centerloss_gray"
        self.baseline_type = "Casia Webface"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v2/centerloss_gray.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_mobio_gray.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_gray.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_lfw_gray.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_gray.py")
        


class idiap_casia_inception_v2_centerloss_rgb(Baseline):
    """
    idiap_casia_inception_v2_centerloss_rgb
    """

    def __init__(self):
        self.name = "idiap_casia_inception_v2_centerloss_rgb"
        self.baseline_type = "Casia Webface"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/casiawebface/inception_resnet_v2/centerloss_rgb.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_mobio_rgb.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_lfw_rgb.py")
        self.preprocessors["ijbc_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/inception_resnet_preprocessors/crop_ijba_rgb.py")


""""
class idiap_casia_inception_v2_crossentropy(Baseline):
    
    Idiap Casia inception v2 crossentropy loss
    

    def __init__(self):
        self.name = "idiap_casia_inception_v2_crossentropy"
        self.baseline_type = "Casia Webface"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_crossentropy/inception_v2.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_mobio.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_ijba.py")
        self.preprocessors["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_lfw.py")

        
       
class idiap_msceleba_inception_v2(Baseline):
    
    idiap_msceleba_inception_v2
    

    def __init__(self):
        self.name = "idiap_msceleba_inception_v2"
        self.baseline_type = "MSCeleb"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_ijba.py")

        
class idiap_msceleba_inception_v2_gray(Baseline):
    
    idiap_msceleba_inception_v2_gray
    

    def __init__(self):
        self.name = "idiap_msceleba_inception_v2_gray"
        self.baseline_type = "MSCeleb"
        self.extractor = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/inception_v2.py")
        self.preprocessors = dict()
        self.preprocessors["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_mobio.py")
        self.preprocessors["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_mobio.py")
        
"""
