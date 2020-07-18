# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_help']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'discord-pretty-help',
    'version': '1.0.0',
    'description': 'And nicer looking interactive help menu for discord.py',
    'long_description': '![version](https://img.shields.io/pypi/v/discord-pretty-help) ![python](https://img.shields.io/badge/python-3.6+-blue)\n\n# discord-pretty-help\n\nAn embed version of the built in help command for discord.py\n\nBased on the DefaultHelpCommand that discord.py uses, but revised for embeds and cogs on individual pages that can be "scrolled" through with reactions.\n\n## Installation\n\n`pip install discord-pretty-help`\n\n## Usage\n\nExample of how to use it:\n\n```python\nfrom pretty_help import PrettyHelp\n\nbot = commands.Bot(command_prefix="!", help_command=PrettyHelp())\n```\n\n### Optional Args\n\n- `color` - Set the default embed color\n- `active` - Set the time (in seconds) that the message will be active default is 30s\n\nBy default, the help will just pick a random color on every invoke. You can change this using the `color` argument:\n\n```python\nfrom pretty_help import PrettyHelp\n\nbot = commands.Bot(command_prefix="!", help_command=PrettyHelp(color=discord.Color.dark_gold(), active=5)) #message will be active for 5s\n```\n\nThe basic `help` command will break commands up by cogs. Each cog will be a different page. Those pages can be navigated with\nthe arrow embeds. The message is unresponsive after 30s of no activity, it\'ll remove the reactions to let you know.\n\n![example](https://raw.githubusercontent.com/stroupbslayen/discord-pretty-help/master/images/example.gif)\n\n## Notes:\n\n- discord.py must already be installed to use this\n- `manage-messages` permission is recommended so reactions can be removed automatically\n',
    'author': 'StroupBSlayen',
    'author_email': '29642143+stroupbslayen@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stroupbslayen/discord-pretty-help',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
