# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adit',
 'adit.config',
 'adit.controllers',
 'adit.dashboard',
 'adit.dashboard.cache',
 'adit.dashboard.models',
 'adit.ingestors',
 'adit.ingestors.crawlers',
 'adit.ingestors.receivers',
 'adit.processor',
 'adit.utils']

package_data = \
{'': ['*'], 'adit.dashboard': ['static/images/*', 'templates/*', 'themes/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'dask[complete]>=2.17.2,<3.0.0',
 'distributed>=2.18.0,<3.0.0',
 'fxcmpy>=1.2.6,<2.0.0',
 'hurst>=0.0.5,<0.0.6',
 'pandas>=1.0.4,<2.0.0',
 'python-socketio>=4.6.0,<5.0.0',
 'requests>=2.24.0,<3.0.0',
 'scipy>=1.5.1,<2.0.0',
 'tiledb>=0.6.5,<0.7.0',
 'tqdm>=4.46.1,<5.0.0']

setup_kwargs = {
    'name': 'adit',
    'version': '0.1.3',
    'description': 'Adit is a toolbox that helps people collaborating on machine learning prototype easier.',
    'long_description': None,
    'author': 'Trinh Tran',
    'author_email': 'trinhtran2151995@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
