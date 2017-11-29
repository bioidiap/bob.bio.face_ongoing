
#./bin/jman submit --name IJBA --repeat 1 --queue sgpu \
#./bin/bob_tf_train_generic \
# ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1.py


#./bin/jman submit --name IJBA-half --repeat 1 --queue sgpu \
#./bin/bob_tf_train_generic \
# ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1_adapted.py


###
# EVALUATE
###

#./bin/jman submit --name E.IJBA --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
#./bin/bob_tf_eval_generic \
#   ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1.py


#sleep 2000

#./bin/jman submit --name E.IJBA-half --repeat 1 --queue sgpu \
# ./bin/bob_tf_eval_generic \
#  ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1_adapted.py




### Triplet

#./bin/jman submit --name IJBA --repeat 1 --queue gpu \
#./bin/bob_tf_train_generic \
# ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1_adapted_triplet.py



#./bin/jman submit --name E.IJBA --queue q1d --io-big \
# --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" -- \
# ./bin/bob_tf_eval_generic \
# ./bob/bio/face-ongoing/configs/cnn/resnet_inception_v2/IJBA/split1_adapted_triplet.py

