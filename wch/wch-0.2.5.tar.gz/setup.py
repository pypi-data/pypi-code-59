# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wch']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['wch = wch.wch:cli_sync']}

setup_kwargs = {
    'name': 'wch',
    'version': '0.2.5',
    'description': 'Runs the provided command on detected file changes.',
    'long_description': '# wch\n\n```\npip install wch\n```\n\n```\nwch --help\n```\n\n```\nusage: wch [options] -- <command>\n\nRuns the provided command on detected file changes.\n\npositional arguments:\n  command\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -d DIRECTORY, --directory DIRECTORY\n                        Directory to watch. Defaults to current working directory.\n  -i IGNORE, --ignore IGNORE\n                        Directory to ignore.\n\nExamples:\n  wch -d src -d tests -- pytest\n  wch -i docs -- black .\n```\n\n',
    'author': 'Peter',
    'author_email': 'byfield554@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Peter554/wch#readme',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
