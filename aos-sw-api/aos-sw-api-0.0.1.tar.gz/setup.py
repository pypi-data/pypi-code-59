# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aos_sw_api',
 'aos_sw_api.auth',
 'aos_sw_api.enums',
 'aos_sw_api.exceptions',
 'aos_sw_api.globel_models',
 'aos_sw_api.system',
 'aos_sw_api.validate']

package_data = \
{'': ['*']}

install_requires = \
['httpx==0.13.3', 'pydantic==1.5.1']

setup_kwargs = {
    'name': 'aos-sw-api',
    'version': '0.0.1',
    'description': 'ArubaOS Switch REST API',
    'long_description': '# ArubaOS Switch API\n',
    'author': 'Kenneth Sølberg',
    'author_email': 'solberg.kenneths94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KennethSoelberg/AOS-SW-API',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
