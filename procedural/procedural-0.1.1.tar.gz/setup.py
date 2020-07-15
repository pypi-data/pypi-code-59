# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['procedural', 'procedural.utils']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'procedural',
    'version': '0.1.1',
    'description': "A Python client for interacting with Procedural's REST APIs.",
    'long_description': "# Procedural\n\nA Python client for interacting with [Procedural's](www.procedural.build/) REST APIs.\n\n",
    'author': 'Christian Kongsgaard',
    'author_email': 'christian@procedural.build',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/procedural-build/procedural-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
