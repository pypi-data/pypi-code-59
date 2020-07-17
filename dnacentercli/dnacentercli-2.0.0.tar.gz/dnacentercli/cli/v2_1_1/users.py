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
def users(ctx, obj):
    """DNA Center Users API (version: 2.1.1).

    Wraps the DNA Center Users API and exposes the API as native Python commands.

    """
    ctx.obj = obj.users


@users.command()
@click.option('--headers', type=str, help='''Dictionary of HTTP Headers to send with the Request.''',
              default=None,
              show_default=True)
@click.option('-pp', '--pretty_print', type=int, help='''Pretty print indent''',
              default=None,
              show_default=True)
@click.option('--beep', is_flag=True, help='''Spinner beep (on)''')
@click.pass_obj
def get_user_enrichment_details(obj, pretty_print, beep,
                                headers):
    """Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user and devices that the user is connected to.
    """
    spinner = init_spinner(beep=beep)
    start_spinner(spinner)
    try:
        if headers is not None:
            headers = json.loads(headers)
        result = obj.get_user_enrichment_details(
            headers=headers)
        stop_spinner(spinner)
        opprint(result, indent=pretty_print)
    except Exception as e:
        stop_spinner(spinner)
        tbprint()
        eprint('Error:', e)
        click.Context.exit(-1)
