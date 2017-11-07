#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


import bob.bio.face
from bob.bio.face.database import IJBABioDatabase

ijba_directory = "/idiap/resource/database/IJB-A/"

database = IJBABioDatabase(
  original_directory=ijba_directory,
  protocol='search_split4',
  original_extension=".png"
)

sub_directory = 'search/split4'

