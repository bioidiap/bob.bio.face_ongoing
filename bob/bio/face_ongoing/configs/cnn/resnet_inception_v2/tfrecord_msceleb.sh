#./bin/jman submit --name CELEB --repeat 1 --queue gpu \
#./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss.py


#./bin/jman submit --name CELEB-GRAY --repeat 1 --queue gpu \
#./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss_GRAY.py

./bin/jman submit --name CELEB-0.4 --repeat 3 --queue lgpu \
./bin/bob_tf_train_generic \
./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_centerloss_dbscan0.4.py



###
# EVALUATE
###

#./bin/jman submit --name E.CELEB-gray --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
#  ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss_GRAY.py


#./bin/jman submit --name E.CELEB --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss.py


#sleep 1800

#./bin/jman submit --name E.CELEB-0.4 --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_crossentropy_dbscan0.4.py



