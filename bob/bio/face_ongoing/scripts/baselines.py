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
import os
from bob.extension.config import load
import pkg_resources
from docopt import docopt
from bob.bio.face.database import MobioBioDatabase
from bob.bio.base.script.verify import main as verify


base_paths = pkg_resources.resource_filename("bob.bio.face_ongoing",
                                             "configs/base_paths.py")


resources = dict()

ijba_comparison_protocols = ["compare_split{0}".format(i) for i in range(1, 11)]
ijba_search_protocols = ["search_split{0}".format(i) for i in range(1, 11)]

all_baselines = ["idiap_msceleba_inception_v2",
                 "idiap_msceleba_inception_v2_gray",
                 "facenet_msceleba_inception_v1",
                 "idiap_casia_inception_v2",
                 "idiap_casia_inception_v2_gray",
                 "vgg16"]

# Mapping databases
resources["databases"] = dict()
resources["databases"]["mobio"] = "mobio-male"
resources["databases"]["ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijba.py")
resources["databases"]["ijbb"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijbb.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2"] = dict()
resources["idiap_msceleba_inception_v2"]["name"] = "idiap_msceleba_inception_v2"
resources["idiap_msceleba_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")
resources["idiap_msceleba_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
resources["idiap_msceleba_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_ijba.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2_gray"] = dict()
resources["idiap_msceleba_inception_v2_gray"]["name"] = "idiap_msceleba_inception_v2_gray"
resources["idiap_msceleba_inception_v2_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/inception_v2.py")
resources["idiap_msceleba_inception_v2_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_mobio.py")
resources["idiap_msceleba_inception_v2_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2_gray/crop_ijba.py")

# idiap_casia_inception_v2_gray
resources["idiap_casia_inception_v2_gray"] = dict()
resources["idiap_casia_inception_v2_gray"]["name"] = "idiap_casia_inception_v2_gray"
resources["idiap_casia_inception_v2_gray"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/inception_v2.py")
resources["idiap_casia_inception_v2_gray"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/crop_mobio.py")
resources["idiap_casia_inception_v2_gray"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2_gray/crop_ijba.py")

# idiap_casia_inception_v2
resources["idiap_casia_inception_v2"] = dict()
resources["idiap_casia_inception_v2"]["name"] = "idiap_casia_inception_v2"
resources["idiap_casia_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/inception_v2.py")
resources["idiap_casia_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/crop_mobio.py")
resources["idiap_casia_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_casia_inception_v2/crop_ijba.py")

# vgg-16
resources["vgg16"] = dict()
resources["vgg16"]["name"] = "vgg16"
resources["vgg16"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/vgg16.py")
resources["vgg16"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_mobio.py")
resources["vgg16"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_ijba.py")

# vgg-16
resources["facenet_msceleba_inception_v1"] = dict()
resources["facenet_msceleba_inception_v1"]["name"] = "facenet_msceleba_inception_v1"
resources["facenet_msceleba_inception_v1"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/inception_v1.py")
resources["facenet_msceleba_inception_v1"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_mobio.py")
resources["facenet_msceleba_inception_v1"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_ijba.py")


def trigger_verify(preprocessor, extractor, database, groups, sub_directory, protocol=None,
                   preprocessed_directory=None, extracted_directory=None):
    
    configs  = load([base_paths])
    parameters = [
        base_paths,
        preprocessor,
        extractor,
        '-d', database,
        '-a', "distance-cosine",
        '-vvv',
        '-g', 'demanding',
        '--temp-directory', configs.temp_dir,
        '--result-directory', configs.results_dir,
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


def run_cnn_baseline(baseline, database=resources["databases"].keys()):
    configs  = load([base_paths])

    # Triggering mobio
    if "mobio" in database:
        import tensorflow as tf
        tf.reset_default_graph()

        parameters = trigger_verify(resources[baseline]["mobio_crop"],
                                    resources[baseline]["extractor"],
                                    "mobio-male",
                                    ["dev", "eval"],
                                    "MOBIO/"+resources[baseline]["name"],
                                    protocol=None)
        verify(parameters)

    if "ijba" in database:
        first_subdir = os.path.join("IJBA", resources[baseline]["name"], ijba_comparison_protocols[0])
        for p in ijba_comparison_protocols:
            import tensorflow as tf
            tf.reset_default_graph()

            sub_directory = os.path.join("IJBA", resources[baseline]["name"], p)
            parameters = trigger_verify(resources[baseline]["ijba_crop"],
                                        resources[baseline]["extractor"],
                                        resources["databases"]["ijba"],
                                        ["dev"],
                                        sub_directory,
                                        protocol=p,
                                        preprocessed_directory=os.path.join(configs.temp_dir, first_subdir, "preprocessed"),
                                        extracted_directory=os.path.join(configs.temp_dir, first_subdir, "extracted"))
            verify(parameters)
            
    if "ijbb" in database:
        import tensorflow as tf
        tf.reset_default_graph()

        # Comparison protocol
        p = "1-1"
        sub_directory = os.path.join("IJBB", resources[baseline]["name"], p)

        # Just to reuse in other experiments
        first_sub_directory = sub_directory
        parameters = trigger_verify(resources[baseline]["ijba_crop"],
                                    resources[baseline]["extractor"],
                                    resources["databases"]["ijbb"],
                                    ["dev"],
                                    sub_directory,
                                    protocol=p,
                                    preprocessed_directory=os.path.join(configs.temp_dir, first_sub_directory, "preprocessed"),
                                    extracted_directory=os.path.join(configs.temp_dir, first_sub_directory, "extracted"))
        verify(parameters)


def main():

    args = docopt(__doc__, version='Run experiment')
    if args["--databases"] == "all":
        database = resources["databases"].keys()
    else:
        database = args["--databases"]

    if args["--baselines"] == "all":
        for b in all_baselines:
            run_cnn_baseline(baseline=b, database=database)
    else:
        run_cnn_baseline(baseline=args["--baselines"], database=database)


if __name__ == "__main__":
    main()
