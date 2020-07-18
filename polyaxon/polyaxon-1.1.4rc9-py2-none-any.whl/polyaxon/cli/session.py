#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from typing import Callable

import click

from polyaxon_sdk.rest import ApiException
from urllib3.exceptions import HTTPError

from polyaxon import pkg
from polyaxon.cli.errors import handle_cli_error
from polyaxon.client import PolyaxonClient
from polyaxon.managers.auth import AuthConfigManager
from polyaxon.managers.cli import CliConfigManager
from polyaxon.utils import indentation
from polyaxon.utils.formatting import Printer
from polyaxon.utils.tz_utils import now


def session_expired():
    AuthConfigManager.purge()
    CliConfigManager.purge()
    click.echo("Session has expired, please try again.")
    sys.exit(1)


def get_server_installation(polyaxon_client=None):
    polyaxon_client = polyaxon_client or PolyaxonClient()
    try:
        return polyaxon_client.versions_v1.get_installtion()
    except ApiException as e:
        if e.status == 403:
            session_expired()
        handle_cli_error(e, message="Could not get cli version.", sys_exit=True)
    except HTTPError:
        Printer.print_error("Could not connect to remote server.", sys_exit=True)


def get_log_handler(polyaxon_client=None):
    polyaxon_client = polyaxon_client or PolyaxonClient()
    try:
        return polyaxon_client.versions_v1.get_log_handler()
    except ApiException as e:
        if e.status == 403:
            session_expired()
        handle_cli_error(e, message="Could not get cli version.", sys_exit=True)
    except HTTPError:
        Printer.print_error("Could not connect to remote server.", sys_exit=True)


def set_versions_config(polyaxon_client=None, set_handler: bool = False):
    polyaxon_client = polyaxon_client or PolyaxonClient()
    server_installation = get_server_installation(polyaxon_client=polyaxon_client)
    log_handler = None
    if set_handler:
        log_handler = get_log_handler(polyaxon_client=polyaxon_client)
    return CliConfigManager.reset(
        last_check=now(),
        current_version=pkg.VERSION,
        server_installation=server_installation.to_dict(),
        log_handler=log_handler,
    )


def verify_version(config, pip_upgrade: Callable = None):
    """Check if the current version satisfies the server requirements"""
    from distutils.version import LooseVersion  # pylint:disable=import-error

    if LooseVersion(config.current_version) < LooseVersion(config.min_version):
        click.echo(
            """Your version of CLI ({}) is no longer compatible with server.""".format(
                config.current_version
            )
        )
        if pip_upgrade and click.confirm(
            "Do you want to upgrade to " "version {} now?".format(config.latest_version)
        ):
            pip_upgrade()
            sys.exit(0)
        else:
            indentation.puts("Your can manually run:")
            with indentation.indent(4):
                indentation.puts("pip install -U polyaxon-cli")
            indentation.puts(
                "to upgrade to the latest version `{}`".format(config.latest_version)
            )

            sys.exit(0)
    elif LooseVersion(config.current_version) < LooseVersion(config.latest_version):
        indentation.puts(
            "New version of CLI ({}) is now available. To upgrade run:".format(
                config.latest_version
            )
        )
        with indentation.indent(4):
            indentation.puts("pip install -U polyaxon")
    elif LooseVersion(config.current_version) > LooseVersion(config.latest_version):
        indentation.puts(
            "Your version of CLI ({}) is ahead of the latest version "
            "supported by Polyaxon Platform ({}) on your cluster, "
            "and might be incompatible.".format(
                config.current_version, config.latest_version
            )
        )
