
import pyperclip


def copy(text):
    pyperclip.copy(text)
    return True


def paste():
    text = pyperclip.paste()
    return text


# alias for copy
def set(text):
    return copy(text)


# alias for paste
def get():
    return paste()

