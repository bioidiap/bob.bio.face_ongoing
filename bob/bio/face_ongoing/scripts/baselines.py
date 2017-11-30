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

all_baselines = ["idiap_msceleba_inception_v2",
                 "facenet_inception_v1_msceleb",
                 "idiap_inception_v2_casia",
                 "idiap_inception_v2_casia_GRAY",
                 "idiap_inception_v2_msceleb_GRAY",
                 "vgg16"]

# Mapping databases
resources["databases"] = dict()
resources["databases"]["mobio"] = "mobio-male"
resources["databases"]["ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/databases/ijba.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2"] = dict()
resources["idiap_msceleba_inception_v2"]["name"] = "idiap_casia_inception_v2"
resources["idiap_msceleba_inception_v2"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/inception_v2.py")
resources["idiap_msceleba_inception_v2"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_mobio.py")
resources["idiap_msceleba_inception_v2"]["ijba_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/idiap_msceleba_inception_v2/crop_ijba.py")

# idiap_msceleba_inception_v2
resources["idiap_msceleba_inception_v2_gray"] = dict()
resources["idiap_msceleba_inception_v2_gray"]["name"] = "idiap_casia_inception_v2_gray"
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
resources["vgg16"]["mobio_ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/vgg16/crop_ijba.py")

# vgg-16
resources["facenet_msceleba_inception_v1"] = dict()
resources["facenet_msceleba_inception_v1"]["name"] = "facenet_msceleba_inception_v1"
resources["facenet_msceleba_inception_v1"]["extractor"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/inception_v1.py")
resources["facenet_msceleba_inception_v1"]["mobio_crop"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_mobio.py")
resources["facenet_msceleba_inception_v1"]["mobio_ijba"] = pkg_resources.resource_filename("bob.bio.face_ongoing", "configs/baselines/facenet_msceleba_inception_v1/crop_ijba.py")


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
        '-g', 'demmanding',
        '--temp-directory', configs.temp_dir,
        '--result-directory', configs.results_dir,
        '--sub-directory', sub_directory
    ] + ['--groups'] + groups
    
    if protocol is not None:
        parameters += ['--protocol', protocol]

    if preprocessed_directory is not None:
        parameters += ['--preprocessed-directory', preprocessed_directory]

    if extracted_directory is not None:
        parameters += ['--extracted-directory', extracted_directory]


    return parameters


def run_cnn_baseline(baseline):

    # Triggering mobio
    parameters = trigger_verify(resources[baseline]["mobio_crop"],
                                resources[baseline]["extractor"],
                                "mobio-male",
                                ["dev", "eval"],
                                "MOBIO/"+resources[baseline]["name"],
                                protocol=None)
    verify(parameters)

    for p in ijba_comparison_protocols:
        parameters = trigger_verify(resources[baseline]["ijba_crop"],
                                    resources[baseline]["extractor"],
                                    resources["databases"]["ijba"],
                                    ["dev"],
                                    "IJBA/"+resources[baseline]["name"]+"/"+p,
                                    protocol=p)
        verify(parameters)


def main():

    args = docopt(__doc__, version='Run experiment')
    run_cnn_baseline
    if args["--baselines"] == "all":
        for b in all_baselines:
            run_cnn_baseline(baseline=b)
    else:
        run_cnn_baseline(baseline=args["--baselines"])


if __name__ == "__main__":
    main()
