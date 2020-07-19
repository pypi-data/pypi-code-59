# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wch']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['wch = wch.wch:cli']}

setup_kwargs = {
    'name': 'wch',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Peter',
    'author_email': 'byfield554@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
