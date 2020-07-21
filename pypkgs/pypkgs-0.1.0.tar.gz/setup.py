# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypkgs']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.5,<2.0.0']

setup_kwargs = {
    'name': 'pypkgs',
    'version': '0.1.0',
    'description': 'Python package that eases the pain of concatenating Pandas categoricals!',
    'long_description': None,
    'author': 'Tomas Beuzen',
    'author_email': 'tomas.beuzen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
