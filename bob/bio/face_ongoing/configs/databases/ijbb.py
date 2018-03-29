#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from bob.bio.face.database import IJBBBioDatabase
from bob.extension import rc
ijbb_directory = rc['ijbb']

database = IJBBBioDatabase(
  original_directory=ijbb_directory,
  protocol='1:1',
  original_extension=".png"
)

sub_directory = '1:1'


