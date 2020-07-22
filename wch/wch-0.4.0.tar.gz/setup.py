# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wch']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.3.1,<0.4.0']

entry_points = \
{'console_scripts': ['wch = wch.wch:app']}

setup_kwargs = {
    'name': 'wch',
    'version': '0.4.0',
    'description': 'Runs the provided command on detected file changes.',
    'long_description': '# wch\n\n[![Build Status](https://travis-ci.org/Peter554/wch.svg?branch=master)](https://travis-ci.org/Peter554/wch)\n\n```\npip install wch\n```\n\n```\nwch --help\n```\n\n```\nUsage: wch [OPTIONS] COMMAND\n\n  Runs the provided command on detected file changes.\n\n  example: wch -d src -d tests -i docs "black --check ."\n\nArguments:\n  COMMAND  [required]\n\nOptions:\n  -d, --directory TEXT  [default: .]\n  -i, --ignore TEXT     [default: ]\n  --help                Show this message and exit.\n```\n\n',
    'author': 'Peter',
    'author_email': 'byfield554@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Peter554/wch#readme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
