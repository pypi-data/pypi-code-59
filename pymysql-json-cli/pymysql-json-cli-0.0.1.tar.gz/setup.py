# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['src']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'pymysql>=0.9.3,<0.10.0']

entry_points = \
{'console_scripts': ['pymysql-json = src.main:cli']}

setup_kwargs = {
    'name': 'pymysql-json-cli',
    'version': '0.0.1',
    'description': 'pymysql wrapper for cli use',
    'long_description': '# pymysql-json-cli\n\n## install\n\n```sh\npip install pymysql-json-cli\n```\n\n## usage\n\n```sh\ncat << EOF |\nSHOW DATABASES;\nEOF\npymysql-json\n# [{"Database": "information_schema"}, {"Database": "test"}]\n```\n\n```sh\ncat <<EOF |\nSELECT *\nFROM %(table_name)s\nEOF\npymysql-json --args \'{"table_name": "test_table"}\'\n# [{"test_column": "arg_value"}, {"test_column": "test_value"}]\n```\n\n```sh\necho "SHOW DATABASES;" > db.sql\npymysql-json --sqlfile ./db.sql\n# [{"Database": "information_schema"}, {"Database": "test"}]\n```\n\n## development\n\n- Need\n  - cargo-make\n  - docker\n\n### lint & test\n\n```sh\nmakers --env-file .env.test tests\n```\n\n### lint except python code\n\n```sh\nmakers --env-file .env.test lints\n```',
    'author': 'watarukura',
    'author_email': 'what.r.j150@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/watarukura',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
