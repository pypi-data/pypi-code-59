# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['contra_rotor']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow>=1.10.10,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'requests>=2.24.0,<3.0.0']

entry_points = \
{'console_scripts': ['contra-rotor = contra_rotor.console:main']}

setup_kwargs = {
    'name': 'contra-rotor',
    'version': '0.1.0',
    'description': '',
    'long_description': '# contra-rotor',
    'author': 'Lucas Melin',
    'author_email': 'lucas.melin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lucasmelin/contra-rotor.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
