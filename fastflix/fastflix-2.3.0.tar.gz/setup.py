# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastflix',
 'fastflix.builders',
 'fastflix.plugins',
 'fastflix.plugins.av1',
 'fastflix.plugins.common',
 'fastflix.plugins.gif',
 'fastflix.plugins.hevc',
 'fastflix.plugins.svt_av1',
 'fastflix.plugins.vp9',
 'fastflix.widgets',
 'fastflix.widgets.panels']

package_data = \
{'': ['*'], 'fastflix': ['data/*', 'data/rotations/*']}

install_requires = \
['PySide2>=5.15.0,<6.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'python-box[all]>=5.0.1,<6.0.0',
 'requests>=2.24.0,<3.0.0',
 'reusables>=0.9.5,<0.10.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'shiboken2>=5.15.0,<6.0.0']

entry_points = \
{'console_scripts': ['fastflix = fastflix.__main__:main']}

setup_kwargs = {
    'name': 'fastflix',
    'version': '2.3.0',
    'description': 'Easy to use video encoder GUI wrapper',
    'long_description': None,
    'author': 'Chris Griffith',
    'author_email': 'chris@cdgriffith.com',
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
