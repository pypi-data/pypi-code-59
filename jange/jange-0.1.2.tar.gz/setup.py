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
    'version': '0.1.2',
    'description': 'Easy NLP library for Python',
    'long_description': None,
    'author': 'Sanjaya Subedi',
    'author_email': 'jangedoo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
