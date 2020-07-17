# -*- coding: utf-8 -*-
import click
import urllib3
import os
from dnacentersdk import DNACenterAPI
from dnacentercli.environment import (
    DNA_CENTER_USERNAME,
    DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH,
    DNA_CENTER_DEBUG,
    DNA_CENTER_VERSION,
    DNA_CENTER_BASE_URL,
    DNA_CENTER_SINGLE_REQUEST_TIMEOUT,
    DNA_CENTER_WAIT_ON_RATE_LIMIT,
    DNA_CENTER_VERIFY,
)
from .utils.spinner import (
    init_spinner,
    start_spinner,
    stop_spinner,
)
from .utils.print import (
    tbprint,
    eprint,
    oprint,
    opprint,
)

from .v1_2_10.clients import \
    clients as v1_2_10_clients
from .v1_2_10.command_runner import \
    command_runner as v1_2_10_command_runner
from .v1_2_10.devices import \
    devices as v1_2_10_devices
from .v1_2_10.fabric_wired import \
    fabric_wired as v1_2_10_fabric_wired
from .v1_2_10.file import \
    file as v1_2_10_file
from .v1_2_10.network_discovery import \
    network_discovery as v1_2_10_network_discovery
from .v1_2_10.networks import \
    networks as v1_2_10_networks
from .v1_2_10.non_fabric_wireless import \
    non_fabric_wireless as v1_2_10_non_fabric_wireless
from .v1_2_10.path_trace import \
    path_trace as v1_2_10_path_trace
from .v1_2_10.pnp import \
    pnp as v1_2_10_pnp
from .v1_2_10.swim import \
    swim as v1_2_10_swim
from .v1_2_10.site_profile import \
    site_profile as v1_2_10_site_profile
from .v1_2_10.sites import \
    sites as v1_2_10_sites
from .v1_2_10.tag import \
    tag as v1_2_10_tag
from .v1_2_10.task import \
    task as v1_2_10_task
from .v1_2_10.template_programmer import \
    template_programmer as v1_2_10_template_programmer
from .v1_3_0.clients import \
    clients as v1_3_0_clients
from .v1_3_0.command_runner import \
    command_runner as v1_3_0_command_runner
from .v1_3_0.devices import \
    devices as v1_3_0_devices
from .v1_3_0.fabric_wired import \
    fabric_wired as v1_3_0_fabric_wired
from .v1_3_0.file import \
    file as v1_3_0_file
from .v1_3_0.network_discovery import \
    network_discovery as v1_3_0_network_discovery
from .v1_3_0.networks import \
    networks as v1_3_0_networks
from .v1_3_0.non_fabric_wireless import \
    non_fabric_wireless as v1_3_0_non_fabric_wireless
from .v1_3_0.path_trace import \
    path_trace as v1_3_0_path_trace
from .v1_3_0.pnp import \
    pnp as v1_3_0_pnp
from .v1_3_0.swim import \
    swim as v1_3_0_swim
from .v1_3_0.site_profile import \
    site_profile as v1_3_0_site_profile
from .v1_3_0.sites import \
    sites as v1_3_0_sites
from .v1_3_0.tag import \
    tag as v1_3_0_tag
from .v1_3_0.task import \
    task as v1_3_0_task
from .v1_3_0.template_programmer import \
    template_programmer as v1_3_0_template_programmer
from .v1_3_1.application_policy import \
    application_policy as v1_3_1_application_policy
from .v1_3_1.clients import \
    clients as v1_3_1_clients
from .v1_3_1.command_runner import \
    command_runner as v1_3_1_command_runner
from .v1_3_1.configuration_templates import \
    configuration_templates as v1_3_1_configuration_templates
from .v1_3_1.device_onboarding_pnp import \
    device_onboarding_pnp as v1_3_1_device_onboarding_pnp
from .v1_3_1.devices import \
    devices as v1_3_1_devices
from .v1_3_1.event_management import \
    event_management as v1_3_1_event_management
from .v1_3_1.fabric_wired import \
    fabric_wired as v1_3_1_fabric_wired
from .v1_3_1.file import \
    file as v1_3_1_file
from .v1_3_1.issues import \
    issues as v1_3_1_issues
from .v1_3_1.network_discovery import \
    network_discovery as v1_3_1_network_discovery
from .v1_3_1.network_settings import \
    network_settings as v1_3_1_network_settings
from .v1_3_1.non_fabric_wireless import \
    non_fabric_wireless as v1_3_1_non_fabric_wireless
from .v1_3_1.path_trace import \
    path_trace as v1_3_1_path_trace
from .v1_3_1.site_design import \
    site_design as v1_3_1_site_design
from .v1_3_1.sites import \
    sites as v1_3_1_sites
from .v1_3_1.software_image_management_swim import \
    software_image_management_swim as v1_3_1_software_image_management_swim
from .v1_3_1.tag import \
    tag as v1_3_1_tag
from .v1_3_1.task import \
    task as v1_3_1_task
from .v1_3_1.topology import \
    topology as v1_3_1_topology
from .v1_3_1.users import \
    users as v1_3_1_users
from .v1_3_3.application_policy import \
    application_policy as v1_3_3_application_policy
from .v1_3_3.clients import \
    clients as v1_3_3_clients
from .v1_3_3.command_runner import \
    command_runner as v1_3_3_command_runner
from .v1_3_3.configuration_templates import \
    configuration_templates as v1_3_3_configuration_templates
from .v1_3_3.device_onboarding_pnp import \
    device_onboarding_pnp as v1_3_3_device_onboarding_pnp
from .v1_3_3.devices import \
    devices as v1_3_3_devices
from .v1_3_3.discovery import \
    discovery as v1_3_3_discovery
from .v1_3_3.event_management import \
    event_management as v1_3_3_event_management
from .v1_3_3.file import \
    file as v1_3_3_file
from .v1_3_3.issues import \
    issues as v1_3_3_issues
from .v1_3_3.network_settings import \
    network_settings as v1_3_3_network_settings
from .v1_3_3.path_trace import \
    path_trace as v1_3_3_path_trace
from .v1_3_3.sda import \
    sda as v1_3_3_sda
from .v1_3_3.site_design import \
    site_design as v1_3_3_site_design
from .v1_3_3.sites import \
    sites as v1_3_3_sites
from .v1_3_3.software_image_management_swim import \
    software_image_management_swim as v1_3_3_software_image_management_swim
from .v1_3_3.tag import \
    tag as v1_3_3_tag
from .v1_3_3.task import \
    task as v1_3_3_task
from .v1_3_3.topology import \
    topology as v1_3_3_topology
from .v1_3_3.users import \
    users as v1_3_3_users
from .v1_3_3.wireless import \
    wireless as v1_3_3_wireless
from .v2_1_1.application_policy import \
    application_policy as v2_1_1_application_policy
from .v2_1_1.clients import \
    clients as v2_1_1_clients
from .v2_1_1.command_runner import \
    command_runner as v2_1_1_command_runner
from .v2_1_1.configuration_templates import \
    configuration_templates as v2_1_1_configuration_templates
from .v2_1_1.device_onboarding_pnp import \
    device_onboarding_pnp as v2_1_1_device_onboarding_pnp
from .v2_1_1.device_replacement import \
    device_replacement as v2_1_1_device_replacement
from .v2_1_1.devices import \
    devices as v2_1_1_devices
from .v2_1_1.discovery import \
    discovery as v2_1_1_discovery
from .v2_1_1.event_management import \
    event_management as v2_1_1_event_management
from .v2_1_1.file import \
    file as v2_1_1_file
from .v2_1_1.itsm import \
    itsm as v2_1_1_itsm
from .v2_1_1.issues import \
    issues as v2_1_1_issues
from .v2_1_1.network_settings import \
    network_settings as v2_1_1_network_settings
from .v2_1_1.path_trace import \
    path_trace as v2_1_1_path_trace
from .v2_1_1.sda import \
    sda as v2_1_1_sda
from .v2_1_1.site_design import \
    site_design as v2_1_1_site_design
from .v2_1_1.sites import \
    sites as v2_1_1_sites
from .v2_1_1.software_image_management_swim import \
    software_image_management_swim as v2_1_1_software_image_management_swim
from .v2_1_1.tag import \
    tag as v2_1_1_tag
from .v2_1_1.task import \
    task as v2_1_1_task
from .v2_1_1.topology import \
    topology as v2_1_1_topology
from .v2_1_1.users import \
    users as v2_1_1_users
from .v2_1_1.wireless import \
    wireless as v2_1_1_wireless


def version_set(ctx, param, value):
    if value not in ['1.2.10', '1.3.0', '1.3.1', '1.3.3', '2.1.1']:
        ctx.fail(
            'Unknown API version, '
            + 'known versions are {}'.format(
                '1.2.10, 1.3.0, 1.3.1, 1.3.3 and 2.1.1.'
            )
        )
    if value == '1.2.10':
        main.add_command(v1_2_10_clients)
        main.add_command(v1_2_10_command_runner)
        main.add_command(v1_2_10_devices)
        main.add_command(v1_2_10_fabric_wired)
        main.add_command(v1_2_10_file)
        main.add_command(v1_2_10_network_discovery)
        main.add_command(v1_2_10_networks)
        main.add_command(v1_2_10_non_fabric_wireless)
        main.add_command(v1_2_10_path_trace)
        main.add_command(v1_2_10_pnp)
        main.add_command(v1_2_10_swim)
        main.add_command(v1_2_10_site_profile)
        main.add_command(v1_2_10_sites)
        main.add_command(v1_2_10_tag)
        main.add_command(v1_2_10_task)
        main.add_command(v1_2_10_template_programmer)
    if value == '1.3.0':
        main.add_command(v1_3_0_clients)
        main.add_command(v1_3_0_command_runner)
        main.add_command(v1_3_0_devices)
        main.add_command(v1_3_0_fabric_wired)
        main.add_command(v1_3_0_file)
        main.add_command(v1_3_0_network_discovery)
        main.add_command(v1_3_0_networks)
        main.add_command(v1_3_0_non_fabric_wireless)
        main.add_command(v1_3_0_path_trace)
        main.add_command(v1_3_0_pnp)
        main.add_command(v1_3_0_swim)
        main.add_command(v1_3_0_site_profile)
        main.add_command(v1_3_0_sites)
        main.add_command(v1_3_0_tag)
        main.add_command(v1_3_0_task)
        main.add_command(v1_3_0_template_programmer)
    if value == '1.3.1':
        main.add_command(v1_3_1_application_policy)
        main.add_command(v1_3_1_clients)
        main.add_command(v1_3_1_command_runner)
        main.add_command(v1_3_1_configuration_templates)
        main.add_command(v1_3_1_device_onboarding_pnp)
        main.add_command(v1_3_1_devices)
        main.add_command(v1_3_1_event_management)
        main.add_command(v1_3_1_fabric_wired)
        main.add_command(v1_3_1_file)
        main.add_command(v1_3_1_issues)
        main.add_command(v1_3_1_network_discovery)
        main.add_command(v1_3_1_network_settings)
        main.add_command(v1_3_1_non_fabric_wireless)
        main.add_command(v1_3_1_path_trace)
        main.add_command(v1_3_1_site_design)
        main.add_command(v1_3_1_sites)
        main.add_command(v1_3_1_software_image_management_swim)
        main.add_command(v1_3_1_tag)
        main.add_command(v1_3_1_task)
        main.add_command(v1_3_1_topology)
        main.add_command(v1_3_1_users)
    if value == '1.3.3':
        main.add_command(v1_3_3_application_policy)
        main.add_command(v1_3_3_clients)
        main.add_command(v1_3_3_command_runner)
        main.add_command(v1_3_3_configuration_templates)
        main.add_command(v1_3_3_device_onboarding_pnp)
        main.add_command(v1_3_3_devices)
        main.add_command(v1_3_3_discovery)
        main.add_command(v1_3_3_event_management)
        main.add_command(v1_3_3_file)
        main.add_command(v1_3_3_issues)
        main.add_command(v1_3_3_network_settings)
        main.add_command(v1_3_3_path_trace)
        main.add_command(v1_3_3_sda)
        main.add_command(v1_3_3_site_design)
        main.add_command(v1_3_3_sites)
        main.add_command(v1_3_3_software_image_management_swim)
        main.add_command(v1_3_3_tag)
        main.add_command(v1_3_3_task)
        main.add_command(v1_3_3_topology)
        main.add_command(v1_3_3_users)
        main.add_command(v1_3_3_wireless)
    if value == '2.1.1':
        main.add_command(v2_1_1_application_policy)
        main.add_command(v2_1_1_clients)
        main.add_command(v2_1_1_command_runner)
        main.add_command(v2_1_1_configuration_templates)
        main.add_command(v2_1_1_device_onboarding_pnp)
        main.add_command(v2_1_1_device_replacement)
        main.add_command(v2_1_1_devices)
        main.add_command(v2_1_1_discovery)
        main.add_command(v2_1_1_event_management)
        main.add_command(v2_1_1_file)
        main.add_command(v2_1_1_itsm)
        main.add_command(v2_1_1_issues)
        main.add_command(v2_1_1_network_settings)
        main.add_command(v2_1_1_path_trace)
        main.add_command(v2_1_1_sda)
        main.add_command(v2_1_1_site_design)
        main.add_command(v2_1_1_sites)
        main.add_command(v2_1_1_software_image_management_swim)
        main.add_command(v2_1_1_tag)
        main.add_command(v2_1_1_task)
        main.add_command(v2_1_1_topology)
        main.add_command(v2_1_1_users)
        main.add_command(v2_1_1_wireless)
    return value


@click.group()
@click.option('--dna-version', '-v', 'version', type=str,
              default=DNA_CENTER_VERSION,
              help='Controls which version of DNA_CENTER to use.',
              show_default=True,
              callback=version_set,
              is_eager=True)
@click.option('--username', '-u',
              default=DNA_CENTER_USERNAME,
              help='HTTP Basic Auth username.',
              show_default=True)
@click.option('--password', '-p',
              default=DNA_CENTER_PASSWORD,
              help='HTTP Basic Auth password.',
              show_default=True)
@click.option('--encoded_auth', '-ea', type=str,
              default=DNA_CENTER_ENCODED_AUTH,
              help='HTTP Basic Auth base64 encoded string.',
              show_default=True)
@click.option('--base_url', type=str,
              default=DNA_CENTER_BASE_URL,
              help='The base URL to be prefixed to the individual API endpoint suffixes.',
              show_default=True)
@click.option('--single_request_timeout', type=int,
              default=DNA_CENTER_SINGLE_REQUEST_TIMEOUT,
              help='Timeout (in seconds) for RESTful HTTP requests.',
              show_default=True)
@click.option('--wait_on_rate_limit', type=bool,
              default=DNA_CENTER_WAIT_ON_RATE_LIMIT,
              help='Enables or disables automatic rate-limit handling.',
              show_default=True)
@click.option('--verify', type=bool,
              default=DNA_CENTER_VERIFY,
              help="Controls whether to verify the server's TLS certificate.",
              show_default=True)
@click.option('--debug', '-d', type=bool,
              default=DNA_CENTER_DEBUG,
              help="Controls whether to log information about DNA Center APIs' request and response process.",
              show_default=True)
@click.option('-y/-n', 'prompt', is_flag=True,
              default=False,
              help='''Prompt flag for username and password''')
@click.pass_context
def main(ctx, username, password, encoded_auth, base_url,
         version,
         single_request_timeout,
         wait_on_rate_limit,
         verify,
         debug,
         prompt):
    """DNA Center API wrapper.

    DNACenterAPI wraps all of the individual DNA Center APIs and represents
    them in a simple hierarchical structure.

    """

    if prompt:
        username = click.prompt('Username', default=username, show_default=True)
        password_prompt = 'Password [****]' if password else 'Password'
        password = click.prompt(password_prompt, default=password, show_default=False, hide_input=True, confirmation_prompt='Repeat for confirmation')

    urllib3.disable_warnings()
    spinner = init_spinner(beep=False)
    start_spinner(spinner)
    try:
        ctx.obj = DNACenterAPI(username, password, encoded_auth,
                               base_url=base_url,
                               single_request_timeout=single_request_timeout,
                               wait_on_rate_limit=wait_on_rate_limit,
                               verify=verify,
                               version=version,
                               debug=debug)
        stop_spinner(spinner)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('''Try "dnacentercli --help" for help.''')
        eprint('Error:', e)
        ctx.exit(-1)
