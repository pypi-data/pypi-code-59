# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sofconizer']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sofconizer = main:main']}

setup_kwargs = {
    'name': 'sofconizer',
    'version': '1.0.1595557815',
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
