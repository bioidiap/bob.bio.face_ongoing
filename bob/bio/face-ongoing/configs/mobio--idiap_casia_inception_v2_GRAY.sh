./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/idiap_casia_inception_v2_GRAY/inception_v2.py \
 ./bob/bio/face-ongoing/configs/databases/mobio/mobio-male.py \
 ./bob/bio/face-ongoing/configs/baselines/idiap_casia_inception_v2_GRAY/crop_mobio.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_casia_inception_v2_GRAY/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/idiap_casia_inception_v2_GRAY/ \
 -vvv \
 -g 'demanding' \
 --groups dev eval
 


