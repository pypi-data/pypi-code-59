# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['polyjuice']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2.0,<2.3.0', 'sqlalchemy>=1.3.0,<1.4.0']

setup_kwargs = {
    'name': 'polyjuice',
    'version': '0.1.0',
    'description': 'SQLAlchemy tables disguised as Django models.',
    'long_description': '# Polyjuice ⚗️🧙\u200d♂️\n\nSQLAlchemy tables disguised as Django models.\n\n[![Build Status](https://api.travis-ci.org/ducdetronquito/polyjuice.svg?branch=master)](https://travis-ci.org/ducdetronquito/polyjuice) [![License](https://img.shields.io/badge/license-public%20domain-ff69b4.svg)](https://github.com/ducdetronquito/polyjuice#license)\n\n\n## Usage\n\n*Polyjuice* allows you to define your database tables with [SQLAlchemy Core](https://docs.sqlalchemy.org/en/13/core/) and use them\nas legit Django models.\n\nYou could find *Polyjuice* relevant in situations where you want manage your table without the Django constraints, but still\ntake advantage of all the goodness of Django integration and tooling when needed.\n\nI haven\'t tried every use case yet, but I imagine it could suits many:\n\n- Use other database management tools (ex: migrations with [alembic](https://github.com/sqlalchemy/alembic))\n- Take advantage of the async world (ex: build RabbitMQ consummers with [aio-pika](https://github.com/mosquito/aio-pika))\n- Build complex SQL queries with the SQLAlchemy API and execute them through the Django database connection\n- Transition to another web framework\n- ¯\\\\_(ツ)_/¯\n\n\n### Example\n\n**In an python package called `my_tables.py`**\n\n```python\n"""Here, define your table schemas with the SQLAlchemy core API."""\nimport polyjuice\nfrom sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table\n\nmetadata = MetaData()\n\n\nProfessorTable = Table(\n    "hogwarts__professor",\n    metadata,\n    Column("id", Integer, primary_key=True),\n    Column("name", String(30), nullable=False)\n)\n\n\nPotionTable = Table(\n    \'hogwarts__potion\',\n    metadata,\n    Column("id", Integer, primary_key=True),\n    Column("name", String(100), nullable=False),\n    Column(\n        \'made_by\',\n        Integer,\n        ForeignKey(ProfessorTable.c.id),\n        django_on_delete="CASCADE",\n        django_related_name="personal_potions"\n    )\n)\n```\n\n**In your Django project**\n\n```python\nfrom my_tables import PotionTable, ProfessorTable\nimport polyjuice\n\n\n@polyjuice.mimic(ProfessorTable)\nclass Professor:\n    """The Polyjuice decorator will turn this class into a legit Django model."""\n\n    def welcome(self):\n        print(f"Welcome to my class, I am Pr. {self.name} 🧙\u200d♂️")\n\n\n@polyjuice.mimic(PotionTable)\nclass Potion:\n    """This class too"""\n\n    def boil(self):\n        print(f"*The {self.name} potion is blurping* ⚗️")\n\n\n# And you are ready to go !\nseverus_snape = Professor.objects.create(name="Severus Snape")\nveritaserum = Professor.objects.create(name="Veritaserum", made_by=severus_snape)\n\nassert severus_snape.personal_potions.count() == 1\n```\n\n\n## Requirements\n\n*Polyjuice* is currently built on top of SQLAlchemy 1.3 and Django 2.2, and requires Python 3.6.\n\n\n## License\n\n*Polyjuice* is released into the Public Domain. 🎉🍻\n',
    'author': 'ducdetronquito',
    'author_email': 'guillaume.paulet@giome.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ducdetronquito/polyjuice',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
