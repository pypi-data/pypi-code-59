# coding: utf8
from __future__ import print_function, absolute_import

import os
import click
import json
from tabulate import tabulate
from fds import GalaxyFDSClientException
from cloudpretrain.config import default_config
from cloudpretrain.utils.fds import listing_generator, load_object, check_object_exists, upload_file_to_fds, remove_dir
from cloudpretrain.utils.colors import error, colorize, success
from cloudpretrain.constants import DATASET_PREFIX, CLOUD_PRETRAIN_BUCKET
from cloudpretrain.constants import TRAIN_FILE_NAME, DEV_FILE_NAME, TEST_FILE_NAME, DES_FILE_NAME


@click.group()
def datasets():
    """dataset"""
    if not default_config.validate():
        click.echo(colorize(":red{Config file not exists. Try }:yellow{'cloud-pretrain init'}:red{ to initialize.}"))
        exit()


@datasets.command("list", help="List available datasets.")
def list_datasets():
    click.echo(success("------------Public-------------------:"))
    _list_datasets(CLOUD_PRETRAIN_BUCKET)
    
    click.echo(success("\n------------Private-------------------:"))
    _list_datasets(default_config.fds_bucket)
    

@datasets.command("upload", help="upload dataset to fds.")
@click.option("-d", "--dir", "dataset_folder", type=click.Path(exists=True, dir_okay=True), required=True,
              help="dataset folder, which should have four files in the folder (des.json / train.txt / dev.txt / test.txt)")
@click.option("-p", "--public", is_flag=True, default=False, help="if set, the datasets will be public datasets, every user can view and use")
@click.option("-g", "--group", default="default", help="put the dataset under this group")
def upload_dataset(dataset_folder, public, group):
     # exists
    if not os.path.exists(dataset_folder):
        click.echo("dataset with same name and version exists")
        return
    
    # have the target files with same names
    files = os.listdir(dataset_folder)

    if len(files) < 4 or TRAIN_FILE_NAME not in files or DEV_FILE_NAME not in files or TEST_FILE_NAME not in files or DES_FILE_NAME not in files:
        click.echo("predefined files not in folder")
        return
    
    # get the name and version
    with open(dataset_folder + "/" + DES_FILE_NAME) as json_file:
        content = json.load(json_file)

        if "name" not in content or "version" not in content:
            click.echo("name / version not in des.json")
            return
    
        name = content["name"]
        version = content["version"]

        # check if we have same folder in fds
        folder_prefix = os.path.join(DATASET_PREFIX, group, name, str(version)).replace('\\', '/')

        bucket_name = default_config.fds_bucket

        if public:
            bucket_name = CLOUD_PRETRAIN_BUCKET

        if check_object_exists(bucket_name, os.path.join(group, folder_prefix, DES_FILE_NAME).replace('\\', '/')):
            click.echo("target folder exists in fds, use new name or version")
            return
        
        # try to upload the data
        _upload_data(dataset_folder, TRAIN_FILE_NAME, folder_prefix, bucket_name)
        _upload_data(dataset_folder, DEV_FILE_NAME, folder_prefix, bucket_name)
        _upload_data(dataset_folder, TEST_FILE_NAME, folder_prefix, bucket_name)
        _upload_data(dataset_folder, DES_FILE_NAME, folder_prefix, bucket_name)

        click.echo("dataset uploaded")


@datasets.command("delete", help="delete private dataset (for public dataset, pls contact cloud-pretrain team for deleting)")
@click.option("-n", "--name", "name", required=True, help="dataset name")
@click.option("-v", "--version", "version", required=True, help="dataset version")
@click.option("-g", "--group", "group", default="default", help="dataset group")
def delete(name, version, group):
    bucket_name = default_config.fds_bucket
    
    # check if we can find the dataset
    dataset_path = os.path.join(DATASET_PREFIX, group, name, str(version))

    if not check_object_exists(bucket_name, os.path.join(dataset_path, DES_FILE_NAME)):
        click.echo(error("can not find {} with version {}".format(name, version)))
        return
    
    remove_dir(bucket_name, dataset_path)

    click.echo("Done")


def _upload_data(local_folder, file_name, fds_folder, bucket_name):
    local_path = os.path.join(local_folder, file_name)
    fds_folder = os.path.join(fds_folder, file_name)

    upload_file_to_fds(bucket_name, local_path, fds_folder)


def _list_datasets(bucket):

    tables = {}
    
    for listing in listing_generator(bucket, DATASET_PREFIX):
        for group_name in listing.common_prefixes:
            _, name = os.path.split(os.path.split(group_name)[0])

            show_datas = _list_group_datasets(bucket, group_name)

            if len(show_datas):
                tables[name] = show_datas
    
    if len(tables) == 0:
        click.echo("No dataset found")
    
    for k, v in tables.items():
        click.echo(success("group: {}".format(k)))
        click.echo(tabulate(v, headers=["NAME", "PROBLEM", "VERSION", "DATE", "OWNER", "COUNT"]))
        click.echo("\n")


def _list_group_datasets(bucket_name, group_name):
    table = []
    for listing in listing_generator(bucket_name, group_name):
        for dataset_prefix in listing.common_prefixes:
            for version_list in listing_generator(bucket_name, dataset_prefix):
                for version in version_list.common_prefixes:
                    
                    try:
                        content = load_object(bucket_name, version  + DES_FILE_NAME)

                        content = json.loads(content)
                        name = content.get("name")
                        problem = content.get("problem")
                        version = content.get("version")
                        date = content.get("date")
                        owner = content.get("owner")
                        count = content.get("count")

                        row = [name, problem, version, date, owner, count]
                        table.append(row)
                    except GalaxyFDSClientException as ex:
                        click.echo(error("exceptions during list the datset: {}".format(ex.message)))
                        continue
    return table