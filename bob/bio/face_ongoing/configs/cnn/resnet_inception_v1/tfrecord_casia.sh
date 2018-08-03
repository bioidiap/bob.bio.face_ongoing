
#./bin/jman submit --name C-v1-BA --repeat 1 --queue gpu \
# ./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_centerloss_batchnorm.py

#./bin/jman submit --name C-G-v1 --repeat 1 --queue gpu -- \
# ./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_centerloss_noBatchNorm_GRAY.py

#./bin/jman submit --name Cross-G-v1 --repeat 1 --queue gpu -- \
# ./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_crossentropy_noBatchNorm_GRAY.py



###
# EVALUATE
###


#./bin/jman submit --name E.C-v1-BA --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_centerloss_batchnorm.py

#./bin/jman submit --name E.CG-v1 --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_centerloss_noBatchNorm_GRAY.py

