import asyncio  # pytype: disable=pyi-error

import click

from ..utils import handle_credentials

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.command(context_settings=CONTEXT_SETTINGS)
def login():
    """ Configure your Coiled account credentials
    """
    asyncio.run(handle_credentials(save=True))
    print(
        '\nNext: see the "Run your first computation" guide at ... \n'
        "https://coiled.io/cloud/getting_started.html#run-your-first-computation"
    )
