# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['penguin_libraries',
 'penguin_libraries.EasyML',
 'penguin_libraries.EfficientGAN',
 'penguin_libraries.EfficientGAN.models',
 'penguin_libraries.templates']

package_data = \
{'': ['*']}

install_requires = \
['Pillow',
 'PyYAML',
 'lightgbm',
 'numpy',
 'optuna',
 'pandas',
 'pytorch-lightning',
 'scikit-learn',
 'tensorboard',
 'torch',
 'torchvision']

setup_kwargs = {
    'name': 'penguin-libraries',
    'version': '0.1.6',
    'description': 'Easy and useful libraries.',
    'long_description': None,
    'author': 'PixelPenguin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
