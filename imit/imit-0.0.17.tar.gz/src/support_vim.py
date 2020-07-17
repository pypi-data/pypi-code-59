
import sys
import time
import os
from pynput.keyboard import Controller, Key, Listener


kb = Controller()


def Press(key):
    Stop()
    kb.press(key)
    kb.release(key)
    Start()


def on_press(key):
    try:
        if key.char == 'j':
            Press(Key.up)
        elif key.char == 'k':
            Press(Key.down)
    except AttributeError:
        pass


def on_release(key):
    pass


listener = Listener(on_press=on_press, on_release=on_release)


def Start():
    global listener
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()


def Stop():
    global listener
    listener.stop()
