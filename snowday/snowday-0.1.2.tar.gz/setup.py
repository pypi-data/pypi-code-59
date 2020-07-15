# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snowday',
 'snowday.acl',
 'snowday.acl.grants',
 'snowday.acl.privileges',
 'snowday.graph',
 'snowday.objects',
 'snowday.types',
 'snowday.util']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.4,<3.0']

setup_kwargs = {
    'name': 'snowday',
    'version': '0.1.2',
    'description': 'Tools for turning Snowflake into a Snow Day. ❄️',
    'long_description': '# snowday\n\nTools for turning [Snowflake](https://www.snowflake.com/) into a Snow Day ❄️.\n\n\n![Snowday](snowday.png)\n\n\n### Installation\n\n```\npip install snowday\n```\n\n\n### Usage\n\n\n\n### License\n\nSnowday is licensed under GPLv3.0.\n',
    'author': 'Jacob Thomas',
    'author_email': 'jake@bostata.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bostata/snowday',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
