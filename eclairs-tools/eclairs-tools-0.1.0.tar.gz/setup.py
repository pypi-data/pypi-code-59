# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eclairs_tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'eclairs-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'John Doe',
    'author_email': 'john-doe@example.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=666,<667',
}


setup(**setup_kwargs)
