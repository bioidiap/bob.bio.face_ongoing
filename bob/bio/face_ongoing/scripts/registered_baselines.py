#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import pkg_resources

all_baselines = ["idiap_msceleba_inception_v2",
                 "idiap_msceleba_inception_v2_gray",
                 "facenet_msceleba_inception_v1",
                 "idiap_casia_inception_v2_centerloss",
                 "idiap_casia_inception_v2_centerloss_gray",
                 "idiap_casia_inception_v2_crossentropy",
                 "idiap_casia_inception_v2_crossentropy_gray",                 
                 "vgg16",
                 "idiap_msceleba_inception_v2_facenet_prunning",
                 "idiap_msceleba_inception_v2_gray_facenet_prunning",
                 "idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04",
                 "idiap_casia_inception_v1_crossentropy_tantriggs"]

resources = dict()

# Mapping databases
resources["databases"] = dict()
resources["databases"]["mobio"] = "mobio-male"
resources["databases"]["ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijba.py")
resources["databases"]["ijbb"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijbb.py")
resources["databases"]["lfw"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/lfw.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2"] = dict()
resources["idiap_msceleba_inception_v2"]["name"] = "idiap_msceleba_inception_v2"
resources["idiap_msceleba_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")
resources["idiap_msceleba_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
resources["idiap_msceleba_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_ijba.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2_gray"] = dict()
resources["idiap_msceleba_inception_v2_gray"]["name"] = "idiap_msceleba_inception_v2_gray"
resources["idiap_msceleba_inception_v2_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/inception_v2.py")
resources["idiap_msceleba_inception_v2_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_mobio.py")
resources["idiap_msceleba_inception_v2_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_ijba.py")

# idiap_casia_inception_v2_gray
resources["idiap_casia_inception_v2_centerloss_gray"] = dict()
resources["idiap_casia_inception_v2_centerloss_gray"]["name"] = "idiap_casia_inception_v2_centerloss_gray"
resources["idiap_casia_inception_v2_centerloss_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss_gray/inception_v2.py")
resources["idiap_casia_inception_v2_centerloss_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss_gray/crop_mobio.py")
resources["idiap_casia_inception_v2_centerloss_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss_gray/crop_ijba.py")

# idiap_casia_inception_v2
resources["idiap_casia_inception_v2_centerloss"] = dict()
resources["idiap_casia_inception_v2_centerloss"]["name"] = "idiap_casia_inception_v2_centerloss"
resources["idiap_casia_inception_v2_centerloss"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/inception_v2.py")
resources["idiap_casia_inception_v2_centerloss"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_mobio.py")
resources["idiap_casia_inception_v2_centerloss"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_ijba.py")
resources["idiap_casia_inception_v2_centerloss"]["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_lfw.py")

# idiap_casia_inception_v2
resources["idiap_casia_inception_v2_crossentropy"] = dict()
resources["idiap_casia_inception_v2_crossentropy"]["name"] = "idiap_casia_inception_v2_crossentropy"
resources["idiap_casia_inception_v2_crossentropy"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_crossentropy/inception_v2.py")
resources["idiap_casia_inception_v2_crossentropy"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_mobio.py")
resources["idiap_casia_inception_v2_crossentropy"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_ijba.py")
resources["idiap_casia_inception_v2_crossentropy"]["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_lfw.py")


# idiap_casia_inception_v2 + GRAY
resources["idiap_casia_inception_v2_crossentropy_gray"] = dict()
resources["idiap_casia_inception_v2_crossentropy_gray"]["name"] = "idiap_casia_inception_v2_crossentropy_gray"
resources["idiap_casia_inception_v2_crossentropy_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_crossentropy_gray/inception_v2.py")
resources["idiap_casia_inception_v2_crossentropy_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss_gray/crop_mobio.py")
resources["idiap_casia_inception_v2_crossentropy_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss_gray/crop_ijba.py")


# idiap_casia_inception_v1 + TanTriggs
resources["idiap_casia_inception_v1_crossentropy_tantriggs"] = dict()
resources["idiap_casia_inception_v1_crossentropy_tantriggs"]["name"] = "idiap_casia_inception_v1_crossentropy_tantriggs"
resources["idiap_casia_inception_v1_crossentropy_tantriggs"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v1_crossentropy_tantriggs/inception_v1.py")
resources["idiap_casia_inception_v1_crossentropy_tantriggs"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v1_crossentropy_tantriggs/crop_mobio.py")
resources["idiap_casia_inception_v1_crossentropy_tantriggs"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v1_crossentropy_tantriggs/crop_ijba.py")



# vgg-16
resources["vgg16"] = dict()
resources["vgg16"]["name"] = "vgg16"
resources["vgg16"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/vgg16.py")
resources["vgg16"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_mobio.py")
resources["vgg16"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_ijba.py")

# vgg-16
resources["facenet_msceleba_inception_v1"] = dict()
resources["facenet_msceleba_inception_v1"]["name"] = "facenet_msceleba_inception_v1"
resources["facenet_msceleba_inception_v1"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/inception_v1.py")
resources["facenet_msceleba_inception_v1"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_mobio.py")
resources["facenet_msceleba_inception_v1"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_ijba.py")
resources["facenet_msceleba_inception_v1"]["lfw_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_centerloss/crop_lfw.py")

# idiap_msceleba_inception_v2_facenet_prunning
resources["idiap_msceleba_inception_v2_facenet_prunning"] = dict()
resources["idiap_msceleba_inception_v2_facenet_prunning"]["name"] = "idiap_msceleba_inception_v2_facenet_prunning"
resources["idiap_msceleba_inception_v2_facenet_prunning"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2_facenet_prunning.py")
resources["idiap_msceleba_inception_v2_facenet_prunning"]["mobio_crop"] = resources["idiap_msceleba_inception_v2"]["mobio_crop"]
resources["idiap_msceleba_inception_v2_facenet_prunning"]["ijba_crop"] = resources["idiap_msceleba_inception_v2"]["ijba_crop"]

# idiap_msceleba_inception_v2_facenet_prunning gray
resources["idiap_msceleba_inception_v2_gray_facenet_prunning"] = dict()
resources["idiap_msceleba_inception_v2_gray_facenet_prunning"]["name"] = "idiap_msceleba_inception_v2_gray_facenet_prunning"
resources["idiap_msceleba_inception_v2_gray_facenet_prunning"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/inception_v2_facenet_prunning.py")
resources["idiap_msceleba_inception_v2_gray_facenet_prunning"]["mobio_crop"] = resources["idiap_msceleba_inception_v2_gray"]["mobio_crop"]
resources["idiap_msceleba_inception_v2_gray_facenet_prunning"]["ijba_crop"] = resources["idiap_msceleba_inception_v2_gray"]["ijba_crop"]


# idiap_msceleba_inception_v2_facenet_prunning gray
resources["idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"] = dict()
resources["idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"]["name"] = "idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"
resources["idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/inception_v2_facenet_prunning_04.py")
resources["idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"]["mobio_crop"] = resources["idiap_msceleba_inception_v2_gray"]["mobio_crop"]
resources["idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04"]["ijba_crop"] = resources["idiap_msceleba_inception_v2_gray"]["ijba_crop"]






