# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['find_the_site']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.7.1,<5.0.0',
 'requests>=2.22,<3.0',
 'user-agent>=0.1.9,<0.2.0']

setup_kwargs = {
    'name': 'find-the-site',
    'version': '0.2',
    'description': 'Find the site in duckduckgo',
    'long_description': '[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/serhii73/find_the_site/graphs/commit-activity)\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n[![GitHub contributors](https://img.shields.io/github/contributors/serhii73/find_the_site.svg)](https://GitHub.com/serhii73/find_the_site/graphs/contributors/)\n[![GitHub stars](https://img.shields.io/github/stars/serhii73/find_the_site.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/serhii73/find_the_site/stargazers/)\n![GitHub forks](https://img.shields.io/github/forks/serhii73/find_the_site.svg?style=social)\n[![GitHub issues](https://img.shields.io/github/issues/serhii73/find_the_site.svg)](https://GitHub.com/serhii73/find_the_site/issues/)\n\n# find_the_site\n## Are you looking for a company/enterprise website? This small library finds websites in [duckduckgo search engine](https://duckduckgo.com/?t=hk)\n#### Optionally you can use:\n- the [ecosia](https://ecosia.org) search engine, to support environmental efforts\n##### How to Install ?\n\n```\npip install find_the_site\n```\n\n##### How to use ?\n\ndef get_website(website, eco=False)\n> **website**: Whose website you are searching for\n>\n> **eco**: \n>- **True**: Use ecosia search.\n>- **default**: **False**\n\n##### Find the website\n\n```\nIn [1]: from find_the_site.fw import get_website                                               \n\nIn [2]: get_website("UNITED NATIONS")                                                          \nOut[2]: \'https://www.un.org/en/\'\n```\n#\n```\nIn [1]: from find_the_site.fw import get_website \n\nIn [2]: get_website("UNITED NATIONS", eco=True)                                                          \nOut[2]: \'https://www.un.org/en/\'\n```\n',
    'author': 'serhii',
    'author_email': 'aserhii@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/serhii73/find_the_site',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
