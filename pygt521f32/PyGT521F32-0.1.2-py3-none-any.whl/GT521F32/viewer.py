import sys
import time
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage

import PIL
import PIL.Image

import GT521F32


class ViewerThread(QThread):
    set_image = pyqtSignal(QImage)

    def __init__(self, parent, reader):
        super().__init__(parent)
        self._reader = reader

    def run(self):
        with self._reader.led():
            while True:
                self._reader.capture()
                data = self._reader.get_image()
                img = QImage(data, 202, 258, QImage.Format_RGB888)
                self.set_image.emit(img)
                time.sleep(0.5)
                return


class Viewer(QWidget):
    def __init__(self, reader):
        super().__init__()
        self._reader = reader
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GT521F32")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._thread = ViewerThread(self, self._reader)
        self._thread.set_image.connect(self.set_image)

        self.label = QLabel(self)
        self.resize(202, 258)
        self._thread.start()
        self.show()

    @pyqtSlot(QImage)
    def set_image(self, img):
        print("yooo")
        self.label.setPixmap(QPixmap.fromImage(img))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Viewer(GT521F32.GT521F32("/dev/sg2"))
    ex.show()
    sys.exit(app.exec_())
