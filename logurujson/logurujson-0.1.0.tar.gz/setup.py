# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logurujson']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.1,<0.6.0']

setup_kwargs = {
    'name': 'logurujson',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Amit Oren',
    'author_email': 'amit@panorays.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
