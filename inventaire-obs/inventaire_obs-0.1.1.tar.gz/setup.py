# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inventaire_obs']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'netmiko>=3.1.1,<4.0.0']

setup_kwargs = {
    'name': 'inventaire-obs',
    'version': '0.1.1',
    'description': "Script d'inventaire OBS",
    'long_description': 'Usage: inventaire_obs.py [OPTIONS]\n\nOptions:\n\n  --help               Show this message and exit.\n  \n  -n, --name TEXT      Nom de code du magasin  [required]\n  \n  -f, --fichier TEXT   Nom du fichier avec les IPs  [required] // Une IP par ligne\n  \n  -s, --sortie TEXT    Nom du fichier de sortie\n  \n  -u, --username TEXT  Username  [required]\n  \n  -p, --password TEXT  Password\n  ',
    'author': 'Thomas Christory',
    'author_email': 'thomas@christory.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
