
import time
import click
from numpy.core.numeric import Infinity
import rasterio
import numpy as np
import pymannkendall as mk
import riomucho
from .trend_calculator import run_trend
from .pearson_calculator import run_pearson
from .inspect_calculator import run_inspect

# np.seterr(all='raise')


@click.group()
def cli():
    pass


@click.command()
@click.option('--out', '-o', 'out_file', required=True)
@click.option('--selector', '-s', required=True)
@click.argument('in_file', required=True)
def trend(out_file, selector, in_file):
    print(out_file, selector, in_file)
    run_trend(in_file, out_file, selector)


@click.command()
@click.option('--out', '-o', 'out_file', required=True)
@click.option('--selector', '-s', required=True)
@click.option('--selector2', '-s2', required=True)
@click.argument('in_file', required=True)
def pearson(out_file, selector, selector2, in_file):
    click.echo('pearson')
    run_pearson(in_file, out_file, selector, selector2)


@click.command()
@click.argument('in_file', required=True)
def inspect(in_file):
    run_inspect(in_file)



@click.command()
@click.argument('in_file', required=True)
def print_func(in_file):
    with rasterio.open(in_file) as src:
        print(src.read())


cli.add_command(trend)
cli.add_command(pearson)
cli.add_command(inspect)
# cli.add_command(scale)
cli.add_command(print_func, "print")

if __name__ == "__main__":
    cli()
