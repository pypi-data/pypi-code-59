# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sway_xkb_switcher']

package_data = \
{'': ['*']}

install_requires = \
['i3ipc>=2.1.1,<3.0.0']

entry_points = \
{'console_scripts': ['sway-xkb-switcher = sway_xkb_switcher.switcher:main']}

setup_kwargs = {
    'name': 'sway-xkb-switcher',
    'version': '0.2.2',
    'description': 'Keyboard layout switcher for sway windows',
    'long_description': 'sway-xkb-switcher\n===============\n\n## Description\n\nThis app records keyboard layout for a sway windows when you leave them.\nAnd when you come back it is restore keyboard layout.\n\nThis project is forked from https://github.com/inn0kenty/i3-xkb-switcher\nand adapted to work with sway window manager.\n\nThis project is under construction yet.\n\n## Install\n\n```bash\n$ pip install sway-xkb-switcher\n```\n\nAlso you can download compiled binary from [release page](https://github.com/nmukhachev/sway-xkb-switcher/releases).\n\n## Usage\n\n```bash\n$ sway-xkb-switcher --input-identifier <identifier>\n```\n\nYou can view a list of actual identifiers by looking at\n\n```bash\n$ swaymsg -t get_inputs | grep identifier\n```\nThe identifier corresponds to that from the input section of your sway config.\n\nTo enable debug mode run with `--debug` key.\n\nBy default it writes logs to stdout. You can specify path by `--log-path` option.\n',
    'author': 'Innokenty Lebedev',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nmukhachev/sway-xkb-switcher',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
