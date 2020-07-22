# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['flask_github_webhook']
install_requires = \
['github-webhook>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'flask-github-webhook',
    'version': '0.2.0',
    'description': 'Flask extension for github-webhooks',
    'long_description': "# Flask-Github-Webhook\n\n[![Build Status](https://travis-ci.org/shawalli/flask-github-webhook.svg?branch=master)](https://travis-ci.org/shawalli/flask-github-webhook)\n[![Coverage Status](https://coveralls.io/repos/github/shawalli/flask-github-webhook/badge.svg?branch=master)](https://coveralls.io/github/shawalli/flask-github-webhook?branch=master)\n\nFlask-Github-Webhook adds extension support for GitHub webhooks to Flask. This extension primarily extends the [python-github-webhook](https://github.com/bloomberg/python-github-webhook) project by making the [Flask Extension Pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/#factories-extensions) available as an initialization option.\n\n## Initialization\nThe Github-Webhook Extension may be initialized directly or as an extension:\n\n**Direct Setup**\n```\nfrom flask import Flask\nfrom flask_github_webhook import GithubWebhook\n\napp = Flask(__name__)\nwebhook = GithubWebhook(app)\n```\n\n**Extension Setup**\n```\nfrom flask import Flask\n\n# The extension may be initialized from anywhere in the project, including\n# inside this file, by calling GithubWebhook()\nfrom .extension import WEBHOOK\n\napp = Flask(__name__)\nWEBHOOK.init_app(app)\n```\n\n## Usage\nThe extension may be used in the same manner as `python-github-webhook`.\n```\nfrom .extension import WEBHOOK\n\n@WEBHOOK.hook()\ndef push_handler(data):\n    print('Received the following PUSH event:{}'.format(data))\n\n@WEBHOOK.hook(event_type='pull_request')\ndef pullrequest_handler(data):\n    print('Received the following PULL-REQUEST event:{}'.format(data))\n```\n\n## Versions\nVersion 0.1.x supports `^2.7` and `^3.4`.\n\nVersions 0.2+ supports `^3.6.7`. This is primarily due to Python version\nconstraints on the package and test tools. For instance, here are some\ndependencies and their supported Python versions: `poetry=^3.4`,\n`coveralls=^3.5`, `pre-commit=^3.6.1`, and `pytest=^3.6`. Due to these\nconstraints, the decision was made to drop official support for `2.7`, `3.4`\nand `3.5`. However, `flask-github-webhook=^0.1.x` should work for older\nPython versions.\n\n## Configuration\nThe extension has the same configurations available as the `python-github-webhook` package. However, unlike referenced package, this extension reads those configurations from the Flask application, not initialization arguments. The values below should be configured in the Flask application (app.config) prior to initializing the extension.\n\n### GITHUB_WEBHOOK_ENDPOINT\nThis setting declares the route that all webhook event handlers will use. If left unset, the setting will default to the endpoint as declared in `python-github-webook`. As of this writing, the default endpoint is `/postreceive`.\n\n### GITHUB_WEBHOOK_SECRET\nIf provided, this setting's value should match the secret set in the GitHub repository from which this extension will receive webhooks.\n\n## Contributing\nContributions are welcomed! If you would like to improve or modify Flask-Github-Webhook, please follow these steps:\n1. Fork this repository.\n2. Make your changes and create a pull request.\n3. Ensure that all status checks are passing.\n\n## Author & License\nThis package is released under an open source MIT License. Flask-Github-Webhook was originally written by [Shawn Wallis](https://github.com/shawalli).\n\n## References\n* [python-github-webhook](https://github.com/bloomberg/python-github-webhook)\n* [GitHub Webhook Development Guide](https://developer.github.com/webhooks)\n* [Flask Extension Pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/#factories-extensions)\n",
    'author': 'Shawn Wallis',
    'author_email': 'shawn.p.wallis@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shawalli/flask-github-webhook',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6.7,<4.0.0',
}


setup(**setup_kwargs)
