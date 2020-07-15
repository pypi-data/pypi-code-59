# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py2graphql']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py2graphql',
    'version': '0.14.2',
    'description': 'Pythonic GraphQL Client',
    'long_description': None,
    'author': 'Willem Thiart',
    'author_email': 'himself@willemthiart.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
