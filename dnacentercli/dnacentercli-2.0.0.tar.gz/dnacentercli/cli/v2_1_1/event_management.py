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
def event_management(ctx, obj):
    """DNA Center Event Management API (version: 2.1.1).

    Wraps the DNA Center Event Management API and exposes the API as native Python commands.

    """
    ctx.obj = obj.event_management


@event_management.command()
@click.option('--event_ids', type=str,
              help='''List of subscriptions related to the respective eventIds.''',
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
def count_of_event_subscriptions(obj, pretty_print, beep,
                                 event_ids,
                                 headers):
    """Returns the Count of EventSubscriptions.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.count_of_event_subscriptions(
            event_ids=event_ids,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
@click.option('--event_id', type=str,
              help='''The registered EventId should be provided.''',
              show_default=True)
@click.option('--tags', type=str,
              help='''The registered Tags should be provided.''',
              required=True,
              show_default=True)
@click.option('--offset', type=int,
              help='''The number of Registries to offset in the resultset whose default value 0.''',
              show_default=True)
@click.option('--limit', type=int,
              help='''The number of Registries to limit in the resultset whose default value 10.''',
              show_default=True)
@click.option('--sort_by', type=str,
              help='''SortBy field name.''',
              show_default=True)
@click.option('--order', type=str,
              help='''order query parameter.''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_events(obj, pretty_print, beep,
               event_id,
               tags,
               offset,
               limit,
               sort_by,
               order,
               headers):
    """Gets the list of registered Events with provided eventIds or tags as mandatory.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_events(
            event_id=event_id,
            tags=tags,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            order=order,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
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
def update_event_subscriptions(obj, pretty_print, beep,
                               headers,
                               payload,
                               active_validation):
    """Update SubscriptionEndpoint to list of registered events.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.update_event_subscriptions(
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


@event_management.command()
@click.option('--event_id', type=str,
              help='''The registered EventId should be provided.''',
              show_default=True)
@click.option('--tags', type=str,
              help='''The registered Tags should be provided.''',
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
def count_of_events(obj, pretty_print, beep,
                    event_id,
                    tags,
                    headers):
    """Get the count of registered events with provided eventIds or tags as mandatory.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.count_of_events(
            event_id=event_id,
            tags=tags,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
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
def create_event_subscriptions(obj, pretty_print, beep,
                               headers,
                               payload,
                               active_validation):
    """Subscribe SubscriptionEndpoint to list of registered events.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        if payload is not None:
            payload = json.loads(payload)
        result = obj.create_event_subscriptions(
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


@event_management.command()
@click.option('--subscriptions', type=str,
              help='''List of EventSubscriptionId's for removal.''',
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
def delete_event_subscriptions(obj, pretty_print, beep,
                               subscriptions,
                               headers):
    """Delete EventSubscriptions.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.delete_event_subscriptions(
            subscriptions=subscriptions,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
@click.option('--event_ids', type=str,
              help='''The registered EventIds should be provided.''',
              show_default=True)
@click.option('--start_time', type=str,
              help='''StartTime .''',
              show_default=True)
@click.option('--end_time', type=str,
              help='''endTime .''',
              show_default=True)
@click.option('--category', type=str,
              help='''category .''',
              show_default=True)
@click.option('--type', type=str,
              help='''type .''',
              show_default=True)
@click.option('--severity', type=str,
              help='''severity .''',
              show_default=True)
@click.option('--domain', type=str,
              help='''domain .''',
              show_default=True)
@click.option('--sub_domain', type=str,
              help='''subDomain .''',
              show_default=True)
@click.option('--source', type=str,
              help='''source .''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def count_of_notifications(obj, pretty_print, beep,
                           event_ids,
                           start_time,
                           end_time,
                           category,
                           type,
                           severity,
                           domain,
                           sub_domain,
                           source,
                           headers):
    """Get the Count of Published Notifications.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.count_of_notifications(
            event_ids=event_ids,
            start_time=start_time,
            end_time=end_time,
            category=category,
            type=type,
            severity=severity,
            domain=domain,
            sub_domain=sub_domain,
            source=source,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
@click.option('--event_ids', type=str,
              help='''List of subscriptions related to the respective eventIds.''',
              show_default=True)
@click.option('--offset', type=int,
              help='''The number of Subscriptions's to offset in the resultset whose default value 0.''',
              show_default=True)
@click.option('--limit', type=int,
              help='''The number of Subscriptions's to limit in the resultset whose default value 10.''',
              show_default=True)
@click.option('--sort_by', type=str,
              help='''SortBy field name.''',
              show_default=True)
@click.option('--order', type=str,
              help='''order query parameter.''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_event_subscriptions(obj, pretty_print, beep,
                            event_ids,
                            offset,
                            limit,
                            sort_by,
                            order,
                            headers):
    """Gets the list of Subscriptions's based on provided offset and limit.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_event_subscriptions(
            event_ids=event_ids,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            order=order,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
@click.option('--execution_id', type=str,
              help='''Execution ID.''',
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
def get_status_api_for_events(obj, pretty_print, beep,
                              execution_id,
                              headers):
    """Get the Status of events API calls with provided executionId as mandatory path parameter.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_status_api_for_events(
            execution_id=execution_id,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)


@event_management.command()
@click.option('--event_ids', type=str,
              help='''The registered EventIds should be provided.''',
              show_default=True)
@click.option('--start_time', type=str,
              help='''StartTime .''',
              show_default=True)
@click.option('--end_time', type=str,
              help='''endTime .''',
              show_default=True)
@click.option('--category', type=str,
              help='''category .''',
              show_default=True)
@click.option('--type', type=str,
              help='''type .''',
              show_default=True)
@click.option('--severity', type=str,
              help='''severity .''',
              show_default=True)
@click.option('--domain', type=str,
              help='''domain .''',
              show_default=True)
@click.option('--sub_domain', type=str,
              help='''subDomain .''',
              show_default=True)
@click.option('--source', type=str,
              help='''source .''',
              show_default=True)
@click.option('--offset', type=int,
              help='''Offset whose default value 0.''',
              show_default=True)
@click.option('--limit', type=int,
              help='''Limit whose default value 10.''',
              show_default=True)
@click.option('--sort_by', type=str,
              help='''SortBy field name.''',
              show_default=True)
@click.option('--order', type=str,
              help='''order query parameter.''',
              show_default=True)
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_notifications(obj, pretty_print, beep,
                      event_ids,
                      start_time,
                      end_time,
                      category,
                      type,
                      severity,
                      domain,
                      sub_domain,
                      source,
                      offset,
                      limit,
                      sort_by,
                      order,
                      headers):
    """Get the list of Published Notifications.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_notifications(
            event_ids=event_ids,
            start_time=start_time,
            end_time=end_time,
            category=category,
            type=type,
            severity=severity,
            domain=domain,
            sub_domain=sub_domain,
            source=source,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            order=order,
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)
