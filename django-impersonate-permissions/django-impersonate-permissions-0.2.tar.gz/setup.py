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
    'version': '0.2',
    'description': 'Django app that tracks user permssions when using django-impersonate.',
    'long_description': "# Django Impersonate Permissions\n\nAdd ability to control impersonate permissions.\n\nImpersonate is a powerful Django app that allow site admins to log in to a user's account, and take\nactions on their behalf. This can be invalulable in providing technical support. However, with great\npower comes great responsiblity, and operationally you should **never** impersonate a user without\ntheir explicit consent.\n\nThis app provides a mechanism for recording user consent, and enforcing it.\n",
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
