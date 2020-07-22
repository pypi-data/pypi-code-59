# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_mod_auth_gssapi']

package_data = \
{'': ['*']}

install_requires = \
['flask>=1.1,<2.0', 'gssapi>=1.6.2,<2.0.0']

setup_kwargs = {
    'name': 'flask-mod-auth-gssapi',
    'version': '0.1.0',
    'description': "A Flask extention to make use of the authentication provided by the mod_auth_gssapi extention of Apache's HTTPd.",
    'long_description': "# Flask Mod Auth GSSAPI\n\n\nA Flask extention to make use of the authentication provided by the\nmod_auth_gssapi extention of Apache's HTTPd.\n",
    'author': 'Fedora Infrastructure',
    'author_email': 'admin@fedoraproject.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedora-infra/flask-mod-auth-gssapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
