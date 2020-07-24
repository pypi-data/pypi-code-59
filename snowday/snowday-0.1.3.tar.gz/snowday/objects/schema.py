from dataclasses import dataclass, field
from typing import List

from snowday.objects.base import BaseSnowflakeObject
from snowday.objects.database import Schema


@dataclass
class SchemaObject(BaseSnowflakeObject):
    schema: Schema
    comment: str

    @property
    def fqn(self):
        return f"{self.schema.fqn}.{self.name}"


@dataclass
class Integration(SchemaObject):
    pass


@dataclass
class Stage(SchemaObject):
    pass


@dataclass
class Task(SchemaObject):
    pass


@dataclass
class View(SchemaObject):
    pass


@dataclass
class MaterializedView(SchemaObject):
    pass


@dataclass
class MaskingPolicy(SchemaObject):
    pass


@dataclass
class FileFormatTypeOptions:
    pass


@dataclass
class FileFormat(SchemaObject):
    pass


@dataclass
class InternalStage(SchemaObject):
    pass


@dataclass
class ExternalStage(SchemaObject):
    pass


@dataclass
class Pipe(SchemaObject):
    pass


@dataclass
class Stream(SchemaObject):
    pass


@dataclass
class Function(SchemaObject):
    pass


@dataclass
class Procedure(SchemaObject):
    pass


@dataclass
class Sequence(SchemaObject):
    pass
