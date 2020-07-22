# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['feature_graph']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-bigquery>=1.25.0,<2.0.0',
 'graphviz>=0.14.1,<0.15.0',
 'loguru>=0.5.1,<0.6.0']

setup_kwargs = {
    'name': 'feature-graph',
    'version': '0.2.0',
    'description': 'A simple DAG orchestrator built specifically for machine learning feature generation',
    'long_description': None,
    'author': 'Murray Vanwyk',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
