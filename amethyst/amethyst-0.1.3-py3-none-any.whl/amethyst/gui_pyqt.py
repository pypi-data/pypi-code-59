"""Define the Amethyst GUI for PyQt, in particular the QtApp class."""

import logging
import sys
from os import environ

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QBrush, QPainterPath, QColor
from PyQt5.QtWidgets import QApplication, QDialog

from amethyst.amy import Amy
from amethyst.app import App
from amethyst.gui_common import Key, Geometry

KEYS = {
    Qt.Key_Up: Key.up,
    Qt.Key_Right: Key.right,
    Qt.Key_Down: Key.down,
    Qt.Key_Left: Key.left,
    Qt.Key_Escape: Key.escape
}


class QtWindow(QDialog):
    """Qt class that represents a window."""

    def __init__(self, amy: Amy):
        super().__init__(flags=Qt.Dialog)
        self.amy = amy

        self.setModal(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):  # pylint: disable=invalid-name, unused-argument
        """Qt method triggered when then window is drawn."""

        logging.info('PyQt: Draw event triggered.')
        self.amy.on_draw()

    def keyPressEvent(self, event):  # pylint: disable=invalid-name
        """Qt method triggered when a key press event occurs."""

        logging.info('PyQt: Key press event triggered.')
        if event.key() in KEYS:
            self.amy.on_key_press(KEYS[event.key()])
        else:
            logging.warning('PyQt: Not recognised key pressed: %s', event.key().name)


class QtApp(App):
    """
    The app class that handles the GUI with PyQt, inheriting from App class.
    """

    def __init__(self):
        super().__init__()
        self.app = None

    def init(self, amy: Amy) -> None:
        logging.info('PyQt: Init app.')
        self.amy = amy

        environ['QT_QPA_PLATFORM'] = 'xcb'  # see https://bugreports.qt.io/browse/QTBUG-80702
        self.app = QApplication([])

    def get_screen_size(self) -> Geometry:
        screen_size = self.app.desktop().screenGeometry()
        logging.info('PyQt: Screen size: %dx%d.', screen_size.width(), screen_size.height())
        return Geometry(screen_size.width(), screen_size.height())

    def start(self) -> None:
        logging.info('PyQt: Opening window.')
        self.window = QtWindow(self.amy)
        self.window.setMinimumWidth(self.amy.window_size.width)
        self.window.setMinimumHeight(self.amy.window_size.height)
        self.window.setMaximumWidth(self.amy.window_size.width)
        self.window.setMaximumHeight(self.amy.window_size.height)
        self.window.show()

        sys.exit(self.app.exec_())

    def exit(self) -> None:
        logging.info('PyQt: exiting app.')
        self.window.close()

    def draw_gem(self) -> None:
        logging.info('PyQt: drawing gem.')
        width = self.amy.window_size.width
        d_out = self.amy.gem_config.outer_size
        d_in = self.amy.gem_config.inner_size
        nb_faces = self.amy.gem.type.value
        angle = 360 / nb_faces

        outer_bg = QRectF(width / 2 - d_out / 2, width / 2 - d_out / 2, d_out, d_out)
        inner_bg = QRectF(width / 2 - d_in / 2, width / 2 - d_in / 2, d_in, d_in)

        qpath = QPainterPath()
        for i_face in range(0, nb_faces):
            qpath.arcMoveTo(outer_bg, i_face * angle + 0.5 * angle)
            qpath.arcTo(outer_bg, i_face * angle + 0.5 * angle, angle)
            qpath.arcTo(inner_bg, i_face * angle + 0.5 * angle + angle, -angle)
            qpath.closeSubpath()

        painter = QPainter(self.window)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(self.amy.color_scheme.background_main), Qt.SolidPattern))
        painter.drawPath(qpath)
