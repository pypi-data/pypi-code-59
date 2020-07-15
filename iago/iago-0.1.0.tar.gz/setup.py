# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iago']

package_data = \
{'': ['*']}

install_requires = \
['SpeechRecognition>=3.8.1,<4.0.0',
 'pandas>=1.0.5,<2.0.0',
 'playsound>=1.2.2,<2.0.0',
 'pyttsx3>=2.90,<3.0',
 'termcolor>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'iago',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Lorenzo Coacci',
    'author_email': 'lorenzo@coacci.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
