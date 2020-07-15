import click
import json
import asyncio
from .loader import load_node, load_input, load_output
from .entrypoint import run_node


@click.group()
def execute_cli():
    """
    The base of the grappl cli.
    """
    pass


@execute_cli.group()
def config():
    """
    Only print the loaded configuration.
    """
    pass


@execute_cli.group()
def run():
    """
    Run the actual grappl node.
    """
    pass


@execute_cli.group()
def load():
    """
    Load the defined node and input and output according to the specified configuration, 
    and open a shell for playing around.
    """
    pass


@config.resultcallback()
def process_config(result):
    click.echo(json.dumps(result))


@run.resultcallback()
def process_run(result):
    node = load_node(result)
    node_input = load_input(result)
    node_output = load_output(result)
    asyncio.run(run_node(node, node_input, node_output))


@load.resultcallback()
def process_load(result):
    node = load_node(result)
    input = load_input(result)
    output = load_output(result)
    import ipdb
    ipdb.set_trace()
