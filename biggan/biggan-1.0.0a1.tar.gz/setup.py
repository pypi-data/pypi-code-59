# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['biggan', 'biggan.architecture', 'biggan.config', 'biggan.scripts']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3.1,<6.0.0', 'tensorflow>=2.2,<3.0']

entry_points = \
{'console_scripts': ['biggan.prepare = biggan.scripts.prepare:main',
                     'biggan.train = biggan.scripts.train:main']}

setup_kwargs = {
    'name': 'biggan',
    'version': '1.0.0a1',
    'description': 'BigGAN in idiomatic Keras',
    'long_description': None,
    'author': 'Jon Kyl',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
