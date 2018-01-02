#./bin/jman submit --name CA --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy_RMSPROP.py

#./bin/jman submit --name E.CASIA --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy_RMSPROP.py 




####

#./bin/jman submit --name CA-CE --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_center_loss.py



#./bin/jman submit --name E.CA-CE --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_center_loss.py



###

#./bin/jman submit --name CA-CROS --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy.py

#./bin/jman submit --name E.CA-CROS --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy.py


##

#./bin/jman submit --name CA-GRAY --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy_GRAY.py


#./bin/jman submit --name E.CASIA-GRAY --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_crossentropy_GRAY.py




##

#./bin/jman submit --name CA-CE-G --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_center_loss_GRAY.py
 

#./bin/jman submit --name E.CA-CE-G --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/CASIA_center_loss_GRAY.py


### TRiplet

#./bin/jman submit --name CA.GRAY.TRIPLET --repeat 1  --queue sgpu -- \
# ./bin/bob_tf_train_generic \
# ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/CASIA_TRIPLET_loss_GRAY.py


#./bin/jman submit --name E.CA.TRIPLET --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/CASIA_TRIPLET_loss_GRAY.py

 
 

