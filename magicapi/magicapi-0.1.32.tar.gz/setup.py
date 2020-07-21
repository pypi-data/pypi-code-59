# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magicapi',
 'magicapi.Decorators',
 'magicapi.Errors',
 'magicapi.FieldTypes',
 'magicapi.Globals',
 'magicapi.Models',
 'magicapi.RouteClasses',
 'magicapi.Services',
 'magicapi.Services.Doorman',
 'magicapi.Services.Email',
 'magicapi.Services.MagicLink',
 'magicapi.Services.Mailgun',
 'magicapi.Services.Segment',
 'magicapi.Services.Stripe',
 'magicapi.Services.Twilio',
 'magicapi.Utils']

package_data = \
{'': ['*']}

install_requires = \
['analytics-python>=1.2.9,<2.0.0',
 'boto3>=1.14.23,<2.0.0',
 'fastapi[all]>=0.59.0,<0.60.0',
 'magicdb>=0.0.6,<0.0.7',
 'mangum>=0.9.2,<0.10.0',
 'phonenumbers>=8.12.6,<9.0.0',
 'pydantic[dotenv]>=1.6.1,<2.0.0',
 'requests>=2.24.0,<3.0.0',
 'stripe>=2.49.0,<3.0.0',
 'twilio>=6.44.0,<7.0.0',
 'typer>=0.3.1,<0.4.0']

entry_points = \
{'console_scripts': ['magic = magicapi.cli:app']}

setup_kwargs = {
    'name': 'magicapi',
    'version': '0.1.32',
    'description': '',
    'long_description': '# Magic API\n\nThe Magic API!\n\n1) incr the toml version\n2) poetry publish --build',
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jerber/MagicAPI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
