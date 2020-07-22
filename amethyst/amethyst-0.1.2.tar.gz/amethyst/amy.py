"""A module dedicated to the Amy class."""

import logging
import os.path as op
import shutil
from threading import Timer
from typing import Dict
from typing import TextIO

import click

from amethyst import consts
from amethyst.app import App
from amethyst.color_scheme import ColorScheme
from amethyst.config import Config
from amethyst.gem import Gem
from amethyst.input import Key, Input


class Amy:
    """The main Amethyst class used to manage the application."""
    # pylint: disable=too-many-instance-attributes

    def __init__(self, app: App, module_name: str, dmenu: TextIO):
        self.app: App = app
        self.window_width: int = -1
        self.window_height: int = -1
        self.outer_size: int = -1
        self.inner_size: int = -1
        self.current_key_inputs: Dict[Key, Timer] = {}

        logging.basicConfig(filename=consts.LOG_FILE_PATH, level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s: %(message)s')
        logging.info('\n\n=== Starting Amethyst ===\n')

        self.gem: Gem = Gem.from_dmenu(dmenu) if dmenu else Gem.from_module_name(module_name)
        self.config: Config = Config()

        if not op.isdir(consts.USER_MODULES_PATH):
            logging.info('User modules folder does not exist, importing builtin modules...')
            shutil.copytree(consts.MODULES_PATH, consts.USER_MODULES_PATH)

        self.color_scheme: ColorScheme = ColorScheme(self.config.color_scheme)

    def start(self) -> None:
        """Starts the Amethyst application."""

        self.app.load(self)
        self.window_width = self.config.window_size_ratio * min(self.app.screen_width, self.app.screen_height)
        self.window_height = self.window_width
        self.outer_size = self.config.outer_size_ratio * self.window_width
        self.inner_size = self.config.inner_size_ratio * self.outer_size
        self.app.start()

    def on_key_press(self, key: Key) -> None:
        """
        Called by the GUI app when the user hit a key.
        :param key: the code of the key.
        """

        def on_key_press_after_delay(_key: Key):
            """Function triggered when the timer started by on_key_press() ends."""

            input_id = '_'.join([k.name for k in set(self.current_key_inputs)])
            user_input = Input[input_id].value if input_id in Input.__members__ else Input[_key.name].value

            logging.info('input: %s', user_input.name)
            click.echo(user_input.name)
            self.current_key_inputs = {}
            self.app.exit()

        if key == Key.escape:
            logging.info('good bye')
            self.app.exit()
        else:
            for timer in self.current_key_inputs.values():
                timer.cancel()

            self.current_key_inputs[key] = Timer(self.config.key_delay, on_key_press_after_delay, args=[key])
            self.current_key_inputs[key].start()

    def on_draw(self) -> None:
        """Called by the GUI app when the window must be paint."""
        self.app.draw_gem()
