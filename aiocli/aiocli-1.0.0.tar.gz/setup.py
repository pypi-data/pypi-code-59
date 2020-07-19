# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiocli']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiocli',
    'version': '1.0.0',
    'description': 'Simple and lightweight async console runner.',
    'long_description': '# Async Python application\n\naiocli is a Python library for simple and lightweight async console runner.\n\nFull compatibility with argparse module and highly inspired by aiohttp module.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install aiocli.\n\n```bash\npip install aiocli\n```\n\n## Usage\n\n```python\nfrom asyncio import get_event_loop, AbstractEventLoop\nfrom pyaioapp import AsyncApplication\nfrom aiocli.commander import Application, run_app, Command\nfrom typing import Dict as Container, Any\n\nSETTINGS = {\n    \'DEBUG\': \'0\', \'DEBUG_HOST\': \'0.0.0.0\', \'DEBUG_PORT\': \'5678\'\n}\n\n\nasync def get_container(settings: dict, **kwargs) -> Container:\n    async def hello_world_command(args: dict) -> int:\n        print(f\'Hello {args.get("name")}!\')\n        return 0\n\n    return {\n        \'hello_world_command\': hello_world_command\n    }\n\n\nasync def get_runner(container: Container) -> Application:\n    return Application([\n        Command(\n            name=\'hello:world\',\n            handler=container.get(\'hello_world_command\'),\n            optionals=[(\'--name\', {\'default\': \'World\'})],\n            positionals=[]\n        ),\n    ])\n\n\nclass CliApp(AsyncApplication[Container, Application]):\n    async def __aenter__(self) -> Application:\n        self._container = await get_container(SETTINGS, loop=self.loop)\n        self._runner = await get_runner(self._container)\n        return self._runner\n\n    def __call__(self) -> None:\n        run_app(app=self.__aenter__(), loop=self.loop)\n\n\ndef main(loop: AbstractEventLoop) -> Any:\n    if SETTINGS[\'DEBUG\'] == \'1\':\n        from ptvsd import enable_attach  # type: ignore\n        enable_attach(\n            address=(SETTINGS[\'DEBUG_HOST\'], int(SETTINGS[\'DEBUG_PORT\']))\n        )\n    return CliApp(loop).__call__()\n\n\nif __name__ == \'__main__\':\n    main(get_event_loop())\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://github.com/ticdenis/python-aiocli/blob/master/LICENSE)\n',
    'author': 'ticdenis',
    'author_email': 'denisnavarroalcaide@outlook.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ticdenis/python-aiocli',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
