# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['saa_contours_converter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'saa-contours-converter',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'John Doe',
    'author_email': 'john-doe@example.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=666,<667',
}


setup(**setup_kwargs)
