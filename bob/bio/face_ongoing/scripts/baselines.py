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


base_paths = pkg_resources.resource_filename("bob.bio.face_ongoing",
                                             "configs/base_paths.py")


resources = dict()

ijba_comparison_protocols = ["compare_split{0}".format(i) for i in range(10)]
ijba_search_protocols = ["search_split{0}".format(i) for i in range(10)]

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2"] = dict()
resources["idiap_msceleba_inception_v2"]["name"] = "idiap_casia_inception_v2"
resources["idiap_msceleba_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")
resources["idiap_msceleba_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
resources["idiap_msceleba_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_ijba.py")



def run_cnn_baseline(preprocessor, extractor, database, groups, sub_directory, protocol=None):
    
    configs  = load([base_paths])
    parameters = [
        base_paths,
        preprocessor,
        extractor,
        '-d', database,
        '-a', "distance-cosine",
        '-vvv',
        '-g', 'grid',
        '--temp-directory', configs.temp_dir,
        '--result-directory', configs.results_dir,
        '--sub-directory', sub_directory
    ] + ['--groups'] + groups
    
    if protocol is not None:
        parameters += ['--protocol', protocol]
    
    return parameters


def run_idiap_msceleba_inception_v2():

    # Triggering mobio
    parameters = run_cnn_baseline(resources["idiap_msceleba_inception_v2"]["mobio_crop"],
                                  resources["idiap_msceleba_inception_v2"]["extractor"],
                                  "mobio-male",
                                  ["dev", "eval"],
                                  "MOBIO/"+resources["idiap_msceleba_inception_v2"]["name"],
                                  protocol=None)
    verify(parameters)
    
    for p in ijba_comparison_protocols:
        parameters = run_cnn_baseline(resources["idiap_msceleba_inception_v2"]["ijba_crop"],
                                      resources["idiap_msceleba_inception_v2"]["extractor"],
                                      "mobio-male",
                                      ["dev"],
                                      "MOBIO/"+resources["idiap_msceleba_inception_v2"]["name"],
                                      protocol=None)
    



def main():

    args = docopt(__doc__, version='Run experiment')
    
    if args["--baselines"] == "all":
        run_idiap_msceleba_inception_v2()



if __name__ == "__main__":
    main()
