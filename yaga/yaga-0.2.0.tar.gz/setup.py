# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yaga']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['yaga = yaga:cli']}

setup_kwargs = {
    'name': 'yaga',
    'version': '0.2.0',
    'description': 'Yet Another Great Automator',
    'long_description': None,
    'author': 'Joseph Egan',
    'author_email': 'joseph.s.egan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eganjs/yaga',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
