import cyrtranslit
from pynput.keyboard import Key, Controller
import time

class UTILITY:
    def __init__(self):
        pass

    def LANGRusToCyrilik(self, TextRUS):
        TextRUS = str(TextRUS).decode('cp1251')
        TextRUS = unicode(TextRUS).encode('utf-8')
        TextCyrylik = cyrtranslit.to_latin(TextRUS, 'ru')

        return TextCyrylik

    def una_autorefresh(self):
        keyb = Controller()

        keyb.press(Key.alt)
        keyb.press(Key.tab)
        keyb.release(Key.alt)
        keyb.release(Key.tab)

        time.sleep(0.5)
        keyb.press(Key.alt)
        keyb.press('r')
        keyb.release(Key.alt)
        keyb.release('r')
        keyb.press(Key.down)
        keyb.release(Key.down)
        keyb.press(Key.up)
        keyb.release(Key.up)

    def tt(self):
        print('ok')
