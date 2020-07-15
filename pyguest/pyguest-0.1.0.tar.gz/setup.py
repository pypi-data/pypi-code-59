# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyguest']
install_requires = \
['numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'pyguest',
    'version': '0.1.0',
    'description': 'A simple python package for simulating event attendance from a guest list.',
    'long_description': None,
    'author': 'Tomas Beuzen',
    'author_email': 'tomas.beuzen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
