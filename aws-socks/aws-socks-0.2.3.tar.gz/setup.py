# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['socks']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.9,<2.0']

setup_kwargs = {
    'name': 'aws-socks',
    'version': '0.2.3',
    'description': 'A wrapper for boto3 to provide one-liners for common AWS tasks.',
    'long_description': '\n<h3 align="center">socks</h3>\n\n---\n\n<p align="center"> \n    Most AWS tasks are solved problems. Stop reinventing the wheel.\n    <br> \n</p>\n\n## 📝 Table of Contents\n- [About](#about)\n- [Getting Started](#getting_started)\n- [Usage](https://github.com/devenjarvis/aws-socks/wiki/Usage)\n- [Contributing](/CONTRIBUTING.md)\n- [Contributors](#contributors)\n- [Roadmap](https://github.com/devenjarvis/aws-socks/wiki/Roadmap)\n\n## 🧐 About <a name = "about"></a>\nCurrent Version: 0.2.3\n\n`socks` is a Python library designed to abstract common AWS tasks as one liners. It is opinionated in the pursuit to provide the most performant implementation that can be leveraged generally, but also attempts to offer reasonable levels of customization to the developer by supporting most boto3 functionality.\n\nThis package attempts to provide performant abstractions of the most common AWS tasks for the most common AWS services, so you can spend less time finding the best way to get that object from S3 and more time on what you actually want to do with that object (as an example).\n\nThis package is not comprehensive across all (or even most) AWS services at this time, but I hope to grow this overtime so a majority of the AWS tasks you find yourself re-solving or copying from one repo to the next can be implemented here in the most efficient way.\n\n\n## 🏁 Getting Started <a name = "getting_started"></a>\nPlease note socks has not yet hit the 1.0 release so breaking API changes may occur. I\'ll try to limit those as possible and document them when they happen, but if you\'d like to use socks it might be a good idea to lock your version in your requirements.txt file.\n\nIf you\'d like to install the library locally or without code warp/spawn you can use the following install command:\n\n`pip install aws-socks`\n\nTo upgrade an existing install use:\n\n`pip install --upgrade aws-socks`\n\nOnce installed use `import socks` to start using it.\n\n### Prerequisites\n- The only external dependency for this library is boto3 which is packaged within the library.\n- This package expects Python version 3.6 and up. There are no plans to support previous versions of Python.\n\n## 🤠 Contributors <a name = "contributors"></a>\n- [@jones-chris] (https://github.com/jones-chris) - Maintainer\n- [@devenjarvis](https://github.com/devenjarvis) - Maintainer\n- [@artkinghur](https://github.com/artkinghur) - SSM get_parameter exception handling\n- [@arief-akbarr](https://github.com/arief-akbar) - Scan Dynamo Operation, Invoke Lambda Function\n- [@ds0440](https://github.com/ds0440) - Support of boto3 kwargs',
    'author': 'Deven Jarvis',
    'author_email': 'devenjarvis@gmail.com',
    'url': 'https://github.com/devenjarvis/aws-socks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
