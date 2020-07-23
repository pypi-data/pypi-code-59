# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swap_user']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.1']

setup_kwargs = {
    'name': 'django-swap-user',
    'version': '0.1.0b0',
    'description': '(Beta) Simple and flexible way to swap default Django User',
    'long_description': '# django-swap-user',
    'author': 'Artem Innokentiev',
    'author_email': 'artinnok@protonmail.com',
    'maintainer': 'Artem Innokentiev',
    'maintainer_email': 'artinnok@protonmail.com',
    'url': 'http://github.com/artinnok/django-swap-user',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
