#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

"""
This script runs some face recognition baselines under some face databases

Run `bob faceongoing show` to list all the baselines and databases available

Examples:

This command line will run the facenet from David Sandberg using the IJB-A dataset:
  `bob faceongoing run --baseline facenet_msceleba_inception_v1 --database ijba`
  

This command line will run all the registed baselines using all databases registered databases::
  `bob faceongoing run --baseline all --database all`

"""


import bob.bio.base
import bob.io.base
import os
from bob.extension.config import load
import pkg_resources
from docopt import docopt
from bob.bio.base.script.verify import main as verify
from bob.bio.face_ongoing.baselines import get_available_databases
from bob.extension import rc
from bob.extension.scripts.click_helper import verbosity_option
from bob.extension.scripts.click_helper import (
    verbosity_option, ConfigCommand, ResourceOption)
import click


all_baselines = bob.bio.base.resource_keys('baselines', package_prefix='bob.bio.face.')
all_databases = get_available_databases()
#all_baselines_by_type = get_all_baselines_by_type()


@click.group()
@verbosity_option()
def face_ongoing():
    """The manager for the face ongoing baselines"""
    pass


@face_ongoing.command(entry_point_group='bob.bio.config', cls=ConfigCommand)
@click.option('--database', '-d', required=True, cls=ResourceOption, help="Registered database", type=click.Choice([_ for _ in all_databases]+["all"]))
@click.option('--baseline', '-b', required=True, cls=ResourceOption, help="Registered baseline", type=click.Choice([_ for _ in all_baselines]+["all"]))
@click.option('--temp-dir', '-T', required=False, cls=ResourceOption, help="Temp directory. If not set, this value will be take from Bob Global Configuration Variable rc['bob_faceongoing_temp_dir']")
@click.option('--result-dir', '-R', required=False, cls=ResourceOption, help="Result directory. If not set, this value will be take from Bob Global Configuration Variable rc['bob_faceongoing_result_dir']")
@click.option('--grid', '-g', help="Execute the algorithm in the SGE grid.", is_flag=True)
@click.option('--zt-norm', '-z', help="Enable the computation of ZT norms (if the database supports it).", is_flag=True)
def baselines(baseline, database, temp_dir, result_dir, grid, zt_norm, **kwargs):
    """
    Run a particular baseline
    """

    def search_preprocessor(key, keys):
        """
        Wrapper that searches for preprocessors for specific databases.
        If not found, the default preprocessor is returned
        """
        for k in keys:
            if key.startswith(k):
                return k
        else:
            return "default"

    if database == "all":
        database = all_databases
    else:
        database = [database]

    if baseline == "all":
        baselines = all_baselines
    else:
        baselines = [baseline]

    # Triggering training for each baseline/database    
    for b in baselines:
        for d in database:

            loaded_baseline = bob.bio.base.load_resource(b, 'baselines', package_prefix="bob.bio.face.")

            # this is the default sub-directory that is used
            sub_directory = os.path.join(d, b)
            database_data = get_available_databases()[d]
            parameters = [
                '-p', loaded_baseline.preprocessors[search_preprocessor(d, loaded_baseline.preprocessors.keys())],
                '-e', loaded_baseline.extractor,
                '-d', d,
                '-a', loaded_baseline.algorithm,
                '-vvv',
                '--temp-directory', temp_dir,
                '--result-directory', result_dir,
                '--sub-directory', sub_directory
            ]
            
            parameters += ['--groups'] + database_data["groups"]

            if grid:
                parameters += ['-g', 'demanding']

            if zt_norm and 'has_zt' in database_data.keys():
                parameters += ['--zt-norm']

            verify(parameters)


