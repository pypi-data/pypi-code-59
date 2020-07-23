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
from amethyst.gem import Gem, GemConfig
from amethyst.gui_common import Key, Geometry
from amethyst.input import Input


class Amy:
    """The main Amethyst class used to manage the application."""

    def __init__(self, app: App, module_name: str, dmenu: TextIO):
        logging.info('Instantiating Amy...')

        self.app: App = app
        self.window_size: Geometry = Geometry()
        self.gem_config = GemConfig()
        self.current_key_inputs: Dict[Key, Timer] = {}

        self.gem: Gem = Gem.from_dmenu(dmenu) if dmenu else Gem.from_module_name(module_name)
        self.conf: Config = Config()

        if not op.isdir(consts.USER_MODULES_PATH):
            logging.info('User modules folder does not exist, importing builtin modules...')
            shutil.copytree(consts.MODULES_PATH, consts.USER_MODULES_PATH)

        self.color_scheme: ColorScheme = ColorScheme.from_name(self.conf.color_scheme)

    def start(self) -> None:
        """Starts the Amethyst application."""

        self.app.init(self)
        screen_size = self.app.get_screen_size()
        win_width = int(self.conf.window_size_ratio * min(screen_size.width, screen_size.height))
        self.window_size = Geometry(win_width, win_width)
        self.gem_config = GemConfig(outer_size=int(self.conf.outer_size_ratio * win_width),
                                    inner_size=int(self.conf.inner_size_ratio * self.conf.outer_size_ratio * win_width))
        logging.info('Starting app ...')
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

            logging.info('Key timer ended. Input: %s', user_input.name)
            click.echo(user_input.name)
            self.current_key_inputs = {}
            self.app.exit()

        if key == Key.escape:
            logging.info('good bye')
            self.app.exit()
        else:
            for time_key, timer in self.current_key_inputs.items():
                logging.info('Cancelling timer for key %s.', time_key.name)
                timer.cancel()

            self.current_key_inputs[key] = Timer(self.conf.key_delay, on_key_press_after_delay, args=[key])
            self.current_key_inputs[key].start()

    def on_draw(self) -> None:
        """Called by the GUI app when the window must be paint."""

        self.app.draw_gem()
