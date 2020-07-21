# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['labthings',
 'labthings.actions',
 'labthings.apispec',
 'labthings.core',
 'labthings.core.tasks',
 'labthings.default_views',
 'labthings.default_views.docs',
 'labthings.example_components',
 'labthings.json',
 'labthings.json.marshmallow_jsonschema',
 'labthings.semantics',
 'labthings.server',
 'labthings.server.semantics',
 'labthings.server.view',
 'labthings.sync',
 'labthings.views']

package_data = \
{'': ['*'], 'labthings.default_views.docs': ['static/*', 'templates/*']}

install_requires = \
['Flask>=1.1.1,<2.0.0',
 'apispec>=3.2.0,<4.0.0',
 'flask-cors>=3.0.8,<4.0.0',
 'flask-threaded-sockets>=0.2.0,<0.3.0',
 'marshmallow>=3.4.0,<4.0.0',
 'webargs>=6.0.0,<7.0.0',
 'zeroconf>=0.24.5,<0.29.0']

setup_kwargs = {
    'name': 'labthings',
    'version': '0.8.0rc1',
    'description': 'Python implementation of LabThings, based on the Flask microframework',
    'long_description': '# python-labthings\n\n[![LabThings](https://img.shields.io/badge/-LabThings-8E00FF?style=flat&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz4NCjxzdmcgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS1taXRlcmxpbWl0PSIyIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNjMgMTYzIiB4bWw6c3BhY2U9InByZXNlcnZlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xMjIuMjQgMTYyLjk5aDQwLjc0OHYtMTYyLjk5aC0xMDEuODd2NDAuNzQ4aDYxLjEyMnYxMjIuMjR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0ibTAgMTIuMjI0di0xMi4yMjRoNDAuNzQ4djEyMi4yNGg2MS4xMjJ2NDAuNzQ4aC0xMDEuODd2LTEyLjIyNGgyMC4zNzR2LTguMTVoLTIwLjM3NHYtOC4xNDloOC4wMTl2LTguMTVoLTguMDE5di04LjE1aDIwLjM3NHYtOC4xNDloLTIwLjM3NHYtOC4xNWg4LjAxOXYtOC4xNWgtOC4wMTl2LTguMTQ5aDIwLjM3NHYtOC4xNWgtMjAuMzc0di04LjE0OWg4LjAxOXYtOC4xNWgtOC4wMTl2LTguMTVoMjAuMzc0di04LjE0OWgtMjAuMzc0di04LjE1aDguMDE5di04LjE0OWgtOC4wMTl2LTguMTVoMjAuMzc0di04LjE1aC0yMC4zNzR6IiBmaWxsPSIjZmZmIi8+PC9zdmc+DQo=)](https://github.com/labthings/)\n[![ReadTheDocs](https://readthedocs.org/projects/python-labthings/badge/?version=latest&style=flat)](https://python-labthings.readthedocs.io/en/latest/)\n[![PyPI](https://img.shields.io/pypi/v/labthings)](https://pypi.org/project/labthings/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![codecov](https://codecov.io/gh/labthings/python-labthings/branch/master/graph/badge.svg)](https://codecov.io/gh/labthings/python-labthings)\n[![Riot.im](https://img.shields.io/badge/chat-on%20riot.im-368BD6)](https://riot.im/app/#/room/#labthings:matrix.org)\n\nA Python implementation of the LabThings API structure, based on the Flask microframework.\n\n## Installation\n\n`pip install labthings`\n\n## Quickstart example\n\nThis example assumes a `PretendSpectrometer` class, which already has `data` and `integration_time` attributes, as well as an `average_data(n)` method. LabThings allows you to easily convert this existing instrument control code into a fully documented, standardised web API complete with auto-discovery and automatic background task threading.\n\n```python\nfrom labthings import fields, create_app\nfrom labthings.example_components import PretendSpectrometer\n\n\n# Create LabThings Flask app\napp, labthing = create_app(\n    __name__,\n    title="My PretendSpectrometer API",\n    description="LabThing API for PretendSpectrometer",\n    version="0.1.0"\n)\n\n\n# Make some properties and actions out of our component\nmy_spectrometer = PretendSpectrometer()\n\n# Single-shot data property\nlabthing.build_property(\n    my_spectrometer,  # Python object\n    "data",  # Objects attribute name\n    description="A single-shot measurement",\n    readonly=True,\n    schema=fields.List(fields.Number())\n)\n\n# Integration time property\nlabthing.build_property(\n    my_spectrometer,  # Python object\n    "integration_time",  # Objects attribute name\n    description="A magic denoise property",\n    schema=fields.Int(min=100, max=500, example=200, unit="microsecond")\n)\n\n# Averaged measurement action\nlabthing.build_action(\n    my_spectrometer,  # Python object\n    "average_data",  # Objects method name\n    description="Take an averaged measurement",\n    schema=fields.List(fields.Number()),\n    args={  # How do we convert from the request input to function arguments?\n        "n": fields.Int(description="Number of averages to take", example=5, default=5)\n    },\n)\n\n\n# Start the app\nif __name__ == "__main__":\n    from labthings import Server\n    Server(app).run()\n```\n\n## Acknowledgements\n\nMuch of the code surrounding default response formatting has been liberally taken from [Flask-RESTful](https://github.com/flask-restful/flask-restful). The integrated [Marshmallow](https://github.com/marshmallow-code/marshmallow) support was inspired by [Flask-Marshmallow](https://github.com/marshmallow-code/flask-marshmallow) and [Flask-ApiSpec](https://github.com/jmcarp/flask-apispec). \n\n## Developer notes\n\n### Changelog generation\n\n* `npm install -g conventional-changelog-cli`\n* `conventional-changelog -r 0 --config ./changelog.config.js -i CHANGELOG.md -s`\n',
    'author': 'Joel Collins',
    'author_email': 'joel@jtcollins.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/labthings/python-labthings/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
