"""The Amethyst entry point which starts Amethyst and its linked GUI app."""

import logging
from typing import TextIO

import click

from amethyst import consts
from amethyst.amy import Amy
from amethyst.gui_common import GuiLib

if consts.GUI_LIB == GuiLib.pyglet:
    from amethyst.gui_pyglet import PygletApp as App
elif consts.GUI_LIB == GuiLib.qt:
    try:
        from amethyst.gui_pyqt import QtApp as App
    except ImportError:
        from amethyst.gui_pyglet import PygletApp as App


@click.command()
@click.argument('module_name', required=False)
@click.option('-d', '--dmenu', type=click.File(), help='A dmenu-like file, or \'-\' to load from stdin.')
def main(module_name: str, dmenu: TextIO) -> None:
    """Launch a configurable radial menu and execute actions according to what is selected."""

    logging.basicConfig(filename=consts.LOG_FILE_PATH, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('\n\n=== Starting Amethyst ===\n')

    if not module_name and not dmenu:
        raise click.UsageError('either a MODULE_NAME or a dmenu file (via --dmenu) must be provided.')

    if module_name and dmenu:
        raise click.BadOptionUsage('dmenu', 'MODULE_NAME and --dmenu are not compatible, chose one.')

    amy = Amy(App(), module_name, dmenu)
    amy.start()
