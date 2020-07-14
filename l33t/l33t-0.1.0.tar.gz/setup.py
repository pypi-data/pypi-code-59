# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['l33t']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['l33t = l33t:main']}

setup_kwargs = {
    'name': 'l33t',
    'version': '0.1.0',
    'description': 'leet speak generator',
    'long_description': None,
    'author': 'Sergey M',
    'author_email': 'tz4678@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tz4678/l33t',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
