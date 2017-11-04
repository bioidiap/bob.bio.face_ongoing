#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tue 20 Oct 2016 16:48:32 CEST
import bob.bio.face
import bob.bio.gmm

preprocessor = "tan-triggs"

extractor = "dct-blocks"

algorithm = bob.bio.gmm.algorithm.ISV(
    # ISV parameters
    subspace_dimension_of_u = 160,
    # GMM parameters
    number_of_gaussians = 512
)

