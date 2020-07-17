# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['create_tao_masternode', 'create_tao_masternode.templates']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'jinja2>=2.10,<3.0', 'pyyaml>=3.13,<4.0']

entry_points = \
{'console_scripts': ['create-tao-masternode = '
                     'create_tao_masternode.main:entrypoint']}

setup_kwargs = {
    'name': 'create-tao-masternode',
    'version': '1.2.5',
    'description': 'Set up a Tao masternode by running one command.',
    'long_description': '# create-tao-masternode\nSet up a Tao masternode by running one command.\n\nFor guides and user documentation, please check the [official documentation](https://docs.tao.network/masternode/create-tao-masternode).\n\n## Development\n\nInstall poetry.\n```\npip3 install --user poetry\n```\n\nInstall the project dependencies.\n```\npoetry install\n```\n\nRun tests.\n```\npoetry run python -m pytest\n```\n',
    'author': 'bryce-weiner',
    'author_email': 'bryce@tao.network',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tao.network',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
