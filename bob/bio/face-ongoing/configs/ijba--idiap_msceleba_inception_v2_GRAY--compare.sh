#!/bin/bash
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

for split in 'compare_split1.py' 'compare_split2.py' 'compare_split3.py' 'compare_split4.py' \
           'compare_split5.py' 'compare_split6.py' 'compare_split7.py' 'compare_split8.py' \
           'compare_split9.py' 'compare_split10.py'
do
 
  command_string="./bin/verify.py ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2_GRAY/inception_v2.py ./bob/bio/face-ongoing/configs/baselines/idiap_msceleba_inception_v2_GRAY/crop_ijba.py ./bob/bio/face-ongoing/configs/databases/ijba/$split "
  command_string+=" --temp-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/idiap_inception_v2_msceleb_GRAY/ "
  command_string+=" --result-directory  /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/idiap_inception_v2_msceleb_GRAY/ " 
  command_string+=" -vvv "
  command_string+=" -g demanding "
  command_string+=" --preprocessed-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/idiap_inception_v2_msceleb_GRAY/compare/split1/preprocessed "
  command_string+=" --extracted-directory /idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/idiap_inception_v2_msceleb_GRAY/compare/split1/extracted "

 $command_string
 
done

