# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kanp']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'httpx', 'uvicorn', 'youtube_dl']

entry_points = \
{'console_scripts': ['kanp = kanp.cli:cli']}

setup_kwargs = {
    'name': 'kanp',
    'version': '0.1.0',
    'description': 'See video with downloading by multithread',
    'long_description': "# Kanp\n\n![pypi](https://img.shields.io/pypi/v/kanp.svg?style=flat)\n![docker](https://img.shields.io/docker/cloud/build/long2ice/kanp)\n![license](https://img.shields.io/github/license/long2ice/kanp)\n![workflows](https://github.com/long2ice/kanp/workflows/pypi/badge.svg)\n![workflows](https://github.com/long2ice/kanp/workflows/ci/badge.svg)\n\n[中文文档](https://github.com/long2ice/kanp/blob/dev/README-zh.md)\n\n## Introduction\n\nSee video with downloading by multithread.\n\n## Install\n\n```shell\n> pip install kanp\n```\n\n## Usage\n\n```shell script\nUsage: kanp [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -V, --version  Show the version and exit.\n  -h, --help     Show this message and exit.\n\nCommands:\n  serve  Serve video server.\n  watch  Open video server url with webbrowser.\n```\n\n### Serve video server\n\n```shell script\nUsage: kanp serve [OPTIONS]\n\n  Serve video server.\n\nOptions:\n  --host TEXT         Video server host.  [default: 0.0.0.0]\n  -p, --port INTEGER  Video server port.  [default: 8000]\n  -h, --help          Show this message and exit.\n\n```\n\n```shell script\n> kanp serve\n```\n\nOr run with docker:\n\n```shell script\n> docker run -d -p 8000:8000 long2ice/kanp\n```\n\nAnd you will see:\n\n```log\nINFO:     Started server process [41254]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)\nCINFO:     Shutting down\nINFO:     Waiting for application shutdown.\nINFO:     Application shutdown complete.\nINFO:     Finished server process [41254]\n```\n\n### Watch video by web browser\n\n```shell script\nUsage: kanp watch [OPTIONS]\n\n  Open video server url with webbrowser.\n\nOptions:\n  -s, --server TEXT  [default: http://127.0.0.1:8000]\n  -u, --url TEXT     Video url or site url support by youtube-dl.  [required]\n  -y, --youtube-dl   Get real video url by youtube-dl.  [default: False]\n  -h, --help         Show this message and exit.\n```\n\n```shell script\n> kanp watch -u 'https://www.youtube.com/watch?v=WLVuUTUbhkw' -y\n```\n\nWill open browser automatically and play video.\n\nJust enjoy it with huge speed!\n\n## License\n\nThis project is licensed under the [Apache-2.0](https://github.com/long2ice/kanp/blob/master/LICENSE) License.\n",
    'author': 'long2ice',
    'author_email': 'long2ice@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/long2ice/kanp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
