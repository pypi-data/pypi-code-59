# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grpc_interceptor']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'grpc-interceptor',
    'version': '0.8.0',
    'description': 'Simplifies gRPC interceptors',
    'long_description': '[![Tests](https://github.com/d5h-foss/grpc-interceptor/workflows/Tests/badge.svg)](https://github.com/d5h-foss/grpc-interceptor/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/d5h-foss/grpc-interceptor/branch/master/graph/badge.svg)](https://codecov.io/gh/d5h-foss/grpc-interceptor)\n[![PyPI](https://img.shields.io/pypi/v/grpc-interceptor.svg)](https://pypi.org/project/grpc-interceptor/)\n[![Read the Docs](https://readthedocs.org/projects/grpc-interceptor/badge/)](https://grpc-interceptor.readthedocs.io/)\n\n# Summary\n\nSimplified Python gRPC interceptors.\n\n# Documentation\n\nRead the [documentation here](https://grpc-interceptor.readthedocs.io/).\n',
    'author': 'Dan Hipschman',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/d5h-foss/grpc-interceptor',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
