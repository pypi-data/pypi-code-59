"""A module dedicated to the App abstract class."""

from amethyst.gui_common import Geometry


class App:
    """
    An abstract class that must be redefined by GUI-specific classes, such as QtApp or PygletApp.
    """

    def __init__(self):
        self.amy = None
        self.window = None

    def init(self, amy) -> None:
        """
        Prepare the app: connect the Amethyst class, instantiate the GUI application, etc.
        Separated from start() in order to retrieve GUI-specific values such as screen size.
        :param amy: The Amethyst instance linked to the app.
        """
        raise NotImplementedError('abstract method')

    def get_screen_size(self) -> Geometry:
        """Returns the screen size."""

        raise NotImplementedError('abstract method')

    def start(self) -> None:
        """
        Create the window and starts the app.
        """
        raise NotImplementedError('abstract method')

    def exit(self) -> None:
        """
        Exit the app.
        """
        raise NotImplementedError('abstract method')

    def draw_gem(self) -> None:
        """
        Draw the gem to the window.
        """
        raise NotImplementedError('abstract method')
