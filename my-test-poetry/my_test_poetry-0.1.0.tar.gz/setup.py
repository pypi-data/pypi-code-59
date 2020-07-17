# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_test_poetry']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'my-test-poetry',
    'version': '0.1.0',
    'description': '测试poetry上传到pipy',
    'long_description': None,
    'author': 'wangchenwei',
    'author_email': 'wangchenwei@focuschina.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
