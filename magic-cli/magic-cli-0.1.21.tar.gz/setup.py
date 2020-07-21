# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magic_cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.24.0,<3.0.0', 'typer[all]>=0.2.1,<0.3.0']

entry_points = \
{'console_scripts': ['magic = magic_cli.main:app']}

setup_kwargs = {
    'name': 'magic-cli',
    'version': '0.1.21',
    'description': '',
    'long_description': '# Magic CLI\n\nThe best server maker.\n\nSteps:\n\n1) pip install magic-cli (make sure the pip points to the correct python (3.6+))\n\n2) cd into the directory you want the server to be in\n\n// use the cli to create the app\n\n3) magic create < app name >\n\n4) cd < app name >\n\n// now make the virtual env and pip install the requirements\n5) python3 -m venv venv\n\n6) source venv/bin/activate\n\n7) pip install -r requirements.txt\n\n// files needed to run\n8) Create an .env file in the < app name > directory.\n\na) Use the ".example_env" as a template. Fill in the env variables for the services you will need to use.\n\nb) The SERVICE and TASKS_TABLE_NAME are required for the app.\n\n// add firestore\n1) add the firestore service account json to the < app name > and name it "my-service-account.json"\n\n\nThat should be it for the setup!\n\nTime to run it!\n\nTo start a local server: magic start\nTo test local server (while local server is running): magic test\nTo deploy for the first time or any time you change the serverless yaml: magic deploy\nTo deploy when you just edited the app code: magic deploy_again',
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
