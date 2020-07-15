# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spanning_cidr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'spanning-cidr',
    'version': '0.1.4',
    'description': 'Function that accepts a sequence of IP addresses returning a single subnet that is large enough to span the lower and upper bound IP addresses with a possible overlap on either end.',
    'long_description': "## Spanning Cidr\n\nFunction that accepts a sequence of IP addresses returning a single subnet that is large enough to span the lower and upper bound IP addresses with a possible overlap on either end.\n\n### Installation\n\nRun `pip install spanning-cidr`\n\n### How To Use\n\n```Python\nfrom spanning_cidr import spanning_cidr\n\nspanning_cidr(['192.168.1.1','192.168.1.2', '192.168.1.3', '192.168.1.4'])\n>> '192.168.1.0/29'\n\nspanning_cidr(['192.168.2.10', '192.168.1.10'])\n>> '192.168.0.0/22'\n```\n",
    'author': 'Vitalii Shishorin',
    'author_email': 'moskrc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/moskrc/spanning-cidr/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
