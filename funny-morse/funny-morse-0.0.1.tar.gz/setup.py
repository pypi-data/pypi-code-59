# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funny_morse']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.7',
 'pynput>=1.6',
 'rshell>=0.0.20',
 'sounddevice>=0.3',
 'wavio>=0.0.1']

setup_kwargs = {
    'name': 'funny-morse',
    'version': '0.0.1',
    'description': 'Converts text to morse code signals [audio, window, keyboardleds, led, servo]',
    'long_description': '# Funny Morse\n\nConverts text to morse code signals\n\n## Examples\n\n```python3\nfrom funny_morse import *\n\nprint(code("Morse code")) # -- --- .-. ... .   -.-. --- -.. .\n```\n\n### Audio\n```python3\naudio("play") # To play morse code audio signal for message\n\naudio_file("code.wav", "wave file", sps=44100, freq=800) # To save\n```\n\n### Window\n```python3\nwindow("show", wpm=5, fs=None)\n```\n\n### Keyboard Leds\n```python3\ncaps_lock("morse")\n\nnum_lock("on")\n\nscroll_lock("indicator")\n```\n\n### Pyboard\n```python3\nled("blink", device="/dev/ttyUSB0")\n\nservo("tap", device="192.168.1.1")\n```\n\n### Parallel\n```python3\nParallel("try parallel",\n         modes=[\n            play,        # can use callables\n            "window"     # can use modes\n         ],\n         led={\n            "pin" : 2,   # kwargs to led mode\n         }\n         ).join()\n```\n\n## CLI Examples\n```\nusage: funny_morse [-h] [--wpm WPM] [--fs FS] [-i] [-p] [-a FILENAME] [-w] [-c] [-n] [-s] [-l] [-m] [-P [MODES [MODES ...]]] [message [message ...]]\n\nConvert text to morse code signals ;)\n\npositional arguments:\n  message               Text to translate or blank to take from stdin\n\noptional arguments:\n  -h, --help                                              show this help message and exit\n  --wpm WPM                                               Words per minute\n  --fs FS                                                 Farnsworth speed\n  -i                                                      For interactive convertion\n  -p, --play                                              To play audio signal\n  -a FILENAME, --audio FILENAME                           To save audio signal\n  -w, --window                                            To show on a window\n  -c, --capsL                                             To show on caps lock indicator\n  -n, --numL                                              To show on num lock indicator\n  -s, --scrollL                                           To show on scroll lock indicator\n  -l, --led                                               To show on LED (required Microcontroller with MicroPython)\n  -m, --servo                                             To tap using servo motor (required Microcontroller with MicroPython)\n  -P [MODES [MODES ...]], --parallel [MODES [MODES ...]]  For parallel modes\n```\n\n```bash\npython -m funny_morse --wpm 15 --fs 15 -p hello\n```\n> ```\n> Dot width           = 80.0 ms\n> Dash width          = 240 ms\n> Character space     = 240 ms\n> Word space          = 560 ms\n> Audio :\n>  samples per second = 8000\n>  Tone period        = 1.3 ms\n> .... . .-.. .-.. ---\n> ```\n\n### Parallel\n```bash\npython -m funny_morse -P p w -- now parallelly play audio and show window\n```\n\n\n## Installation\n\nInstallation is available via pip:\n\n```bash\npip install funny-morse # From PYPI\n\n## OR ##\n\npip install git+https://github.com/nkpro2000sr/funny-morse.git # From github repo\n```\n\n## Links\n* [PyPi](https://pypi.org/project/funny-morse/)\n',
    'author': 'Naveen S R',
    'author_email': 'srnaveen2k@yahoo.com',
    'maintainer': 'Naveen S R',
    'maintainer_email': 'srnaveen2k@yahoo.com',
    'url': 'https://github.com/nkpro2000sr/funny-morse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
