# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textcmp', 'textcmp.tests', 'textcmp.textcmp']

package_data = \
{'': ['*']}

install_requires = \
['python-docx>=0.8.10,<0.9.0']

setup_kwargs = {
    'name': 'textcmp',
    'version': '0.1.1',
    'description': '陈沁开发的两文本比较工具，高亮颜色显示差异',
    'long_description': None,
    'author': '陈沁',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://poetry.chenqin.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.7,<4.0.0',
}


setup(**setup_kwargs)
