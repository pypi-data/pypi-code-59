"""The Amethyst entry point which starts Amethyst and its linked GUI app."""

from typing import TextIO

import click

from amethyst.amy import Amy

try:
    from amethyst.gui_pyqt import QtApp as App
except ImportError:
    from amethyst.gui_pyglet import PygletApp as App


@click.command()
@click.argument('module_name', required=False)
@click.option('-d', '--dmenu', type=click.File(), help='A dmenu-like file, or \'-\' to load from stdin.')
def main(module_name: str, dmenu: TextIO) -> None:
    """Launch a configurable radial menu and execute actions according to what is selected."""

    if not module_name and not dmenu:
        raise click.UsageError('either a MODULE_NAME or a dmenu file (via --dmenu) must be provided.')

    if module_name and dmenu:
        raise click.BadOptionUsage('dmenu', 'MODULE_NAME and --dmenu are not compatible, chose one.')

    amy = Amy(App(), module_name, dmenu)
    amy.start()
