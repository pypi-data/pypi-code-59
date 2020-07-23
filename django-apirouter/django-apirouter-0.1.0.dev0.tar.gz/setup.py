# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['apirouter']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0.8,<4.0.0']

setup_kwargs = {
    'name': 'django-apirouter',
    'version': '0.1.0.dev0',
    'description': 'Django API router',
    'long_description': '# django-apirouter\n',
    'author': 'Anton Ruhlov',
    'author_email': 'antonruhlov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/antonrh/django-apirouter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
