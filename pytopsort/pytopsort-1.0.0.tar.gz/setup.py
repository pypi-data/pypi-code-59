# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytopsort']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pytopsort',
    'version': '1.0.0',
    'description': 'Python implementation of topological sort',
    'long_description': None,
    'author': 'Pavel Kulyov',
    'author_email': 'kulyov.pavel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
