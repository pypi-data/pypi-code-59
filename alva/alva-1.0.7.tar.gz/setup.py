# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alva']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['teslax = entry:main']}

setup_kwargs = {
    'name': 'alva',
    'version': '1.0.7',
    'description': '',
    'long_description': None,
    'author': 'Deniansyah',
    'author_email': '5lineofcode@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
