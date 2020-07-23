# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sofcorecognition']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sofcorecognition = entry:main']}

setup_kwargs = {
    'name': 'sofcorecognition',
    'version': '0.1.0',
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
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
