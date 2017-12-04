#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import pkg_resources

all_baselines = ["idiap_msceleba_inception_v2",
                 "idiap_msceleba_inception_v2_gray",
                 "facenet_msceleba_inception_v1",
                 "idiap_casia_inception_v2",
                 "idiap_casia_inception_v2_gray",
                 "vgg16",
                 "idiap_msceleba_inception_v2_facenet_prunning",
                 "idiap_msceleba_inception_v2_gray_facenet_prunning"]

resources = dict()

# Mapping databases
resources["databases"] = dict()
resources["databases"]["mobio"] = "mobio-male"
resources["databases"]["ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijba.py")
resources["databases"]["ijbb"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijbb.py")

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
resources["idiap_casia_inception_v2_gray"] = dict()
resources["idiap_casia_inception_v2_gray"]["name"] = "idiap_casia_inception_v2_gray"
resources["idiap_casia_inception_v2_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/inception_v2.py")
resources["idiap_casia_inception_v2_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/crop_mobio.py")
resources["idiap_casia_inception_v2_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/crop_ijba.py")

# idiap_casia_inception_v2
resources["idiap_casia_inception_v2"] = dict()
resources["idiap_casia_inception_v2"]["name"] = "idiap_casia_inception_v2"
resources["idiap_casia_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/inception_v2.py")
resources["idiap_casia_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/crop_mobio.py")
resources["idiap_casia_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/crop_ijba.py")

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

