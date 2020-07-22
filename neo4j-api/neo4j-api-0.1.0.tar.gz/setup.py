# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neo4j_api']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['neo4j-api = neo4j_api.cli:main']}

setup_kwargs = {
    'name': 'neo4j-api',
    'version': '0.1.0',
    'description': 'A Neo4j API in Python with FastAPI.',
    'long_description': '# Neo4J API\n\n[![ci](https://github.com/pawamoy/neo4j-api/workflows/ci/badge.svg)](https://github.com/pawamoy/neo4j-api/actions?query=workflow%3Aci)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/neo4j-api/)\n[![pypi version](https://img.shields.io/pypi/v/neo4j-api.svg)](https://pypi.org/project/neo4j-api/)\n\nA Neo4j API in Python with FastAPI.\n\n## Requirements\n\nNeo4J API requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.8\n\n# make it available globally\npyenv global system 3.6.8\n```\n</details>\n\n## Installation\n\nWith `pip`:\n```bash\npython3.6 -m pip install neo4j-api\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npython3.6 -m pip install --user pipx\n\npipx install --python python3.6 neo4j-api\n```\n',
    'author': 'Timothée Mazzucotelli',
    'author_email': 'pawamoy@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pawamoy/neo4j-api',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
