"""A module dedicated to the App abstract class."""


class App:
    """
    An abstract class that must be redefined by GUI-specific classes, such as QtApp or PygletApp.
    """

    def __init__(self):
        self.amy = None
        self.window = None
        self.screen_width = -1
        self.screen_height = -1

    def load(self, amy) -> None:
        """
        Prepare the app: connect the Amethyst class, instantiate the GUI application, etc.
        Separated from start() in order to retrieve GUI-specific values such as screen size.
        :param amy: The Amethyst instance linked to the app.
        """
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
