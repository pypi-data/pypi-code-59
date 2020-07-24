# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snowday',
 'snowday.acl',
 'snowday.acl.grants',
 'snowday.connector',
 'snowday.graph',
 'snowday.objects',
 'snowday.types',
 'snowday.util']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.14.24,<2.0.0',
 'loguru>=0.5.1,<0.6.0',
 'networkx==2.4',
 'snowflake-connector-python==2.2.9']

setup_kwargs = {
    'name': 'snowday',
    'version': '0.1.3',
    'description': 'Tools for turning Snowflake into a Snow Day. ❄️',
    'long_description': '\nTools for turning [Snowflake](https://www.snowflake.com/) into a Snow Day. ❄️\n\nA little bit of sass with a whole lot of `@dataclass`.\n\n\n![Snowday](snowday.png)\n\n\n### Installation\n\n\n```\npip install snowday\n```\n\n\n### What does it do?\n\n#### Connector\n\n![Snowday Connector 1](readme_gif/conn1.gif)\n\n![Snowday Connector 2](readme_gif/conn2.gif)\n\n\n#### Objects\n\n![Snowday Objects 1](readme_gif/obj1.gif)\n\n![Snowday Objects 2](readme_gif/obj2.gif)\n\n\n#### All together now\n\n![Snowday All Together](readme_gif/alltogether.gif)\n\n\n### License\n\n\nSnowday is licensed under GPLv3.0.\n',
    'author': 'Jacob Thomas',
    'author_email': 'jake@bostata.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bostata/snowday',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
