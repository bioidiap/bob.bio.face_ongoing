#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

# Paths
ijba_data_info = {"data_path": "/idiap/resource/database/IJB-A/",
                  "extension": ".png"}
                  
ijbb_data_info = {"data_path": "/idiap/resource/database/IJB-B/",
                  "extension": ".png"}

mobio_data_info = {"data_path": "/idiap/resource/database/mobio/IMAGES_PNG",
                   "annotations_path": "/idiap/resource/database/mobio/IMAGE_ANNOTATIONS",
                   "extension": ".png"}


# Temp directories
temp_dir    = "/idiap/temp/tpereira/bob.bio.face-ongoing/"
results_dir = "/idiap/temp/tpereira/bob.bio.face-ongoing/"


# Background model paths

# dbscan pruning 0.5
inception_resnet_v2_msceleb      = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2/centerloss_alpha-0.95_factor-0.02_lr-0.01/"
inception_resnet_v2_msceleb_gray = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2_gray/centerloss_alpha-0.95_factor-0.02_lr-0.01/"


# dbscan pruning 0.
inception_resnet_v1_msceleb = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning_facenet_0.4/official_checkpoints/resnet_inception_v1/centerloss_alpha-0.95_factor-0.02_lr-0.01/"

# Casia modles
inception_resnet_v2_casia_webface      = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2/centerloss_alpha-0.95_factor-0.02_lr-0.1/"
inception_resnet_v2_casia_webface_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2_gray/centerloss_alpha-0.95_factor-0.02_lr-0.1/"

facenet = "/idiap/temp/tpereira/msceleb/official_checkpoints/facenet/20170512-110547/"
