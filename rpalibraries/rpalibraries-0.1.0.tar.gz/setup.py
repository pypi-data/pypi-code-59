# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpalibraries']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rpalibraries',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Mika Hänninen',
    'author_email': 'mika@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
