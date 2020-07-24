#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""Use command line to operate on data sets through click."""

import os
import sys
from concurrent.futures import FIRST_EXCEPTION, ThreadPoolExecutor, wait
from configparser import ConfigParser
from pathlib import Path, PurePosixPath
from typing import Dict, Iterator, List, Tuple

import click
from click import Context

from . import __version__
from .data_set import NormalDataSet
from .gas import GAS


def _config_filepath() -> str:
    """Get the path of the config file.

    :return: the path of the config file
    """
    home = "HOMEPATH" if os.name == "nt" else "HOME"
    return os.path.join(os.environ[home], ".gasconfig")


def _gas(url: str, access_key: str) -> GAS:
    """Load an object of class <GAS>.

    :param url: the login url
    :param access_key: the accessKey of gas
    :return: the loaded gas from config file
    """
    config_file = _config_filepath()

    if not os.path.exists(config_file):
        click.echo(
            f"{config_file} not exist\n\nPlease use 'gas config <accessKey>' to create config file",
            err=True,
        )
        sys.exit(1)

    if not access_key:
        config_parser = ConfigParser()
        config_parser.read(config_file)
        access_key = config_parser["Credentials"]["accessKey"]
    if url:
        return GAS(access_key, url=url)
    return GAS(access_key)


@click.group()
@click.version_option(version=__version__, message="%(version)s")
@click.option("-u", "--url", type=str, help="The login url.")
@click.option("-k", "--key", type=str, help="The accessKey of gas.")
@click.pass_context
def cli(ctx: Context, url: str = "", key: str = "") -> None:  # pylint: disable=invalid-name
    """You can use 'gas' + COMMAND to operate on your data set.\f

    :param ctx: the context to be passed as first argument
    :param url: the login url
    :param key: the accessKey of gas
    """
    ctx.obj = {
        "url": url,
        "access_key": key,
    }


@cli.command()
@click.argument("name", type=str)
@click.pass_obj
def create(obj: Dict[str, str], name: str) -> None:
    """Create a data set named NAME.\f

    :param obj: a dictionary including config info
    :param name: the name of the data set to be created
    """
    _gas(**obj).create_data_set(name)


@cli.command()
@click.argument("name", type=str)
@click.pass_obj
def publish(obj: Dict[str, str], name: str) -> None:
    """Publish a data set named NAME.\f

    :param obj: a dictionary including config info
    :param name: the name of the data set to be published
    """
    data_set = _gas(**obj).get_data_set(name)
    data_set.publish()


@cli.command()
@click.argument("name", type=str)
@click.pass_obj
def delete(obj: Dict[str, str], name: str) -> None:
    """Delete a data set named NAME.\f

    :param obj: a dictionary including config info
    :param name: the name of the data set to be deleted
    """
    _gas(**obj).delete_data_set(name)


@cli.command()
@click.argument("local_paths", type=str, nargs=-1)
@click.argument("remote_path", type=str, nargs=1)
@click.option(
    "-r", "--recursive", "is_recursive", is_flag=True, help="Copy directories recursively."
)
@click.option("-j", "--jobs", type=int, default=1, help="The number of threads.")
@click.pass_obj
def cp(  # pylint: disable=invalid-name
    obj: Dict[str, str], local_paths: Tuple[str], remote_path: str, is_recursive: bool, jobs: int
) -> None:
    """Copy local data to a remote path.\f

    :param obj: a dictionary including config info
    :param local_paths: a tuple of local paths containing data to be uploaded
    :param remote_path: the path to save the uploaded data, like:
      "dataset_name://remote_path"
    :param is_recursive: whether copy directories recursively
    """
    if "://" not in remote_path:
        click.echo("Error: remote path should follow dataset_name://remote_path", err=True)
        sys.exit(1)

    dataset_name, remote_path = remote_path.split("://")
    data_set = _gas(**obj).get_or_create_data_set(dataset_name)
    local_abspaths: List[str] = [os.path.abspath(local_path) for local_path in local_paths]

    if (
        len(local_abspaths) == 1
        and not os.path.isdir(local_abspaths[0])
        and remote_path
        and not remote_path.endswith("/")
    ):
        data_set.upload_data(local_abspaths[0], remote_path)
        return

    path_mapping = _path_mapping(local_abspaths, remote_path, is_recursive)
    _multithread_upload(data_set, path_mapping, jobs)


def _multithread_upload(data_set: NormalDataSet, path_mapping: Dict[str, str], jobs: int) -> None:
    """Upload local data to the appointed data set with multi-threads.

    :param data_set: the data set to upload data to
    :param path_mapping: a dict of local-remote pairs
    :param jobs: the number of threads
    """
    futures = []
    with ThreadPoolExecutor(jobs) as executor:
        for local_file, remote_file in path_mapping.items():
            futures.append(executor.submit(data_set.upload_data, local_file, remote_file))

        done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
        for future in not_done:
            future.cancel()
        for future in done:
            future.result()


def _path_mapping(
    local_abspaths: List[str], remote_path: str, is_recursive: bool
) -> Dict[str, str]:
    """Get the pair of local_path and remote_path.

    :param local_abspaths: a list of local abstract paths, could be folder or file
    :param remote_path: remote path, not necessarily end with '/'
    :param is_recursive: whether copy directories recursively
    :return: a dict of local-remote pairs
    """
    path_mapping: Dict[str, str] = {}

    for local_abspath in local_abspaths:
        if not os.path.isdir(local_abspath):
            path_mapping[local_abspath] = str(
                PurePosixPath(remote_path) / os.path.basename(local_abspath)
            )
            continue

        if not is_recursive:
            click.echo(
                "Error: local paths include directories, please use -r option", err=True,
            )
            sys.exit(1)

        local_abspath = os.path.normpath(local_abspath)
        folder_name = os.path.basename(local_abspath)
        for root, _, filenames in os.walk(local_abspath):
            relpath = os.path.relpath(root, local_abspath) if root != local_abspath else ""
            for filename in filenames:
                path_mapping[os.path.join(root, filename)] = str(
                    PurePosixPath(Path(os.path.join(remote_path, folder_name, relpath, filename)))
                )
    return path_mapping


@cli.command()
@click.argument("remote_path", type=str, default="")
@click.pass_obj
def ls(obj: Dict[str, str], remote_path: str) -> None:  # pylint: disable=invalid-name
    """List data of the remote path. If remote path is empty, list the names of all data sets.\f

    :param obj: a dictionary including config info
    :param remote_path: The remote path to be listed, like "dataset_name://remote_path".
      If empty, list the names of all data sets.
    """
    gas = _gas(**obj)

    if not remote_path:
        dataset_names = gas.list_data_sets()
        for dataset_name in dataset_names:
            click.echo(dataset_name)
        return

    if "://" not in remote_path:
        click.echo("Error: remote path should follow dataset_name://remote_path", err=True)
        sys.exit(1)

    dataset_name, remote_path = remote_path.split("://")
    data_set = gas.get_data_set(dataset_name)
    filter_data = _filter_data(data_set, remote_path, is_recursive=True)
    for data in filter_data:
        click.echo(data)


@cli.command()
@click.argument("remote_path", type=str)
@click.option(
    "-r", "--recursive", "is_recursive", is_flag=True, help="Remove directories recursively."
)
@click.pass_obj
# pylint: disable=invalid-name
def rm(obj: Dict[str, str], remote_path: str, is_recursive: bool) -> None:
    """Remove the remote paths.\f

    :param obj: a dictionary including config info
    :param remote_path: The remote path to be removed, like "dataset_name://remote_path".
    :param is_recursive: whether remove directories recursively
    """
    if "://" not in remote_path:
        click.echo("Error: remote path should follow dataset_name://remote_path", err=True)
        sys.exit(1)

    if remote_path.endswith("/") and not is_recursive:
        click.echo("Error: remote paths include directories, please use -r option", err=True)
        sys.exit(1)

    dataset_name, remote_path = remote_path.split("://")
    data_set = _gas(**obj).get_data_set(dataset_name)
    delete_data_list = list(_filter_data(data_set, remote_path, is_recursive))
    if not delete_data_list:
        echo_info = "file or directory" if is_recursive else "file"
        click.echo(f"Error: no such {echo_info} '{dataset_name}://{remote_path}'", err=True)
        sys.exit(1)

    data_set.delete_data(delete_data_list)


@cli.command()
@click.argument("access_key", type=str)
def config(access_key: str) -> None:
    """Configure the accessKey of gas.\f

    :param access_key: the accessKey of gas to be written into ".gasconfig"
    """
    config_info = ConfigParser()
    config_info.add_section("Credentials")
    config_info["Credentials"]["accessKey"] = access_key
    config_file = _config_filepath()
    with open(config_file, "w") as file:
        config_info.write(file)

    click.echo(f"Success!\naccessKey has been written into: {config_file}")


def _filter_data(data_set: NormalDataSet, remote_path: str, is_recursive: bool) -> Iterator[str]:
    """Get a data list according to the remote path.

    :param data_set: object of DataSet
    :param remote_path: the remote path of the data set
    :param is_recursive: whether filter data recursively or not
    :return: object of type filter
    """
    data_list = data_set.list_data()

    if not is_recursive:
        return filter(lambda x: x == remote_path, data_list)

    if not remote_path or remote_path.endswith("/"):
        return filter(lambda x: x.startswith(remote_path), data_list)

    return filter(lambda x: x.startswith(remote_path + "/") or x == remote_path, data_list)


if __name__ == "__main__":
    cli(None)
