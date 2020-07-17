# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taomn', 'taomn.elements']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'clint>=0.5.1,<0.6.0',
 'docker>=3.5.0,<4.0.0',
 'pastel>=0.1.0,<0.2.0',
 'python-slugify>=1.2,<2.0']

entry_points = \
{'console_scripts': ['taomn = taomn.taomn:main']}

setup_kwargs = {
    'name': 'taomn',
    'version': '0.5.4',
    'description': 'Quickstart your Tao masternode',
    'long_description': '# taomn <a href="https://gitter.im/taoblockchain/taomn"><img align="right" src="https://badges.gitter.im/gitterHQ/gitter.png"></a>\n\n| Branch  | Status | Coverage |\n| --- | --- | --- |\n| Master | [![Build Status](https://travis-ci.org/taoblockchain/taomn.svg?branch=master)](https://travis-ci.org/taoblockchain/taomn) | [![Coverage Status](https://coveralls.io/repos/github/taoblockchain/taomn/badge.svg?branch=master)](https://coveralls.io/github/taoblockchain/taomn?branch=master) |\n| Develop | [![Build Status](https://travis-ci.org/taoblockchain/taomn.svg?branch=develop)](https://travis-ci.org/taoblockchain/taomn) | [![Coverage Status](https://coveralls.io/repos/github/taoblockchain/taomn/badge.svg?branch=develop)](https://coveralls.io/github/taoblockchain/taomn?branch=develop) |\n\nTao MasterNode (taomn) is a cli tool to help you run a Tao masternode\n\n## Running and applying a masternode\n\nIf you are consulting this repo, it\'s probably because you want to run a masternode.\nFor complete guidelines on running a masternode candidate, please refer to the [documentation](https://docs.tao.network/masternode/requirements/).\n',
    'author': 'Bryce Weiner',
    'author_email': 'bryce@tao.network',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tao.network',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
