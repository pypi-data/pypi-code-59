import click
import requests
from . import __version__

BASE_URL = "http://localhost:8080"


@click.command()
@click.version_option(version=__version__)
def main():
    """Interact with the Airflow REST API from your terminal."""
    with requests.get(f"{BASE_URL}/api/experimental/test") as response:
        response.raise_for_status()
        data = response.json()

    click.secho(data)
