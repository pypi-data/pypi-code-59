# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['penguin-libraries',
 'penguin-libraries.EasyML',
 'penguin-libraries.EfficientGAN',
 'penguin-libraries.EfficientGAN.models',
 'penguin-libraries.templates']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.1.2,<8.0.0',
 'PyYAML>=5.3.1,<6.0.0',
 'lightgbm>=2.3.1,<3.0.0',
 'numpy>=1.18.5,<2.0.0',
 'optuna>=1.5.0,<2.0.0',
 'pandas>=1.0.4,<2.0.0',
 'pytorch-lightning==0.7.6',
 'scikit-learn>=0.23.1,<0.24.0',
 'tensorboard>=2.2.2,<3.0.0',
 'torch==1.5.0',
 'torchvision==0.6.0']

setup_kwargs = {
    'name': 'penguin-libraries',
    'version': '0.1.0',
    'description': 'Implementation of useful api.',
    'long_description': None,
    'author': 'PixelPenguin',
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
