# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gnxi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gnxi',
    'version': '0.0.0a0',
    'description': 'A Python gNxI project namespace package',
    'long_description': '# A Python gNxI Project\n\nThis project is part of a development effort to build a modular set of python packages \nfor building on top of [OpenConfig gRPC Network Management & Operations Interfaces](https://www.openconfig.net/projects/rpc/).\n\nThis project is currently a namespace placeholder and will be updated as individual \ncomponents get published.\n',
    'author': 'Arun Babu Neelicattu',
    'author_email': 'arun.neelicattu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/python-gnxi',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
