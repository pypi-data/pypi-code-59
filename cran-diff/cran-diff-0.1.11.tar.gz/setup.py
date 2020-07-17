# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cran_diff']

package_data = \
{'': ['*']}

install_requires = \
['bs4',
 'deb_pkg_tools',
 'pandas',
 'psycopg2-binary',
 'python-dateutil',
 'requests',
 'rpy2',
 'scipy',
 'sqlalchemy',
 'tqdm',
 'typing']

setup_kwargs = {
    'name': 'cran-diff',
    'version': '0.1.11',
    'description': '',
    'long_description': None,
    'author': 'Aoife Curran',
    'author_email': 'aocurran@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
