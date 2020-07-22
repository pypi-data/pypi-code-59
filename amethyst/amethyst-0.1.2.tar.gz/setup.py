# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amethyst']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3,<6.0', 'appdirs>=1.4,<2.0', 'click>=7.1.2,<8.0.0']

extras_require = \
{'qt': ['PyQt5==5.14']}

entry_points = \
{'console_scripts': ['amethyst = amethyst.main:main',
                     'amy = amethyst.main:main']}

setup_kwargs = {
    'name': 'amethyst',
    'version': '0.1.2',
    'description': 'A general-purpose keyboard-based launcher.',
    'long_description': '# Amethyst\n\n*A general-purpose keyboard-centric launcher with a radial menu.*\n\nPlease read the [Amethyst documentation](https://roipoussiere.frama.io/amethyst) for more information about Amethyst, how to use it and how to contribute.\n',
    'author': 'Nathanaël Jourdane',
    'author_email': 'roipoussiere@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://framagit.org/roipoussiere/amethyst',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
