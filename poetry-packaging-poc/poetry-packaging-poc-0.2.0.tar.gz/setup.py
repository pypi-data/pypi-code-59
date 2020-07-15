# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_packaging_poc']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['poetry-packaging-poc = poetry_packaging_poc.console:main']}

setup_kwargs = {
    'name': 'poetry-packaging-poc',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Marcos Dami\xc3\xa1n Mesmer y Rosset',
    'author_email': 'marcosdmyr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
