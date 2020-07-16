# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roboself',
 'roboself.cli',
 'roboself.cli.commands',
 'roboself.cli.template.skill']

package_data = \
{'': ['*'], 'roboself.cli.template.skill': ['nlg/*', 'nlu/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'python-socketio[client]>=4.6.0,<5.0.0',
 'pyyaml>=5.3.1,<6.0.0',
 'redis>=3.5.3,<4.0.0',
 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'roboself',
    'version': '0.1.1',
    'description': 'The roboself python client.',
    'long_description': None,
    'author': 'Razvan Dinu',
    'author_email': 'razvan@roboself.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
