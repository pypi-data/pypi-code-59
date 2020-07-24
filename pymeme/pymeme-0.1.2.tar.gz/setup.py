# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymeme']

package_data = \
{'': ['*']}

install_requires = \
['loguru', 'psutil']

setup_kwargs = {
    'name': 'pymeme',
    'version': '0.1.2',
    'description': 'Python and memes.',
    'long_description': '# Pymeme\n',
    'author': 'sangarshanan',
    'author_email': 'sangarshanan1998@gmail.com',
    'maintainer': 'sangarshanan',
    'maintainer_email': 'sangarshanan1998@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
