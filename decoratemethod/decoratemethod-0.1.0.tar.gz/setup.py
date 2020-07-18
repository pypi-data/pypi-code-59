# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['decoratemethod']
setup_kwargs = {
    'name': 'decoratemethod',
    'version': '0.1.0',
    'description': 'Let function decorator decorate the bound method of per instance.',
    'long_description': '# decoratemethod-python\n\nLet function decorator decorate the bound method of per instance.\n\n## Examples\n\n### lru_cache\n\nTo make per instance has they own lru cache:\n\n``` py\nfrom functools import lru_cache\nfrom decoratemethod import decorate\n\nclass Foo:\n    @decorate(lru_cache)\n    def decorated_method(self, x):\n        ...\n```\n',
    'author': 'Cologler',
    'author_email': 'skyoflw@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cologler/decoratemethod-python',
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
