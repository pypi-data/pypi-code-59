"""Define the Amethyst GUI for Pyglet, in particular the PygletApp class."""

import logging

from pyglet import app, window, shapes, canvas

from amethyst.amy import Amy
from amethyst.app import App
from amethyst.gui_common import Key, Geometry

KEYS = {
    window.key.UP: Key.up,
    window.key.RIGHT: Key.right,
    window.key.DOWN: Key.down,
    window.key.LEFT: Key.left,
    window.key.ESCAPE: Key.escape
}


class PygletWindow(window.Window):
    """Pyglet class that represent a window."""

    def __init__(self, amy: Amy):
        super().__init__(width=400, height=400, style=window.Window.WINDOW_STYLE_BORDERLESS)
        self.amy = amy

    def on_draw(self):
        logging.info('Pyglet: Draw event triggered.')
        self.amy.on_draw()

    def on_key_press(self, key, modifier):  # pylint: disable=unused-argument
        logging.info('Pyglet: Key press event triggered.')

        if key in KEYS:
            self.amy.on_key_press(KEYS[key])
        else:
            logging.warning('Pyglet: Not recognised key pressed: %s', key.name)


class PygletApp(App):
    """
    The app class that handles the GUI with Pyglet, inheriting from App class.
    """
    def init(self, amy: Amy) -> None:
        logging.info('Pyglet: Init app.')
        self.window = PygletWindow(amy)

    def get_screen_size(self) -> Geometry:
        screen = canvas.Display().get_default_screen()
        return Geometry(screen.width, screen.height)

    def start(self) -> None:
        logging.info('Pyglet: Opening window.')
        app.run()

    def exit(self) -> None:
        logging.info('Pyglet: exiting app.')
        app.exit()

    def draw_gem(self) -> None:
        logging.info('Pyglet: drawing gem.')
        self.window.clear()
        circle = shapes.Circle(x=200, y=200, radius=200, color=(128, 128, 128))
        circle.draw()
