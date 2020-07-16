# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morpho', 'morpho.proto', 'morpho.proto.grpc', 'morpho.rest']

package_data = \
{'': ['*'], 'morpho.rest': ['swagger/*', 'swagger/.swagger-codegen/*']}

install_requires = \
['colorama>=0.4.3,<0.5.0',
 'dataclasses-json>=0.3.7,<0.4.0',
 'flask>=1.1.1,<2.0.0',
 'googleapis-common-protos>=1.6.0,<2.0.0',
 'py-eureka-client>=0.7.4,<0.8.0',
 'pydantic>=1.5.1,<2.0.0',
 'pytest>=5.4.1,<6.0.0',
 'regex>=2020.6.7,<2021.0.0',
 'requests>=2.22.0,<3.0.0',
 'toml>=0.10.0,<0.11.0',
 'waitress>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'morpho',
    'version': '1.0.0a4',
    'description': 'Framework for document transformations as microservice based web services.',
    'long_description': '<img src="docs/images/morpho.png" width="100%" alt="Morpho Logo">\n\n> Python port for the go written [doctrans](https://github.com/theovassiliou/doctrans)\n\n<div align="center">\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square">\n</a>\n<a href=""><img alt="license: MIT" src="https://img.shields.io/badge/license%3A-MIT-green?style=flat-square">\n</a>\n<a href=""><img src="https://img.shields.io/badge/python%3A-%5E3.8-blue?style=flat-square"></a><br>\n<a href=""><img src="https://circleci.com/gh/B4rtware/morpho.svg?style=shield&circle-token=5cd58aa7f458d098a3b9a82e861d87d64ec4a181"></a>\n<a href="https://codecov.io/gh/B4rtware/morpho">\n  <img src="https://codecov.io/gh/B4rtware/morpho/branch/master/graph/badge.svg?token=14BJUE5PY5" />\n</a>\n</div>\n\nMorpho is a framework for microservice based web services. It offers the ability to transform a given document with a provided function.\n\nIn the first place this framework was created to use it for research purposes.\n\n## 💡 Installation\n\n`pip install morpho`\n\n⚠️ currently in alpha: public api may change with breaking changes ⚠️\n\n### via git\n\n1. make sure to use at least **python 3.8**\n2. clone the repo `git clone https://github.com/B4rtware/morpho.git`\n3. `cd morpho` and install dependencies via\n    - `poetry install` ([Poetry](https://github.com/python-poetry/poetry))\n    or\n    - use the provided `requirements.txt`\n\n## ⚙️ Server Example\n\n### ... without options\n\nservice.py\n```python\nfrom morpho.server import Service\n\ndef work(document: str) -> str:\n    return document\n\nservice = Service(name="Echo", version="0.0.1")\n\nif __name__ == "__main__":\n    service.run()\n```\n\n### ... with options\n\nservice.py\n```python\nfrom morpho.server import Service\nfrom pydantic import BaseModel\n\nclass Options(BaseModel):\n    name: str\n\ndef work(document: str, options: Options) -> str:\n    return document + options.name\n\nservice = Service(name="AppendName", version="0.0.1", options_type=Options)\n\nif __name__ == "__main__":\n    service.run()\n```\n\n## 🖥️ Client Example\n\nclient.py\n```python\nfrom morpho.client import Client\nfrom morpho.client import ClientConfig\n\nmorpho = Client(ClientConfig("http://localhost:8761/eureka/"))\n\nresponse = morpho.transform_document(\n    "This is a Document!",\n    service_name="Echo"\n)\n\nprint(response.document)\n```\n`>>> This is a Document!`\n\n## 📝 License\nMIT\n',
    'author': 'B4rtware',
    'author_email': '34386047+B4rtware@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://python-poetry.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
