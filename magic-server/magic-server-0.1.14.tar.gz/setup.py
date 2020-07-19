# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magic', 'magic.things']

package_data = \
{'': ['*']}

install_requires = \
['magicdb>=0.0.6,<0.0.7', 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'magic-server',
    'version': '0.1.14',
    'description': '',
    'long_description': '# Jeremy Poetry Test\n\nThe awesome test!',
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
