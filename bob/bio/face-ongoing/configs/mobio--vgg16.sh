./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/vgg16/vgg16.py \
 ./bob/bio/face-ongoing/configs/databases/mobio/mobio-male.py \
 ./bob/bio/face-ongoing/configs/baselines/vgg16/crop_mobio.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/vgg16/ \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/MOBIO/vgg16/ \
 -vvv \
 -g 'demanding' \
 --groups dev eval
 


