# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cad_tickers', 'cad_tickers.exchanges']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=5.2,<6.0', 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'cad-tickers',
    'version': '0.1.2',
    'description': 'Various Stock Utilties Created by me',
    'long_description': '## Cad Tickers\n\nSet of utilities modules designed to scrap data from the web.\n\nWill write more documentation later, for now refer to test cases.\n',
    'author': 'David Li',
    'author_email': 'davidli012345@gmail.com',
    'maintainer': 'David Li',
    'maintainer_email': 'davidli012345@gmail.com',
    'url': 'https://github.com/FriendlyUser/cad_tickers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
