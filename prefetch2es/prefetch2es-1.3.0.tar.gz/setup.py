# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['prefetch2es']
install_requires = \
['elasticsearch>=7.8.0,<8.0.0',
 'pyprefetch-rs>=0.1.0,<0.2.0',
 'setuptools>=49.2.0,<50.0.0',
 'setuptools_rust>=0.10.6,<0.11.0',
 'tqdm>=4.48.0,<5.0.0',
 'wheel>=0.34.2,<0.35.0']

entry_points = \
{'console_scripts': ['prefetch2es = prefetch2es:main']}

setup_kwargs = {
    'name': 'prefetch2es',
    'version': '1.3.0',
    'description': 'A library for fast import of Windows Prefetch into Elasticsearch.',
    'long_description': "# Prefetch2es\n[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)\n[![PyPI version](https://badge.fury.io/py/prefetch2es.svg)](https://badge.fury.io/py/prefetch2es)\n[![Python Versions](https://img.shields.io/pypi/pyversions/prefetch2es.svg)](https://pypi.org/project/prefetch2es/)\n\nImport Windows Prefetch(.pf) to Elasticsearch\n\nprefetch2es uses Rust library [pyprefetch-rs](https://github.com/sumeshi/pyprefetch-rs).\n\n```\nNote: Nov 11, 2019\n    Moved main development location to gitlab\n```\n\n## Usage\n```bash\n$ prefetch2es /path/to/your/file.pf\n```\n\nor\n\n```python\nfrom prefetch2es.prefetch2es import prefetch2es\n\nif __name__ == '__main__':\n    filepath = '/path/to/your/file.pf'\n    prefetch2es(filepath)\n```\n\n### Options\n```\n--host: \n    ElasticSearch host address\n    (default: localhost)\n\n--port: \n    ElasticSearch port number\n    (default: 9200)\n\n--index: \n    Index name\n    (default: prefetch2es)\n\n--type: \n    Document-type name\n    (default: prefetch2es)\n\n```\n\n### Examples\n```\n$ prefetch2es /path/to/your/file.pf --host=localhost --port=9200 --index=foo --type=bar\n```\n\n```py\nif __name__ == '__main__':\n    prefetch2es('/path/to/your/file.pf', host=localhost, port=9200, index='foo', type='bar')\n```\n\n## Installation\n### via pip\n```\n$ pip install prefetch2es\n```\n\nThe source code for prefetch2es is hosted at GitHub, and you may download, fork, and review it from this repository(https://github.com/sumeshi/prefetch2es).\n\nPlease report issues and feature requests. :sushi: :sushi: :sushi:\n\n## License\nprefetch2es is released under the [MIT](https://github.com/sumeshi/prefetch2es/blob/master/LICENSE) License.\n\nPowered by [pyprefetch-rs](https://github.com/sumeshi/pyprefetch-rs).  ",
    'author': 'sumeshi',
    'author_email': 'j15322sn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sumeshi/prefetch2es',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
