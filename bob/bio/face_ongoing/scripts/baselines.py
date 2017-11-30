#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

"""
Run some face recognition baselines

Usage:
  bob_faceongoing_baselines.py  [--baselines=<arg> --databases=<arg>]
  bob_faceongoing_baselines.py -h | --help

Options:
  --baselines=<arg>                   Baseline name [default: all]
  --databases=<arg>                   Database name [default: all]
  -h --help                             Show this screen.
"""


import bob.bio.base
import bob.io.base

from bob.extension.config import load
import pkg_resources
from docopt import docopt
from bob.bio.face.database import MobioBioDatabase
from bob.bio.base.script.verify import main as verify

def run_cnn_baseline(config_list):
    
    configs  = load(config_list) 
        

    parameters = [
        pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/base_paths.py"),
        pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py"),
        pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py"),
        '-d', 'mobio-male',
        '-a', "distance-cosine",
        '-vvv',
        '-g', 'grid',
        '--groups', 'dev eval'
        '--temp-directory', configs.temp_dir,
        '--result-directory', configs.results_dir,
        '--sub-directory', "MOBIO/idiap_casia_inception_v2"        
    ]

    

    #parameters = [
    #    pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/base_paths.py"),
    #    '-d', 'mobio-male',
    #    '-p', pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py"),
    #    '-e', pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py"),
    #    '-a', "distance-cosine",
    #    '--temp-directory', configs["temp_dir"],
    #    '--result-directory', configs["results_dir"],
    #    '--sub-directory', "MOBIO/idiap_casia_inception_v2"        
    #]

    #import ipdb; ipdb.set_trace();

    verify(parameters)
    
    x=0





def main():

    args = docopt(__doc__, version='Run experiment')
    
    base_paths = pkg_resources.resource_filename("bob.bio.face_ongoing",
                                                 "configs/base_paths.py")
                                                 
    #croppers = pkg_resources.resource_filename("bob.bio.face_ongoing",
    #                                           "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
                                               
    #extractor = pkg_resources.resource_filename("bob.bio.face_ongoing",
    #                                           "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")    
    
    run_cnn_baseline([base_paths])
    
    
    


if __name__ == "__main__":
    main()
