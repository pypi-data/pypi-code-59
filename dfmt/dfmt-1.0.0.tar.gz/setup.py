# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfmt']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dfmt = dfmt:main']}

setup_kwargs = {
    'name': 'dfmt',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Dimitri Merejkowsky',
    'author_email': 'd.merej@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
