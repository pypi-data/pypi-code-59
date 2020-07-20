# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sorting_gym', 'sorting_gym.envs']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.17.2,<0.18.0', 'numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'sorting-gym',
    'version': '0.0.1',
    'description': 'OpenAI Gym Environments for Sorting based',
    'long_description': None,
    'author': 'Brian Thorne',
    'author_email': 'brian@hardbyte.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hardbyte/sorting-gym',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)
