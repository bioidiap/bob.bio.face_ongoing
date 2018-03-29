#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import bob.bio.face
from bob.bio.face.database import IJBABioDatabase
from bob.extension import rc

ijba_directory = rc['ijba']

database = IJBABioDatabase(
  original_directory=ijba_directory,
  protocol='compare_split1',
  original_extension=".png"
)

sub_directory = 'compare/split1'


