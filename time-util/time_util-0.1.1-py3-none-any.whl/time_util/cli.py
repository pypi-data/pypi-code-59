
import click
from datetime import datetime


@click.group()
def cli():
    pass


@cli.command()
@click.option('--utc', is_flag=True)
def now(utc):

    if utc:
        now = datetime.utcnow()
    else:
        now = datetime.now()

    formatted = now.replace(microsecond=0).isoformat()
    print(formatted)


