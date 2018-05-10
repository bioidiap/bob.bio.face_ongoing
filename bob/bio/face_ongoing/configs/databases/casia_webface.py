#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import bob.bio.face
from bob.bio.face.database import CasiaWebFaceBioDatabase
from bob.extension import rc

original_directory = "/idiap/resource/database/CASIA-WebFace/CASIA-WebFace/"

database = CasiaWebFaceBioDatabase(
    original_directory=original_directory,
    original_extension=".jpg",
    protocol='number-all-split1',
    training_depends_on_protocol=True,
    models_depend_on_protocol=True,
)

