#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


import bob.bio.face
from bob.bio.face.database import LFWBioDatabase


lfw_directory = "/idiap/resource/database/lfw/all_images"

database = LFWBioDatabase(
    original_directory=lfw_directory,
    annotation_type='funneled',

    protocol='fold1',
    training_depends_on_protocol=True,
    models_depend_on_protocol=True,

    all_files_options={'world_type': 'restricted'},
    extractor_training_options={'world_type': 'restricted'},  # 'subworld' : 'twofolds'
    projector_training_options={'world_type': 'restricted'},  # 'subworld' : 'twofolds'
    enroller_training_options={'world_type': 'restricted'}  # 'subworld' : 'twofolds'
)



