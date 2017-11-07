./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/facenet_msceleba_inception_v1/inception_v1.py \
 ./bob/bio/face-ongoing/configs/databases/mobio/mobio-male.py \
 ./bob/bio/face-ongoing/configs/baselines/facenet_msceleba_inception_v1/crop_mobio.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/facenet_inception_v1_msceleb/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/facenet_inception_v1_msceleb/ \
 -vvv \
 -g 'demanding' \
 --groups dev eval
 


