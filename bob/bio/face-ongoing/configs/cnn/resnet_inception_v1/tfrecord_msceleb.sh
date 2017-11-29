./bin/jman submit --name CELEB-v1 --repeat 1 --queue gpu \
./bin/bob_tf_train_generic \
./bob/bio/face-ongoing/configs/cnn/resnet_inception_v1/MSCELEBA_center_loss.py


###
# EVALUATE
###


#./bin/jman submit --name E.CELEB-v1 --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#./bob/bio/face-ongoing/configs/cnn/resnet_inception_v1/MSCELEBA_center_loss.py



