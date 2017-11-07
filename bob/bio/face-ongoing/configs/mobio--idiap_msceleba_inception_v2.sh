./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2/inception_v2.py \
 ./bob/bio/face-ongoing/configs/databases/mobio/mobio-male.py \
 ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_msceleba_inception_v2/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_msceleba_inception_v2/ \
 -vvv \
 -g 'demanding' \
 --groups dev eval
 


