# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybreakout']

package_data = \
{'': ['*'], 'pybreakout': ['assets/font/*', 'assets/sfx/*']}

install_requires = \
['pygame==2.0.0.dev10']

entry_points = \
{'console_scripts': ['pybreakout = pybreakout.game:main']}

setup_kwargs = {
    'name': 'pybreakout',
    'version': '0.1.0',
    'description': 'Yet another breakout game written in Python',
    'long_description': 'PyBREAKOUT\n==========\n\nYet another Breakout game written in Python.\n\n.. image:: https://raw.githubusercontent.com/julianolf/pybreakout/master/screenshot.png\n    :width: 640px\n    :alt: game play screenshot\n\nRequirements\n------------\n\n* Python >= 3.7, < 3.8\n\nInstalling\n----------\n\nUse ``pip`` to download and install the game. ::\n\n    $ pip install pybreakout\n\nRunning\n-------\n\nJust type ``pybreakout`` to run the game. ::\n\n    $ pybreakout\n\nControls\n--------\n\nUse the arrow keys to control the paddle.\n',
    'author': 'Juliano Fernandes',
    'author_email': 'julianofernandes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/julianolf/pybreakout',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
