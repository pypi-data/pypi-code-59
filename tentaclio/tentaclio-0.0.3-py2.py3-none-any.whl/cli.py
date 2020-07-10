"""Helper cli to encode urls."""
import typing

import click

from tentaclio import urls


# CLI main entry point


@click.group()
def main():
    """Group the click commands."""
    pass


# Register CLI commands


@main.command()
@click.option("--scheme", default=None, required=True)
@click.option("--username", default=None)
@click.option("--password", default=None)
@click.option("--hostname", default=None)
@click.option("--port", default=None, type=int)
@click.option("--path", default=None)
@click.option(
    "--key",
    default=None,
    nargs=2,
    multiple=True,
    help="Provide key-value pairs using [--key KEY VALUE]",
)
def compose_url(scheme, username, password, hostname, port, path, key):
    """Compose a client URL from individual components."""
    if not hostname and not path:
        raise click.ClickException("Provide at least one of `hostname`, `path`")

    query: typing.Optional[dict] = None
    if key:
        query = {k: v for k, v in key}

    composed_url = urls.URL.from_components(
        scheme=scheme,
        username=username,
        password=password,
        hostname=hostname,
        port=port,
        path=path,
        query=query,
    )

    # Output composed url (with no hidden secrets)
    click.echo(composed_url.url, nl=False)
