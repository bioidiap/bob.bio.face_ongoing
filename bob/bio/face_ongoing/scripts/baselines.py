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
from bob.bio.face_ongoing.baselines import get_all_baselines_by_type, get_all_baselines, get_all_databases
from bob.extension import rc
from bob.extension.scripts.click_helper import verbosity_option
from bob.extension.scripts.click_helper import (
    verbosity_option, ConfigCommand, ResourceOption)
import click


all_baselines = get_all_baselines()
all_databases = get_all_databases()
all_baselines_by_type = get_all_baselines_by_type()


def trigger_verify(result_dir, temp_dir, preprocessor, extractor, database, groups, sub_directory, protocol=None,
                   preprocessed_directory=None, extracted_directory=None):
    
    result_dir = str(rc['bob_faceongoing_results_dir']) if result_dir is None else result_dir
    temp_dir = str(rc['bob_faceongoing_temp_dir']) if temp_dir is None else temp_dir

    parameters = [
        preprocessor,
        extractor,
        '-d', database,
        '-a', "distance-cosine",
        '-g', 'demanding',
        '-G','submitted_experiments.sql3',
        '-vvv',
        '--temp-directory', temp_dir,
        '--result-directory', result_dir,
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


def run_cnn_baseline(baseline, database, result_dir, temp_dir):

    for p in all_databases[database].protocols:
        import tensorflow as tf
        tf.reset_default_graph()

        sub_directory = os.path.join(all_databases[database].name, all_baselines[baseline].name, p.replace(":",""))
        # Taking care of the directories
        if all_databases[database].preprocessed_directory is None:
            preprocessed_directory = all_databases[database].preprocessed_directory
        else:
            preprocessed_directory = os.path.join(rc['bob_faceongoing_temp_dir'], all_databases[database].name, all_baselines[baseline].name,
                                                  all_databases[database].preprocessed_directory)
            
        # Taking care of the directories
        if all_databases[database].extracted_directory is None:
            extracted_directory = all_databases[database].extracted_directory
        else:
            extracted_directory = os.path.join(rc['bob_faceongoing_temp_dir'],  all_databases[database].name, all_baselines[baseline].name,
                                               all_databases[database].extracted_directory)
        
        parameters = trigger_verify(result_dir, temp_dir,
                                    all_baselines[baseline].preprocessors["{0}_crop".format(database)],
                                    all_baselines[baseline].extractor,
                                    all_databases[database].config,
                                    all_databases[database].groups,
                                    sub_directory,
                                    protocol=p,
                                    preprocessed_directory=preprocessed_directory,
                                    extracted_directory=extracted_directory)
        verify(parameters)


@click.group()
@verbosity_option()
def face_ongoing():
    """The manager for the face ongoing baselines"""
    pass


@face_ongoing.command()
def show():
    """
    List all the registered baselines and databases
    """
    import tabulate

    click.echo("====================================")
    click.echo("Follow all the registered databases:")
    click.echo("===================================="+"\n")
    
    click.echo(tabulate.tabulate([[_ for _ in all_databases]+["all"]], tablefmt="simple"))

    click.echo("====================================")
    click.echo("Follow all the registered baselines:")
    click.echo("====================================")
    for a in all_baselines_by_type:
        click.echo("Baselines of the type: %s"%(a))
        for b in all_baselines_by_type[a]:
            click.echo("  >> %s"%(b))
        click.echo("\n")


@face_ongoing.command(entry_point_group='bob.bio.config', cls=ConfigCommand)
@click.option('--database', '-d', required=True, cls=ResourceOption, help="Registered database", type=click.Choice([_ for _ in all_databases]+["all"]))
@click.option('--baseline', '-b', required=True, cls=ResourceOption, help="Registered baseline", type=click.Choice([_ for _ in all_baselines]+["all"]))

@click.option('--temp-dir', '-t', required=False, cls=ResourceOption, help="Temp directory. If not set, this value will be take from Bob Global Configuration Variable rc['bob_faceongoing_temp_dir']")
@click.option('--result-dir', '-r', required=False, cls=ResourceOption, help="Result directory. If not set, this value will be take from Bob Global Configuration Variable rc['bob_faceongoing_result_dir']")
def run(baseline, database, temp_dir, result_dir, **kwargs):
    """
    Run a particular baseline
    """

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
            run_cnn_baseline(baseline=b, database=d, result_dir=result_dir, temp_dir=temp_dir)

