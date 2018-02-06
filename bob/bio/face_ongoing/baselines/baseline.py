#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


class Baseline(object):
    """
    Base class for an baselines
    Each baseline for this package should extend this class
    
    The baseline should have:
      - Name
      - Preprocessor: A path to the correspondent preprocessor config 
      - Extractor: A path to the correspondent extractor config
      - reuse_extractor:
      - preprocessed_data
    
    """

    def __init__(self):
        self.name = ""
        self.baseline_type = ""
        self.preprocessors = dict()
        self.extractor = ""

