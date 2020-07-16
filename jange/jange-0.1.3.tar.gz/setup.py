# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jange', 'jange.ops', 'jange.ops.text', 'jange.stream', 'jange.vis']

package_data = \
{'': ['*']}

install_requires = \
['cytoolz>=0.10.0,<0.11.0',
 'jsonschema>=3.2.0,<4.0.0',
 'pandas==0.24.2',
 'plotly>=4.8.2,<5.0.0',
 'psycopg2-binary>=2.8.3,<3.0.0',
 'scikit-learn>=0.23.1,<0.24.0',
 'spacy>=2.2.0,<3.0.0',
 'sqlalchemy==1.3.1']

setup_kwargs = {
    'name': 'jange',
    'version': '0.1.3',
    'description': 'Easy NLP library for Python',
    'long_description': "# jange\n[![Build Status](https://travis-ci.org/jangedoo/jange.svg?branch=master)](https://travis-ci.org/jangedoo/jange)\n------\njange is an easy to use NLP library for Python. It is based on popular libraries like `pandas`, `scikit-learn`, `spacy`, `plotly` and others.\n\n# Installation\n```\npip install jange\n```\n\n## From source\nThis project uses poetry to manage dependencies. If you don't already have poetry installed then go to https://python-poetry.org/docs/#installation for instructions on how to install it for your OS.\n\nOnce poetry is installed, from the root directory of this project, run `poetry install`. It will create a virtual environment for this project and install the necessary dependencies (including dev dependencies).\n",
    'author': 'Sanjaya Subedi',
    'author_email': 'jangedoo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jangedoo/jange',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
