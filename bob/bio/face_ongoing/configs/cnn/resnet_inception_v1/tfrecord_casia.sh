#./bin/jman submit --name CA-v1 --repeat 1 --queue gpu \
#./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_centerloss.py

#./bin/jman submit --name CA-v1 --repeat 1 --queue gpu \
#./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_cross_entropy.py


./bin/jman submit --name CASIA-v1-TT --repeat 1 --queue gpu \
./bin/bob_tf_train_generic ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_cross_entropy_TAN-TRIGGS.py

#
###
# EVALUATE
###

#sleep 500

#./bin/jman submit --name E.CASIA-v1-TT --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_cross_entropy_TAN-TRIGGS.py



#./bin/jman submit --name E.CA-v1 --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v1/CASIA_cross_entropy.py



