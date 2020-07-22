# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_unicorn',
 'django_unicorn.management.commands',
 'django_unicorn.templatetags']

package_data = \
{'': ['*'],
 'django_unicorn': ['static/img/*',
                    'static/js/.babelrc',
                    'static/js/.babelrc',
                    'static/js/.babelrc',
                    'static/js/.babelrc',
                    'static/js/.babelrc',
                    'static/js/0.1.0/*',
                    'static/js/debounce.js',
                    'static/js/debounce.js',
                    'static/js/debounce.js',
                    'static/js/debounce.js',
                    'static/js/debounce.js',
                    'static/js/morphdom/2.6.1/morphdom-livewire.js',
                    'static/js/morphdom/2.6.1/morphdom-livewire.js',
                    'static/js/morphdom/2.6.1/morphdom-livewire.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.min.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.min.js',
                    'static/js/morphdom/2.6.1/morphdom-umd.min.js',
                    'static/js/unicorn.js',
                    'static/js/unicorn.js',
                    'static/js/unicorn.js',
                    'static/js/unicorn.js',
                    'static/js/unicorn.js',
                    'static/js/unicorn.min.js',
                    'static/js/unicorn.min.js',
                    'static/js/unicorn.min.js',
                    'static/js/unicorn.min.js',
                    'static/js/unicorn.min.js',
                    'static/js/utils.js',
                    'static/js/utils.js',
                    'static/js/utils.js',
                    'static/js/utils.js',
                    'static/js/utils.js',
                    'templates/unicorn/*']}

install_requires = \
['beautifulsoup4>=4.9.1,<5.0.0', 'django>=3.0.0', 'orjson>=3.2.1,<4.0.0']

setup_kwargs = {
    'name': 'django-unicorn',
    'version': '0.1.0',
    'description': 'Magical fullstack framework for Django.',
    'long_description': None,
    'author': 'Adam Hill',
    'author_email': 'unicorn@adamghill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
