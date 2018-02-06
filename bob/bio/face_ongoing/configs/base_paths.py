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

lfw_data_info = {"data_path": "/idiap/resource/database/lfw/all_images",
                 "extension": ".jpg"}


# Temp directories
temp_dir    = "/idiap/temp/tpereira/bob.bio.face-ongoing/"
results_dir = "/idiap/temp/tpereira/bob.bio.face-ongoing/"


# Background model paths

# dbscan pruning 0.5 - light CNN
inception_resnet_v2_msceleb      = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2/centerloss_alpha-0.95_factor-0.02_lr-0.01/"
inception_resnet_v2_msceleb_gray = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2_gray/centerloss_alpha-0.95_factor-0.02_lr-0.01/"

# dbscan pruning 0.5 - facenet
#inception_resnet_v2_msceleb_facenet_prunning      = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning_facenet/official_checkpoints/resnet_inception_v2/centerloss_alpha-0.95_factor-0.02_lr-0.01/"
inception_resnet_v2_msceleb_facenet_prunning = "/idiap/temp/tpereira/msceleb/official_checkpoints/inception_resnet_v2/dbscan_0.4/centerloss_alpha-0.90_factor-0.02/"

inception_resnet_v2_msceleb_gray_facenet_prunning = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning_facenet/official_checkpoints/resnet_inception_v2_gray/centerloss_alpha-0.95_factor-0.02_lr-0.01/"

inception_resnet_v2_msceleb_facenet_prunning = "/idiap/temp/tpereira/msceleb/official_checkpoints/inception_resnet_v2/dbscan_0.4/centerloss_alpha-0.90_factor-0.02/"


idiap_msceleba_inception_v2_crossentropy_gray_facenet_prunning_04 = "/idiap/temp/tpereira/msceleb/official_checkpoints/inception_resnet_v2_gray/dbscan_0.4/crossentropy/"




# dbscan pruning 0.
inception_resnet_v1_msceleb = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning_facenet_0.4/official_checkpoints/resnet_inception_v1/centerloss_alpha-0.95_factor-0.02_lr-0.01/"

# Casia models
#inception_resnet_v2_casia_webface_centerloss      = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2/centerloss_alpha-0.90_factor-0.02"
inception_resnet_v2_casia_webface_centerloss = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2/centerloss_alpha-0.90_factor-0.02_batchnorm/"

inception_resnet_v2_casia_webface_centerloss_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2_gray/centerloss_alpha-0.90_factor-0.02/"

inception_resnet_v2_casia_webface_centerloss_gray_staging = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2_gray/centerloss_alpha-0.90_factor-0.02_staging/"


#inception_resnet_v2_casia_webface_centerloss_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/inception_resnet_v2/centerloss_alpha-0.90_factor-0.02_noBatchNorm_GRAY/"


inception_resnet_v2_casia_webface_crossentropy      = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2/crossentropy/"
#inception_resnet_v2_casia_webface_crossentropy_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/inception_resnet_v2/official_checkpoints/crossentropy_gray/"
inception_resnet_v2_casia_webface_crossentropy_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v2_gray/crossentropy"

inception_resnet_v1_casia_webface_centerloss = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v1/centerloss_alpha-0.90_factor-0.02/"

inception_resnet_v1_casia_webface_centerloss_gray = "/idiap/temp/tpereira/casia_webface/new_tf_format/official_checkpoints/inception_resnet_v1_gray/centerloss_alpha-0.90_factor-0.02/"

inception_resnet_v1_casia_webface_crossentropy_tantriggs = "/idiap/temp/tpereira/casia_webface/new_tf_format/inception_resnet_v1/official_checkpoints/cross_entropy_tantriggs/"



#facenet = "/idiap/project/hface/models/cnn/facenet/20170512-110547"
#facenet = "/idiap/temp/tpereira/facenet/inception_v1/20180104-175138/"
#facenet = "/idiap/temp/tpereira/facenet/inception_v1/20180105-083835/"
#facenet_v2 = "/idiap/temp/tpereira/facenet/inception_v2/20180109-090826/"
facenet_v2 = "/idiap/temp/tpereira/facenet/inception_v2_77plus/20180115-171413/"

