# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_wise_utils']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3.1,<6.0.0']

setup_kwargs = {
    'name': 'python-wise-utils',
    'version': '0.1.5',
    'description': 'Python interpreter convenience utilities',
    'long_description': None,
    'author': 'Wisdom Wolf',
    'author_email': 'wisdomwolf@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
