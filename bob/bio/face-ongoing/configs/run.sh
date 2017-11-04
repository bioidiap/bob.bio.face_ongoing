#verify.py ./configs/baselines/vgg16.py ./configs/databases/mobio.py \
# --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/isv+dct \
# --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/isv+dct \
# -vvv \
# --groups dev eval \
# -g 'grid' \


./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/vgg16.py ./bob/bio/face-ongoing/configs/databases/ijba/compare_split1.py \
 --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA \
 --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA \
 -vvv \
 -g 'grid'


#verify.py ./configs/baselines/vgg16.py ./configs/databases/ijba/search_split1.py \
# --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA \
# --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA \



# -g 'grid' \
