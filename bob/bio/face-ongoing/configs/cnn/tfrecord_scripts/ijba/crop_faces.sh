#!/bin/bash
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


./bin/verify.py ./bob/bio/face-ongoing/configs/cnn/tfrecord_scripts/ijba/split1.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/tfrecords/raw_data/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/tfrecords/raw_data/ \
 -vvv \
 -o preprocessing \
 --groups dev
 
 #-g 'demanding' \
 




