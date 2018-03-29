/remote/idiap.svm/user.active/tpereira/gitlab/bob/bob.bio.face-ongoing/bin/jman submit --name CELEB --repeat 1 --queue lgpu -- \
 /remote/idiap.svm/user.active/tpereira/gitlab/bob/bob.bio.face-ongoing/bin/bob_tf_train_generic \
  /remote/idiap.svm/user.active/tpereira/gitlab/bob/bob.bio.face-ongoing/bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss.py


# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \

#./bin/jman submit --name E.CE --queue q1d --io-big --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \

#./bin/bob_tf_eval_generic \
# ./bob/bio/face_ongoing/configs/cnn/resnet_inception_v2/MSCELEBA_center_loss.py
