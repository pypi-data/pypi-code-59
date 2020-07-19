# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_webhooks']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2,<4.0']

extras_require = \
{'black': ['black>=19.10b0,<20.0'],
 'dev': ['tox<3.8',
         'pytest>=5.2,<6.0',
         'pytest-django>=3.9.0,<4.0.0',
         'pytest-cov>=2.1.0,<3.0.0',
         'sphinx>=3,<4',
         'black>=19.10b0,<20.0',
         'isort[pyproject]>=5.1.2,<6.0.0'],
 'docs': ['sphinx>=3,<4'],
 'isort': ['isort[pyproject]>=5.1.2,<6.0.0'],
 'test': ['pytest>=5.2,<6.0',
          'pytest-django>=3.9.0,<4.0.0',
          'pytest-cov>=2.1.0,<3.0.0']}

setup_kwargs = {
    'name': 'django-gitlab-webhooks',
    'version': '1.0.0',
    'description': 'Gitlab webhooks for Django.',
    'long_description': 'django-gitlab-webhooks\n=======================================================================\n\n.. image:: https://github.com/OpenWiden/django-gitlab-webhooks/workflows/Tests/badge.svg?branch=master\n    :target: https://github.com/OpenWiden/django-gitlab-webhooks/actions\n    :alt: Build\n\n.. image:: https://codecov.io/gh/OpenWiden/django-gitlab-webhooks/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/OpenWiden/django-gitlab-webhooks\n    :alt: Coverage\n\n.. image:: https://readthedocs.org/projects/django-gitlab-webhooks/badge/?version=latest\n    :target: https://django-gitlab-webhooks.readthedocs.io/en/latest/?badge=latest\n    :alt: Docs\n\nGitlab webhooks for Django.\n\nDocs: https://django-gitlab-webhooks.readthedocs.io/en/latest/\n',
    'author': 'stefanitsky',
    'author_email': 'stefanitsky.mozdor@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/OpenWiden/django-gitlab-webhooks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
