#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from bob.bio.face.database import IJBCBioDatabase
from bob.extension import rc
ijbc_directory = rc['ijbc']

database = IJBCBioDatabase(
  original_directory=ijbc_directory,
  protocol='1:1',
  original_extension=".png"
)

sub_directory = '1:1'


