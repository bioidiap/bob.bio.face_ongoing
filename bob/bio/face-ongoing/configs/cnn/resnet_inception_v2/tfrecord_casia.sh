#./bin/jman submit --name CA --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./src/bob.bio.htface/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss.py


#./bin/jman submit --name E.CASIA --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  /idiap/user/tpereira/gitlab/workspace_HTFace/src/bob.bio.htface/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss.py



##

#./bin/jman submit --name CA.GRAY --repeat 1  --queue gpu -- \
# ./bin/bob_tf_train_generic \
# ./src/bob.bio.htface/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss_GRAY.py
 

#./bin/jman submit --name E.CASIA.GRAY --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#  /idiap/user/tpereira/gitlab/workspace_HTFace/src/bob.bio.htface/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss_GRAY.py

 
 

