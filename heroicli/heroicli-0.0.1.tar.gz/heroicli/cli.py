import click
from pathlib import Path
from . import tags

home = str(Path.home())


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-c",
    "--config",
    default="{}/.heroicli.yaml".format(home),
    help="Location of heroicli.yaml config",
)
@click.option("-t", "--tag", required=True, help="Tag to search")
@click.option("-l", "--limit", default=100000, help="Limit sugestions")
@click.option("-v", "--values", is_flag=True, help="Print values")
@click.option("-j", "--json", is_flag=True, help="Implies -v, prints json results")
def tag_inspection(config, tag, limit, values, json):
    """Find all values for a specific tag"""
    tags.inspect_tag(config, tag, limit, values, json)


@cli.command()
@click.option(
    "-c",
    "--config",
    default="{}/.heroicli.yaml".format(home),
    help="Location of heroicli.yaml config",
)
@click.option("-l", "--limit", default=5000, help="Limit sugestions")
@click.option("-v", "--values", is_flag=True, help="Print values")
@click.option("-j", "--json", is_flag=True, help="Implies -v, prints json results")
def key_inspection(config, limit, values, json):
    tags.key_inspect(config, limit, values, json)


@cli.command()
@click.option(
    "-c",
    "--config",
    default="{}/.heroicli.yaml".format(home),
    help="Location of heroicli.yaml config",
)
@click.option("-l", "--limit", default=5000, help="Limit sugestions")
@click.option(
    "-t",
    "--threshold",
    default=10000,
    help="Threshold to consider a tag high cardinality",
)
def high_cardinality(config, limit, threshold):
    tags.high_cardinality(config, limit, threshold)
