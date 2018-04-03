#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

"""
This script runs some face recognition baselines under some face databases

Run `bob_faceongoing_baselines.py  --list` to list all the baselines and databases available

Examples:

This command line will run the facenet from David Sandberg using the IJB-A dataset:
  `bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases ijba`
  

This command line will run all the registed baselines using all databases registered databases::
  `bob_faceongoing_baselines.py --baselines all --databases all`



Usage:
  bob_faceongoing_baselines.py  --baselines=<arg> --databases=<arg>
  bob_faceongoing_baselines.py  --list
  bob_faceongoing_baselines.py -h | --help

Options:
  --baselines=<arg>                   Baseline name [default: all]
  --databases=<arg>                   Database name [default: all]
  --list                              List all the registered baselines
  -h --help                           Show this screen.
"""


import bob.bio.base
import bob.io.base
import os
from bob.extension.config import load
import pkg_resources
from docopt import docopt
from bob.bio.base.script.verify import main as verify
from bob.bio.face_ongoing.baselines import get_all_baselines_by_type, get_all_baselines, get_all_databases
from bob.extension import rc


all_baselines = get_all_baselines()
all_databases = get_all_databases()
all_baselines_by_type = get_all_baselines_by_type()


def trigger_verify(preprocessor, extractor, database, groups, sub_directory, protocol=None,
                   preprocessed_directory=None, extracted_directory=None):

    parameters = [
        preprocessor,
        extractor,
        '-d', database,
        '-a', "distance-cosine",
        '-g', 'demanding',
        '-G','submitted_experiments.sql3',
        '-vvv',
        '--temp-directory', str(rc['temp_dir']),
        '--result-directory', str(rc['results_dir']),
        '--sub-directory', sub_directory,
        '--environment','LD_LIBRARY_PATH=/idiap/user/tpereira/cuda/cuda-8.0/lib64:/idiap/user/tpereira/cuda/cudnn-8.0-linux-x64-v5.1/lib64:/idiap/user/tpereira/cuda/cuda-8.0',
    ] + ['--groups'] + groups
    if protocol is not None:
        parameters += ['--protocol', protocol]

    if preprocessed_directory is not None:
        parameters += ['--preprocessed-directory', preprocessed_directory]

    if extracted_directory is not None:
        parameters += ['--extracted-directory', extracted_directory]

    return parameters


def run_cnn_baseline(baseline, database):

    for p in all_databases[database].protocols:
        import tensorflow as tf
        tf.reset_default_graph()

        sub_directory = os.path.join(all_databases[database].name, all_baselines[baseline].name, p.replace(":",""))
        # Taking care of the directories
        if all_databases[database].preprocessed_directory is None:
            preprocessed_directory = all_databases[database].preprocessed_directory
        else:
            preprocessed_directory = os.path.join(rc['temp_dir'], all_databases[database].name, all_baselines[baseline].name,
                                                  all_databases[database].preprocessed_directory)
            
        # Taking care of the directories
        if all_databases[database].extracted_directory is None:
            extracted_directory = all_databases[database].extracted_directory
        else:
            extracted_directory = os.path.join(rc['temp_dir'],  all_databases[database].name, all_baselines[baseline].name,
                                               all_databases[database].extracted_directory)
        
        parameters = trigger_verify(all_baselines[baseline].preprocessors["{0}_crop".format(database)],
                                    all_baselines[baseline].extractor,
                                    all_databases[database].config,
                                    all_databases[database].groups,
                                    sub_directory,
                                    protocol=p,
                                    preprocessed_directory=preprocessed_directory,
                                    extracted_directory=extracted_directory)
        verify(parameters)


def main():

    args = docopt(__doc__, version='Run experiment')
    if args["--list"]:
        print("====================================")
        print("Follow all the registered baselines:")
        print("====================================")        
        for a in all_databases:
            print("  - %s"%(a))
        print("\n")

        print("====================================")
        print("Follow all the registered databases:")
        print("====================================")
        for a in all_baselines_by_type:
            print("Baselines of the type: %s"%(a))
            for b in all_baselines_by_type[a]:
                print("  >> %s"%(b))
            print("\n")

        exit()
    
    if args["--databases"] == "all":
        database = all_databases
    else:
        database = [args["--databases"]]

    if args["--baselines"] == "all":
        baselines = all_baselines
    else:
        baselines = [args["--baselines"]]

    # Triggering training for each baseline/database
    for b in baselines:
        for d in database:
            run_cnn_baseline(baseline=b, database=d)


if __name__ == "__main__":
    main()
