# -*- coding: utf-8 -*-
import click
import json
from ..utils.spinner import (
    init_spinner,
    start_spinner,
    stop_spinner,
)
from ..utils.print import (
    tbprint,
    eprint,
    oprint,
    opprint,
)


@click.group()
@click.pass_obj
@click.pass_context
def site_design(ctx, obj):
    """DNA Center Site Design API (version: 2.1.1).

    Wraps the DNA Center Site Design API and exposes the API as native Python commands.

    """
    ctx.obj = obj.site_design


@site_design.command()
@click.option('--offset', type=str,
              help='''offset/starting row.''',
              show_default=True)
@click.option('--limit', type=str,
              help='''Number of profile to be retrieved.''',
              show_default=True)
@click.option('--name', type=str,
              help='''Name of network profile to be retrieved.''',
              show_default=True)
@click.option('--id', type=str,
              help='''ID of network profile to retrieve.''',
              required=True,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_nfv_profile(obj, pretty_print, beep,
                    offset,
                    limit,
                    name,
                    id,
                    headers):
    """API to get NFV network profile.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_nfv_profile(
            offset=offset,
            limit=limit,
            name=name,
            id=id,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--device', type=str, multiple=True,
              help='''Device, property of the request body (list of objects).''',
              default=None,
              show_default=True)
@click.option('--name', type=str,
              help='''Name of the profile to be updated.''',
              show_default=True)
@click.option('--id', type=str,
              help='''Id of the NFV profile to be updated.''',
              required=True,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('--payload', type=str, help='''A JSON serializable Python object to send in the body of the Request.''',
              default=None,
              show_default=True)
@click.option('--active_validation', type=bool, help='''Enable/Disable payload validation.''',
              default=True,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def update_nfv_profile(obj, pretty_print, beep,
                       device,
                       name,
                       id,
                       headers,
                       payload,
                       active_validation):
    """API to update a NFV Network profile.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        device = list(device)
        device = json.loads('[{}]'.format(', '.join('{0}'.format(w) for w in device)))
        device = device if len(device) > 0 else None
        result = obj.update_nfv_profile(
            device=device,
            name=name,
            id=id,
            headers=headers,
            payload=payload,
            active_validation=active_validation)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--device_ip', type=str,
              help='''Device Ip, property of the request body.''',
              default=None,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('--payload', type=str, help='''A JSON serializable Python object to send in the body of the Request.''',
              default=None,
              show_default=True)
@click.option('--active_validation', type=bool, help='''Enable/Disable payload validation.''',
              default=True,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def nfv_provisioning_detail(obj, pretty_print, beep,
                            device_ip,
                            headers,
                            payload,
                            active_validation):
    """Checks the provisioning detail of an ENCS device including log information.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.nfv_provisioning_detail(
            device_ip=device_ip,
            headers=headers,
            payload=payload,
            active_validation=active_validation)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--name', type=str,
              help='''Nameof nfv network profile to delete. .''',
              show_default=True)
@click.option('--id', type=str,
              help='''Id of nfv network profile to delete. .''',
              required=True,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def delete_nfv_profile(obj, pretty_print, beep,
                       name,
                       id,
                       headers):
    """API to delete nfv network profile.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.delete_nfv_profile(
            name=name,
            id=id,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--device', type=str, multiple=True,
              help='''Device, property of the request body (list of objects).''',
              default=None,
              show_default=True)
@click.option('--profilename', type=str,
              help='''Site Profile Name, property of the request body.''',
              default=None,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('--payload', type=str, help='''A JSON serializable Python object to send in the body of the Request.''',
              default=None,
              show_default=True)
@click.option('--active_validation', type=bool, help='''Enable/Disable payload validation.''',
              default=True,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def create_nfv_profile(obj, pretty_print, beep,
                       device,
                       profilename,
                       headers,
                       payload,
                       active_validation):
    """API to create network profile for different NFV topologies.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        device = list(device)
        device = json.loads('[{}]'.format(', '.join('{0}'.format(w) for w in device)))
        device = device if len(device) > 0 else None
        result = obj.create_nfv_profile(
            device=device,
            profileName=profilename,
            headers=headers,
            payload=payload,
            active_validation=active_validation)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--provisioning', type=str, multiple=True,
              help='''Provisioning, property of the request body (list of objects).''',
              default=None,
              show_default=True)
@click.option('--siteprofile', type=str, multiple=True,
              help='''Site Profile, property of the request body (list of objects).''',
              default=None,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('--payload', type=str, help='''A JSON serializable Python object to send in the body of the Request.''',
              default=None,
              show_default=True)
@click.option('--active_validation', type=bool, help='''Enable/Disable payload validation.''',
              default=True,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def provision_nfv(obj, pretty_print, beep,
                  provisioning,
                  siteprofile,
                  headers,
                  payload,
                  active_validation):
    """Design and Provision single/multi NFV device with given site/area/building/floor .
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        provisioning = list(provisioning)
        provisioning = json.loads('[{}]'.format(', '.join('{0}'.format(w) for w in provisioning)))
        provisioning = provisioning if len(provisioning) > 0 else None
        siteprofile = list(siteprofile)
        siteprofile = json.loads('[{}]'.format(', '.join('{0}'.format(w) for w in siteprofile)))
        siteprofile = siteprofile if len(siteprofile) > 0 else None
        result = obj.provision_nfv(
            provisioning=provisioning,
            siteProfile=siteprofile,
            headers=headers,
            payload=payload,
            active_validation=active_validation)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@site_design.command()
@click.option('--device_ip', type=str,
              help='''Device to which the provisioning detail has to be retrieved.''',
              required=True,
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_device_details_by_ip(obj, pretty_print, beep,
                             device_ip,
                             headers):
    """Returns provisioning device information for the specified IP address.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_device_details_by_ip(
            device_ip=device_ip,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)
