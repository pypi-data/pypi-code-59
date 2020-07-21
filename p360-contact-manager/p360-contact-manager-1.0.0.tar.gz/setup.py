# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['p360_contact_manager',
 'p360_contact_manager.api',
 'p360_contact_manager.usecases']

package_data = \
{'': ['*']}

install_requires = \
['dependencies>=2.0.0,<3.0.0',
 'iso3166>=1.0,<2.0',
 'requests>=2.24.0,<3.0.0',
 'returns>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'p360-contact-manager',
    'version': '1.0.0',
    'description': 'Public 360 application by Tieto has some issues with for example duplicated contacts. This package tries to fix that and adds other functionality like synchronization(enrichment) with brreg.no.',
    'long_description': '![test](https://github.com/greenbird/p360-contact-manager/workflows/test/badge.svg)\n[![codecov](https://codecov.io/gh/greenbird/p360-contact-manager/branch/master/graph/badge.svg)](https://codecov.io/gh/greenbird/p360-contact-manager)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\n# P360 Contact Manager\n\n## Why\n\nWhile there are built in methods to syncronize against for example brønnøysundregisteret, to enrich data or update data they are slow and point and click oriented.\nThere are also cases where duplicates are created by external programs.\nThis program tries to fix some of those issues.\n\n\n## How\n\nP360 exposes an API for dealing with contacts. It is through this api that we find, update, and fix enterprises in p360.\n\n\n## Setup\n\neasier setup will be available if the package goes to pypi. Then it would be as simple as doing pip install p360-contact-manager and use it directly like:\n\n```sh\n$ python p360_contact_manager args args action\n```\n\nBut for now we install it from source. so clone the repo first. then:\n\n### Get poetry\n\nget poetry - dependency management:\n```sh\n$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python\n```\n\nMake poetry create virtualenv in project folder. This makes it easier for IDE\'s to run correct virtualenv while debuging/running linters etc.\n```sh\n$ poetry config settings.virtualenvs.in-project true\n```\n\n### Get Pyenv - optional\n\npyenv is a nice tool that lets you \'activate\' a version of python either globally, locally or for one shell instance. its really nice and i reccomend getting it and using it now but it is not needed for this program to work.\n\nwith brew:\n```sh\n$ brew update\n$ brew install pyenv\n```\n\nPut this command into the of `~/.bash_profile` or run `pyenv init` to make sure where to put it for for example zsh.\n```\n$ eval "$(pyenv init -)"\n```\n\ninstall a version of python 3.7.2+: This installs a clean python to pyenvs folders and lets us reference that as a \'base\' in our virtualenvs.\n```sh\n$ pyenv install 3.7.4\n```\n\n## Usage\n\nif you did install pyenv activate pyenv for the current shell\n```sh\n$ pyenv shell 3.7.4\n```\n\nRun this to install required packages and a virtualenv\n- if you do not plan on developing on this, add the flag: --no-dev\n```sh\n$ poetry install\n```\n\n### Test\n\n```sh\n$ poetry run python p360_contact_manager --authkey the_key test\n```\n\n### Create a \'Cache\'(json file) of all enterprises in p360\n```sh\npoetry run python p360_contact_manager --authkey the_key cache_enterprises\n```\nadd -c or --cached argument to use local cached json file.\n\n\n### Create duplicate worklist\n```sh\npoetry run python p360_contact_manager --authkey the_key duplicates -c\n```\n\n### Update with worklist\ntip: use --dry to check if everything looks good before continuing\n```sh\n$ poetry run python p360_contact_manager --authkey the_key update --worklist json_worklist_file.json\n```\n\n### Create Brreg data syncronize worklist\nfor now just add the key even though its not needed its flagged as required... will fix.\n```sh\n$ poetry run python p360_contact_manager --authkey the_key brreg_syncronize\n```\n\n### Call synchronize with brreg data worklist\n```sh\n$ poetry run python p360_contact_manager --authkey the_key synchronize --worklist brreg_synchronize_worklist.json\n```\n',
    'author': 'Thomas Borgen',
    'author_email': 'thomas.borgen@greenbird.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/greenbird/p360-contact-manager',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
