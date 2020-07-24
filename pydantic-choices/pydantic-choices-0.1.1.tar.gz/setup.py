# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_choices']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pydantic-choices',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Pydantic-Choices\n\n[![Build Status](https://travis-ci.com/vinissimus/pydantic-choices.svg?branch=master)](https://travis-ci.com/vinissimus/pydantic-choices) [![PyPI version](https://badge.fury.io/py/pydantic-choices.svg)](https://badge.fury.io/py/pydantic-choices) ![](https://img.shields.io/pypi/pyversions/pydantic-choices.svg) [![Codcov](https://codecov.io/gh/vinissimus/pydantic-choices/branch/master/graph/badge.svg)](https://codecov.io/gh/vinissimus/pydantic-choices/branch/master) ![](https://img.shields.io/github/license/vinissimus/pydantic-choices)\n\n## How to use\n\n```python\nfrom pydantic_choices import choice\n\nimport pydantic as pd\n\n\nLicenses = choice(["GPL", "GPLv3+", "MIT", "MPL 2.0"])\n\n\nclass Project(pd.BaseModel):\n    id: str\n    url: str\n    license: Licenses\n\n\n# Validation passes\nProject(\n    id="pydantic_choices",\n    url="https://github.com/vinissimus/pydantic-choices",\n    license="MIT",\n)\n\n# Validation fails\np1 = Project(\n    id="pydantic_choices",\n    url="https://github.com/vinissimus/pydantic-choices",\n    license="propietary",  # value not in choice\n)\n```\n',
    'author': 'Jordi Masip',
    'author_email': 'jordi@masip.cat',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vinissimus/pydantic-choices',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
