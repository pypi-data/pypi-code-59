# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfmt']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dfmt = dfmt:main']}

setup_kwargs = {
    'name': 'dfmt',
    'version': '1.0.1',
    'description': '',
    'long_description': 'dfmt: format paragraphs, comments and doc strings\n=================================================\n\nOverview\n--------\n\ndfmt is a Python command line tool that can reformat text, allowing you to go from::\n\n  this is a pretty big sentence with lots of words that takes a lot of horizontal space\n\nto::\n\n  this is a pretty big sentence with lots\n  of words that takes a lot of horizontal\n  space\n\n\n\nIt can also be used to format paragraphs in comments and doc strings.\n\nInput::\n\n  /**\n   * This is a very long line in a Doxygen comment that takes a lot of space\n   */\n\nOutput::\n\n  /**\n   * This is a very long line in a\n   * Doxygen comment that takes a lot of\n   * space\n   */\n\nUsage\n-----\n\nSend the text to stdin, and dfmt will write the results to stdout.\n\nBy default, text is wrapped at 80 characters. You can use the\n`-w,--width` option to set a different size.\n\nAs such, ``dfmt`` can be used in a number of text editors.\n\n\nHow it works\n------------\n\ndfmt contains an hard-coded list of known prefixes.\n\nIt will start by splitting the input in "regions" that start with the same\nprefix.\n\nThen it will use the ``textwrap`` module from the Python standard library\nto wrap each region while keeping the existing prefix.\n\nIt is also a bit smarted than vim\'s ``gq`` commands, because it can\nkeep leading ``*`` in Doxygen comments for instance.\n',
    'author': 'Dimitri Merejkowsky',
    'author_email': 'd.merej@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dmerejkowsky/dfmt',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
