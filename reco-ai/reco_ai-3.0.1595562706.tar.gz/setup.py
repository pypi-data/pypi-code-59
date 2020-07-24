# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reco_ai']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['reco_ai = reco_ai.script:main']}

setup_kwargs = {
    'name': 'reco-ai',
    'version': '3.0.1595562706',
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
