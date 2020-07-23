import cyrtranslit
import ping, socket
import time

from pynput.keyboard import Key, Controller

def LANGRusToCyrilik(TextRUS):
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


def ping_addr(hostname):
    msg_except = None
    try:
        ip_res = ping.do_one(hostname, timeout=2, psize=3)
        if ip_res == None:
            res = 1
        else:
            res = 0
        return res, msg_except
    except socket.error, e:
        print("Ping error:", e)
        msg_except = "Ping error:" + str(e)
        return -1, msg_except
