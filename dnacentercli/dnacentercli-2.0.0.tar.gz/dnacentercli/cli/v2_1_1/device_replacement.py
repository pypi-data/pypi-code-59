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
def device_replacement(ctx, obj):
    """DNA Center Device Replacement API (version: 2.1.1).

    Wraps the DNA Center Device Replacement API and exposes the API as native Python commands.

    """
    ctx.obj = obj.device_replacement


@device_replacement.command()
@click.option('--faultydeviceserialnumber', type=str,
              help='''DeviceReplacementWorkflowDTO's faultyDeviceSerialNumber.''',
              default=None,
              show_default=True)
@click.option('--replacementdeviceserialnumber', type=str,
              help='''DeviceReplacementWorkflowDTO's replacementDeviceSerialNumber.''',
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
def deploy_device_replacement_workflow(obj, pretty_print, beep,
                                       faultydeviceserialnumber,
                                       replacementdeviceserialnumber,
                                       headers,
                                       payload,
                                       active_validation):
    """API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and images.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.deploy_device_replacement_workflow(
            faultyDeviceSerialNumber=faultydeviceserialnumber,
            replacementDeviceSerialNumber=replacementdeviceserialnumber,
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


@device_replacement.command()
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
def unmark_device_for_replacement(obj, pretty_print, beep,
                                  headers,
                                  payload,
                                  active_validation):
    """UnMarks device for replacement.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.unmark_device_for_replacement(
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


@device_replacement.command()
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
def mark_device_for_replacement(obj, pretty_print, beep,
                                headers,
                                payload,
                                active_validation):
    """Marks device for replacement.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.mark_device_for_replacement(
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


@device_replacement.command()
@click.option('--faulty_device_name', type=str,
              help='''Faulty Device Name.''',
              show_default=True)
@click.option('--faulty_device_platform', type=str,
              help='''Faulty Device Platform.''',
              show_default=True)
@click.option('--replacement_device_platform', type=str,
              help='''Replacement Device Platform.''',
              show_default=True)
@click.option('--faulty_device_serial_number', type=str,
              help='''Faulty Device Serial Number.''',
              show_default=True)
@click.option('--replacement_device_serial_number', type=str,
              help='''Replacement Device Serial Number.''',
              show_default=True)
@click.option('--replacement_status', type=str,
              help='''Device Replacement status [READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED].''',
              show_default=True)
@click.option('--family', type=str,
              help='''List of families[Routers, Switches and Hubs, AP].''',
              show_default=True)
@click.option('--sort_by', type=str,
              help='''SortBy this field. SortBy is mandatory when order is used.''',
              show_default=True)
@click.option('--sort_order', type=str,
              help='''Order on displayName[ASC,DESC].''',
              show_default=True)
@click.option('--offset', type=int,
              help='''offset query parameter.''',
              show_default=True)
@click.option('--limit', type=int,
              help='''limit query parameter.''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def return_replacement_devices_with_details(obj, pretty_print, beep,
                                            faulty_device_name,
                                            faulty_device_platform,
                                            replacement_device_platform,
                                            faulty_device_serial_number,
                                            replacement_device_serial_number,
                                            replacement_status,
                                            family,
                                            sort_by,
                                            sort_order,
                                            offset,
                                            limit,
                                            headers):
    """Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement Device Serial Number, Device Replacement status, Product Family.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.return_replacement_devices_with_details(
            faulty_device_name=faulty_device_name,
            faulty_device_platform=faulty_device_platform,
            replacement_device_platform=replacement_device_platform,
            faulty_device_serial_number=faulty_device_serial_number,
            replacement_device_serial_number=replacement_device_serial_number,
            replacement_status=replacement_status,
            family=family,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@device_replacement.command()
@click.option('--replacement_status', type=str,
              help='''Device Replacement status list[READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR].''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def return_replacement_devices_count(obj, pretty_print, beep,
                                     replacement_status,
                                     headers):
    """Get replacement devices count.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.return_replacement_devices_count(
            replacement_status=replacement_status,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)
