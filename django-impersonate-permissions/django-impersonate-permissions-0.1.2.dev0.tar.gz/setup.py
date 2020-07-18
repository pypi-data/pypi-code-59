# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impersonate_permissions', 'impersonate_permissions.migrations']

package_data = \
{'': ['*'], 'impersonate_permissions': ['templates/impersonate_permissions/*']}

install_requires = \
['django-impersonate>=1.5.1,<2.0.0', 'django>=2.2,<4.0']

setup_kwargs = {
    'name': 'django-impersonate-permissions',
    'version': '0.1.2.dev0',
    'description': 'Django app that tracks user permssions when using django-impersonate.',
    'long_description': '# Django Impersonate Permissions\n\nAdd ability to control impersonate permissions.\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/django-impersonate-permissions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
