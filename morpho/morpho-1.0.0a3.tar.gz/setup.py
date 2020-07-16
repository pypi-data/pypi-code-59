# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morpho', 'morpho.proto', 'morpho.proto.grpc', 'morpho.rest']

package_data = \
{'': ['*'], 'morpho.rest': ['swagger/*', 'swagger/.swagger-codegen/*']}

install_requires = \
['colorama>=0.4.3,<0.5.0',
 'connexion[swagger-ui]==2.6.0',
 'dataclasses-json>=0.3.7,<0.4.0',
 'falcon>=2.0.0,<3.0.0',
 'flask-swagger-ui>=3.25.0,<4.0.0',
 'flask>=1.1.1,<2.0.0',
 'googleapis-common-protos>=1.6.0,<2.0.0',
 'psycopg2>=2.8.4,<3.0.0',
 'py-eureka-client>=0.7.4,<0.8.0',
 'pydantic>=1.5.1,<2.0.0',
 'pytest>=5.4.1,<6.0.0',
 'regex>=2020.6.7,<2021.0.0',
 'requests>=2.22.0,<3.0.0',
 'starlette>=0.13.4,<0.14.0',
 'swagger-ui-py>=0.2.1,<0.3.0',
 'toml>=0.10.0,<0.11.0',
 'uvicorn>=0.11.5,<0.12.0',
 'waitress>=1.4.2,<2.0.0',
 'wrapt_timeout_decorator>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'morpho',
    'version': '1.0.0a3',
    'description': '',
    'long_description': None,
    'author': 'B4rtware',
    'author_email': '34386047+B4rtware@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
