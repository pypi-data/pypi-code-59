# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anansi_market_data_handler']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.5,<2.0.0',
 'pendulum>=2.1.0,<3.0.0',
 'requests>=2.24.0,<3.0.0',
 'requests_mock>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'anansi-market-data-handler',
    'version': '0.1.0',
    'description': 'An API to obtain and manipulate market data, which aims to be independent from both market and  broker.',
    'long_description': '# Anansi Market Data Handler\n',
    'author': 'Marcus Vintem',
    'author_email': 'marcus@vintem.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcusmello/tradingbots',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
