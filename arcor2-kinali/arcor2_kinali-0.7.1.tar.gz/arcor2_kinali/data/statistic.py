from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class StatisticValue(JsonSchemaMixin):

    value: float
    created: int
