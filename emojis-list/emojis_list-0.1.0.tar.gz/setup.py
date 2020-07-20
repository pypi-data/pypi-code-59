# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emojis_list']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'emojis-list',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Lorenzo',
    'author_email': 'lorenzo@coacci.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
