# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['unminder']

package_data = \
{'': ['*']}

install_requires = \
['telethon>=1.14.0,<2.0.0']

entry_points = \
{'console_scripts': ['queue = unminder.cli:queue',
                     'review = unminder.cli:review']}

setup_kwargs = {
    'name': 'unminder',
    'version': '0.1.0',
    'description': 'Queue things in a list, review them later.',
    'long_description': '# Unminder\n\n[![ci](https://github.com/pawamoy/unminder/workflows/ci/badge.svg)](https://github.com/pawamoy/unminder/actions?query=workflow%3Aci)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/unminder/)\n[![pypi version](https://img.shields.io/pypi/v/unminder.svg)](https://pypi.org/project/unminder/)\n\nQueue things in a list, review them later.\n\n## Requirements\n\nUnminder requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.8\n\n# make it available globally\npyenv global system 3.6.8\n```\n</details>\n\n## Installation\n\nWith `pip`:\n```bash\npython3.6 -m pip install unminder\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npython3.6 -m pip install --user pipx\n\npipx install --python python3.6 unminder\n```\n',
    'author': 'Timothée Mazzucotelli',
    'author_email': 'pawamoy@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pawamoy/unminder',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
