./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2/inception_v2.py \
 ./bob/bio/face-ongoing/configs/databases/mobio/mobio-male.py \
 ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_msceleba_inception_v2/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_msceleba_inception_v2/ \
 --environment="LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0" \
 -vvv \
 -g 'demanding' \
 --groups dev eval
 


