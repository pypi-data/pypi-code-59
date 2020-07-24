# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['deepqmc',
 'deepqmc.data',
 'deepqmc.tools',
 'deepqmc.torchext',
 'deepqmc.wf',
 'deepqmc.wf.paulinet']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0',
 'toml>=0.10.0,<0.11.0',
 'torch>=1.2,<2.0',
 'uncertainties>=3.1.2,<4.0.0']

extras_require = \
{'all': ['scipy>=1.2,<2.0',
         'pyscf>=1.6,<2.0',
         'pytest>=4.4,<5.0',
         'coverage>=4.5,<5.0',
         'tensorboard>=2.0,<3.0',
         'tqdm>=4.31,<5.0',
         'h5py>=2.10.0,<3.0.0',
         'Pillow>=7,<8',
         'click>=7.0,<8.0'],
 'cli': ['click>=7.0,<8.0'],
 'doc': ['sphinx>=2.2,<3.0', 'sphinxcontrib-katex>=0.5.1,<0.6.0'],
 'test': ['pytest>=4.4,<5.0', 'coverage>=4.5,<5.0'],
 'train': ['tensorboard>=2.0,<3.0',
           'tqdm>=4.31,<5.0',
           'h5py>=2.10.0,<3.0.0',
           'Pillow>=7,<8'],
 'wf': ['scipy>=1.2,<2.0', 'pyscf>=1.6,<2.0']}

entry_points = \
{'console_scripts': ['deepqmc = deepqmc.cli:cli']}

setup_kwargs = {
    'name': 'deepqmc',
    'version': '0.1.0',
    'description': 'Deep-learning quantum Monte Carlo for electrons in real space',
    'long_description': None,
    'author': 'Jan Hermann',
    'author_email': 'jan.hermann@fu-berlin.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
