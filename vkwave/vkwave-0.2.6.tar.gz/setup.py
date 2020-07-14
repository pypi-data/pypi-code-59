# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vkwave',
 'vkwave.api',
 'vkwave.api.methods',
 'vkwave.api.token',
 'vkwave.bots',
 'vkwave.bots.addons',
 'vkwave.bots.addons.easy',
 'vkwave.bots.core',
 'vkwave.bots.core.dispatching',
 'vkwave.bots.core.dispatching.cast',
 'vkwave.bots.core.dispatching.dp',
 'vkwave.bots.core.dispatching.dp.middleware',
 'vkwave.bots.core.dispatching.events',
 'vkwave.bots.core.dispatching.extensions',
 'vkwave.bots.core.dispatching.extensions.callback',
 'vkwave.bots.core.dispatching.filters',
 'vkwave.bots.core.dispatching.handler',
 'vkwave.bots.core.dispatching.router',
 'vkwave.bots.core.tokens',
 'vkwave.bots.core.types',
 'vkwave.bots.fsm',
 'vkwave.bots.storage',
 'vkwave.bots.storage.storages',
 'vkwave.bots.utils',
 'vkwave.bots.utils.keyboards',
 'vkwave.bots.utils.uploaders',
 'vkwave.client',
 'vkwave.http',
 'vkwave.longpoll',
 'vkwave.streaming',
 'vkwave.types',
 'vkwave.vkscript',
 'vkwave.vkscript.handlers']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<4.0', 'pydantic>=1.4,<2.0', 'typing_extensions>=3.7.4,<4.0.0']

extras_require = \
{'all': ['aioredis>=1.3,<2.0'], 'storage-redis': ['aioredis>=1.3,<2.0']}

setup_kwargs = {
    'name': 'vkwave',
    'version': '0.2.6',
    'description': "Framework for building high-performance & easy to scale projects interacting with VK's API.",
    'long_description': '![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)\n\n> It\'s time to carry out vk_api & vkbottle. VKWave is here.\n\n[Русская версия](https://github.com/fscdev/vkwave/blob/master/readme_ru.md)\n\n[Why VKWave?](./why_vkwave.md)\n\n```python\nfrom vkwave.bots import SimpleLongPollBot\n\nbot = SimpleLongPollBot(tokens="MyToken", group_id=123456789)\n\n@bot.message_handler()\ndef handle(_) -> str:\n    return "Hello world!"\n\nbot.run_forever()\n\n```\n\n# What is it?\n\nFramework for building high-performance & easy to scale projects interacting with VK\'s API.\n\nIt\'s built over asyncio and Python\'s type hints. Minimal required version is `3.7`.\n\nOur Telegram chat - [let\'s chat](https://t.me/vkwave)\n\nCurrent maintainer of this project is [@kesha1225](https://github.com/kesha1225)\n\n## Installation\n\nInstall tested and stable version from PyPi:\n\n```\npip install vkwave\n```\n\nOr from GitHub but with the latest updates.\n```\npip install https://github.com/fscdev/vkwave/archive/master.zip\n```\n\n\n## Performance\n\nVKWave is not **the fastest**. It is because of our wish to make customizable and suitable for all kind of tasks library.\n\nBut we are always interested in improving performance, so feel free to make PRs and discuss performance problems.\n\n## Community\n\nVKWave is a young project.\n\n### Chat\n\nHow been mentioned earlier we have [the chat in Telegram](https://t.me/vkwave).\n\nThere is no chat in VK but you always is able to create your own and ever get a mention here.\n\n### Addons\n\nIf you want to create addon for VKWave (for example much easier way to write bots, like `vkwave.bots.addons.easy`) you should name your project like that: `vkwave-bots-really-easy`.\n\nThe general pattern for these things is `vkwave-<part-of-vkwave>-<name>`.\n\n',
    'author': 'prostomarkeloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fscdev/vkwave',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
