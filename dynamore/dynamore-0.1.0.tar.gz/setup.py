# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynamore']

package_data = \
{'': ['*']}

install_requires = \
['boto3==1.12.32', 'jsonschema>=3.2.0,<4.0.0', 'python-dotenv>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'dynamore',
    'version': '0.1.0',
    'description': 'Dynamore is extremely simple Python library for managing entities on DynamoDb.',
    'long_description': 'DYNAMORE\n--------\n\nDynamore is extremely simple Python library for **managing entities** on DynamoDb. It\'s designed to be used together with REST API and only supports **single table design**.\n\nInstallation\n------------\n\nInstall from Pypi:\n\n.. code-block:: bash\n\n   $ pip install dynamore\n\nQuick start\n-----------\n\nDynamore doesn\'t manage your tables so create DynamoDb table beforehand e.g. provisioning by CloudFormation.\n\nHere\'s the simple example on how to create Person schema and store it to DynamoDb:\n\n.. code-block:: Python\n\n    from dynamore.dynamodb_proxy import DynamoDbProxy\n    from dynamore.entity import Entity\n\n\n    class Person(Entity):\n        SCHEMA = {\n            "title": "PERSON",\n            "type": "object",\n            "required": ["name", "age", "gender", "id_number"],\n            "properties": {\n                "name": {"type": "string"},\n                "age": {"type": "integer", "min": 0, "max": 123},\n                "gender": {"type": "string", "enum": ["male", "female"]},\n                "id_number": {"type": "string"},\n            },\n            "additionalProperties": False,\n        }\n\n        ID_ATTRIBUTE = "id_number"\n\n    db = DynamoDbProxy(table_name="MyTable")\n    data = {\n        "name": "Jeanne",\n        "age": 123,\n        "gender": "female", \n        "id_number": "123456"\n    }\n    _ = db.post(entity_class=Person, data=data)\n    # Get single item\n    item = db.get(\n        entity_class=Person, data={"id_number": data["id_number"]}\n    )\n    # Get all items of type "Person"\n    items = dynamodb_proxy.get(entity_class=Person)\n\nFirst a new entity class Person defined. It\'s **schema** is defined using jsonschema and **id attribute** defines the name of the attribute that is used for uniqueness.\n\nDynamore stores data to DynamoDb in the following format:\n\n+--------+--------+--------+-----+--------+\n| PK     | SK     | name   | age | gender |\n+========+========+========+=====+========+\n| PERSON | 123456 | Jeanne | 123 | female | \n+--------+--------+--------+-----+--------+\n\nBy default entity uses partition key "PK" and sort key "SK" value but you can define them otherwise by overriding pr_keys-method.',
    'author': 'Ville Kärkkäinen',
    'author_email': 'ville.karkkainen@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/villekr/dynamore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
