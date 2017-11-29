#!/bin/bash
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

./bin/jman submit --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0/bin"  --name TO-TF -q q1d --io-big \
./bin/bob_tf_db_to_tfrecords ./bob/bio/face-ongoing/configs/cnn/tfrecord_scripts/ijba/split1.py --allow-failures
