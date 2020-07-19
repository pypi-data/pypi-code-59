# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jeremy_poetry_test', 'jeremy_poetry_test.things']

package_data = \
{'': ['*']}

install_requires = \
['magicdb>=0.0.6,<0.0.7', 'requests>=2.24.0,<3.0.0']

entry_points = \
{'console_scripts': ['jeremy-poetry-test = jeremy_poetry_test:things']}

setup_kwargs = {
    'name': 'jeremy-poetry-test',
    'version': '0.1.8',
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
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
