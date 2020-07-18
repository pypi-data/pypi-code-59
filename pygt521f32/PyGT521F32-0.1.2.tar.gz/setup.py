# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['GT521F32', 'GT521F32-viewer', 'GT521F32.interfaces']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.2.0,<8.0.0', 'pyserial>=3.4,<4.0']

extras_require = \
{':sys_platform == "linux"': ['cython-sgio>=1.1.2,<2.0.0']}

setup_kwargs = {
    'name': 'pygt521f32',
    'version': '0.1.2',
    'description': 'An SDK module for the ADH-Tech GT521F32 fingerprint scanner',
    'long_description': None,
    'author': 'Alon',
    'author_email': 'alonlivne@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
