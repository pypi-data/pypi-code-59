# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyppium', 'pyppium.utils']

package_data = \
{'': ['*']}

install_requires = \
['Appium-Python-Client==1.0.2']

setup_kwargs = {
    'name': 'pyppium',
    'version': '0.1.0',
    'description': 'Pyppium is a wrapper of Appium-Python-Client for cross mobile testing.',
    'long_description': '# Pyppium\n\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n[![codecov](https://codecov.io/gh/leomenezessz/pyppium-wrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/leomenezessz/pyppium-wrapper)\n[![Documentation Status](https://readthedocs.org/projects/pyppium/badge/?version=latest)](https://pyppium.readthedocs.io/en/latest/?badge=latest)\n\n\n\nPyppium is a wrapper of Appium-Python-Client for cross mobile testing.\n\n## Installation\n\n```\n$ pip install pyppium\n```\n\n## Basic Usage\n\nCreate your screen like this\n\n```python\nfrom pyppium.fetcher import fetch, iOS, Android\n\n\nclass ScreenOne:\n    _button = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))\n    _text_field = fetch(iOS("id", "inputUserName"), Android("id", "username"))\n    _text_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))\n\n    def login(self, username, password):\n        self._text_field.send_keys(username)\n        self._text_password.send_keys(password)\n        self._button.click()\n\n    \n```\n\nUser your screen in test after start pyppium driver\n\n```python\nfrom pyppium.driver import PyppiumDriver\nfrom tests.e2e.screens.screen import ScreenOne, ScreenTwo\nfrom assertpy import assert_that\n\n\ndef test_android_basic_behaviours():\n    username = "Lully"\n    password = "123456789"\n\n    caps_android ={\n            "platformName": "Android",\n            "automationName": "uiautomator2",\n            "deviceName": "Android Emulator",\n            "appPackage": "com.example.dummy",\n            "appActivity": "MainActivity",\n            "newCommandTimeout": 0,\n    }\n\n\n    PyppiumDriver(caps_android)\n    ScreenOne().login(username, password)\n    assert_that(ScreenTwo().label_welcome_message()).contains(username)\n    PyppiumDriver.quit()\n```\n\n## Documentation\n\n- https://pyppium.readthedocs.io/en/latest/\n\n\n\n\n\n\n\n\n',
    'author': 'Leonardo Menezes',
    'author_email': 'leonardosmenezes.ssz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/leomenezessz/pyppium',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
