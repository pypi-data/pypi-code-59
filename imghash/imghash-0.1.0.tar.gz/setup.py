# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imghash']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>2,<8']

entry_points = \
{'console_scripts': ['imghash = imghash:main']}

setup_kwargs = {
    'name': 'imghash',
    'version': '0.1.0',
    'description': 'Hash images based on pixel content',
    'long_description': None,
    'author': 'Florian Ludwig',
    'author_email': 'f.ludwig@greyrook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
