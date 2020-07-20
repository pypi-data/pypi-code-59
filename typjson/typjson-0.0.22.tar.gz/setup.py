# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typ']

package_data = \
{'': ['*']}

install_requires = \
['typing_inspect>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'typjson',
    'version': '0.0.22',
    'description': 'Type-safe JSON (de)serialization',
    'long_description': '# typjson\n\nType-safe JSON (de)serialization for Python. Compatible with mypy type hints.\n\n## Requirements\n\n* Python 3.7 or newer\n\n## Features\n\n* Support for primitive types:\n    * `str`, `int`, `float`, `Decimal`, `bool`\n    * `date` as `"%Y-%m-%d"`, `datetime` as `"%Y-%m-%dT%H:%M:%S%z"`, `time` as `"%H:%M:%S"`\n    * `UUID` as `str` in format `"8-4-4-4-12"`\n* Support for None type and Optional type\n* Support for Union[] generic type\n* Structure types: List[], Tuple[], Dict[str, T]\n* Support for classes marked with `@dataclass`\n* Support for custom encoders and decoders\n\n## Simple Usage\n\n```python\nfrom typ import json\nfrom typing import *\nfrom datetime import date\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass Address:\n    street: str\n    house: int\n    apt: Optional[str]\n\n\n@dataclass\nclass Person:\n    first_name: str\n    last_name: str\n    languages: List[str]\n    address: Address\n    birth_date: date\n\n\nperson = Person(\n    "John",\n    "Smith",\n    ["English", "Russian"],\n    Address("Main", 1, "2A"),\n    date(year=1984, month=8, day=1)\n)\n\njson_str = json.dumps(person, indent=2)\nloaded_person = json.loads(Person, json_str)\n\nassert person == loaded_person\n```\n\nValue of `json_str` that is dumped and loaded in the code example above looks like:\n```json\n{\n  "first_name": "John",\n  "last_name": "Smith",\n  "languages": [\n    "English",\n    "Russian"\n  ],\n  "address": {\n    "street": "Main",\n    "house": 1,\n    "apt": "2A"\n  },\n  "birth_date": "1984-08-01"\n}\n```\n\n## API Overview\n\ntypjson API is similar to [json](https://docs.python.org/3/library/json.html) module. Main functions are defined in `typ.json` module. In fact `typ.json` functions are using `json` module under the hood for final conversion of python structures into JSON.\n\n### typ.json.dumps\n\n`typ.json.dumps(value: M, typ: Optional[Type[M]] = None, encoders: List[EncodeFunc] = [], indent: Optional[int] = None) -> str`\n\nSerialize value to a JSON formatted str using specified type.\n\n`value` Python object to be serialized to JSON.\n\n`typ` type information for `value`. If `None` is provided then actual type of `value` is used otherwise `value` is checked to be valid instance of `typ`.\n\n`encoders` list of custom encoders, see [custom encoding](#custom-encoding).\n\n`indent` optional non-negative indent level for JSON. If `None` is provided then JSON is represented as single line without indentation.\n\nReturns JSON string or raises `JsonError`.\n\n### typ.json.dump\n\n`typ.json.dump(fp: IO[str], value: M, typ: Optional[Type[M]] = None, encoders: List[EncodeFunc] = [], indent: Optional[int] = None)`\n\nSerialize value as a JSON formatted stream.\n\n`fp` stream to write JSON to.\n\nOther arguments have the same meaning as in [typ.json.dumps](#typ-json-dumps).\n\n### typ.json.loads\n\n`typ.json.loads(typ: Type[M], json_str: str, decoders: List[DecodeFunc] = []) -> M`\n\nDeserialize json_str to a Python object of specified type.\n\n`typ` type to deserialize JSON into.\n\n`json_str` string containing JSON.\n\n`decoders` list of custom decoders, see [custom encoding](#custom-encoding).\n\nReturns instance of `M` or raises `JsonError`.\n\n### typ.json.load\n\n`typ.json.load(fp: IO[str], typ: Type[M], decoders: List[DecodeFunc] = []) -> M`\n\nDeserialize stream to a Python object of specified type.\n\n`fp` stream to read JSON from.\n\nOther arguments have the same meaning as in [typ.json.loads](#typ-json-loads)\n\n## Supported Types\n\n## Custom Encoding\n',
    'author': 'Vladimir Sapronov',
    'author_email': 'vladimir.sapronov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
