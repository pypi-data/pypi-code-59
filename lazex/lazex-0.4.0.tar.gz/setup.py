# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['lazex']
install_requires = \
['astunparse>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'lazex',
    'version': '0.4.0',
    'description': 'Allow functions to examine and modify the AST of their arguments',
    'long_description': None,
    'author': 'L3viathan',
    'author_email': 'git@l3vi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
