from datetime import date, datetime
from dataclasses import dataclass, field
import json
from typing import List, Union
from snowday.objects.database import SchemaObject
from snowday.exceptions import (
    InvalidWhitespaceException,
    InvalidColumnConstraintException,
)


QUOTEWRAPPED_COLS = [
    "varchar",
    "char",
    "string",
    "text",
    "binary",
    "varbinary",
    "variant",
    "object",
    "array",
    "geography",
]


def get_default_sql(obj): -> str
    if hasattr(obj, "default"):
        if obj.default == False:  # Has to be first because... false is falsey
            return f" default {obj.default}"
        if obj.default:  # But `None` should be politely excused
            if obj.datatype in ["varchar", "char", "string", "text"]:
                return f" default '{obj.default}'"
            elif obj.datatype == "boolean":
                return f" default {obj.default}"
            elif obj.datatype == "date":
                return f" default cast('{obj.default}' as date)"
            elif obj.datatype in ["datetime", "timestamp", "timestamp_ntz"]:
                return f" default cast('{obj.default}' as timestamp_ntz(9))"
            elif obj.datatype == "time":
                return f" default cast('{obj.default}' as time(9))"
            elif obj.datatype == "timestamp_ltz":
                return f" default cast('{obj.default}' as timestamp_ltz(9))"
            elif obj.datatype == "timestamp_tz":
                return f" default cast('{obj.default}' as timestamp_tz(9))"
            elif obj.datatype == "variant":
                return f" default parse_json('{json.dumps(obj.default)}')"
            elif obj.datatype == "object":
                return f" default parse_json('{json.dumps(obj.default)}')"
            elif obj.datatype == "array":
                return f" default parse_json('{json.dumps(obj.default)}')"
            return f" default {obj.default}"
    return ""


@dataclass
class Column:
    """A base class for abstracting up sql consistencies.
    """

    name: str
    comment: str = None
    # inline constraints
    unique: bool = False
    not_null: bool = False
    # foreign_key: Column  # FIXME! do this!

    def __post_init__(self):
        # Make sure columns don't have whitespace.
        if " " in self.name:
            msg = f"Column names cannot have whitespace. Please change column name {self.name} to {self.name.replace(' ', '_')} or equivalent."
            raise InvalidWhitespaceException(msg)
        # Make sure columns don't have both a unique constraint and a column default.
        if hasattr(self, "default"):
            if self.default and self.unique:
                raise InvalidColumnConstraintException(
                    "A column cannot have both a default and a unique constraint. Please alter one or the other."
                )

    @property
    def datatype(self):
        return "column"

    @property
    def datatype_modifier(self):
        return ""

    @property
    def unique_sql(self):
        if self.unique:
            return " unique"
        return ""

    @property
    def not_null_sql(self):
        if self.not_null:
            return " not null"
        return ""

    @property
    def collation_sql(self):
        # FIXME! Incorporate this functionality
        return ""

    # @property
    # def primary_key_sql(self): # FIXME! do this!
    #     if self.primary_key:
    #         return " primary key "
    #     return ""

    # @property
    # def foreign_key_sql(self): # FIXME! do this!
    #     if self.foreign_key

    @property
    def default_sql(self):
        return get_default_sql(self)

    @property
    def comment_sql(self):
        if self.comment:
            return f" comment '{self.comment}'"
        return ""

    @property
    def sql(self):
        return f"{self.name} {self.datatype}{self.datatype_modifier}{self.collation_sql}{self.default_sql}{self.not_null_sql}{self.unique_sql}{self.comment_sql}"


@dataclass
class BaseNumberColumn(Column):
    default: float = None
    precision: int = 38
    scale: int = 0

    @property
    def datatype(self):
        return "number"

    @property
    def datatype_modifier(self):
        return f"({self.precision}, {self.scale})"


@dataclass
class BaseIntColumn(Column):
    default: int = None

    @property
    def datatype(self):
        return "integer"


@dataclass
class BaseFloatingPointColumn(Column):
    default: float = None

    @property
    def datatype(self):
        return "float"


@dataclass
class BaseTextColumn(Column):
    default: str = None

    @property
    def datatype(self):
        return "text"


@dataclass
class BaseDateColumn(Column):
    default: date = None

    @property
    def datatype(self):
        return "date"


@dataclass
class BaseDatetimeColumn(Column):
    default: datetime = None

    @property
    def datatype(self):
        return "datetime"


# Numeric Columns


@dataclass
class NumberColumn(BaseNumberColumn):
    default: float = None

    @property
    def datatype(self):
        return "number"


@dataclass
class DecimalColumn(BaseNumberColumn):
    default: float = None

    @property
    def datatype(self):
        return "decimal"


@dataclass
class NumericColumn(BaseNumberColumn):
    default: float = None

    @property
    def datatype(self):
        return "numeric"


# Fixed precision/scale


@dataclass
class IntColumn(BaseIntColumn):
    @property
    def datatype(self):
        return "int"


@dataclass
class BigIntColumn(BaseIntColumn):
    @property
    def datatype(self):
        return "bigint"


@dataclass
class SmallIntColumn(BaseIntColumn):
    @property
    def datatype(self):
        return "smallint"


@dataclass
class TinyIntColumn(BaseIntColumn):
    @property
    def datatype(self):
        return "tinyint"


@dataclass
class ByteIntColumn(BaseIntColumn):
    @property
    def datatype(self):
        return "byteint"


@dataclass
class FloatColumn(BaseFloatingPointColumn):
    @property
    def datatype(self):
        return "float"


@dataclass
class Float4Column(BaseFloatingPointColumn):
    @property
    def datatype(self):
        return "float4"


@dataclass
class Float8Column(BaseFloatingPointColumn):
    @property
    def datatype(self):
        return "float8"


@dataclass
class DoubleColumn(BaseFloatingPointColumn):
    @property
    def datatype(self):
        return "double"


@dataclass
class RealColumn(BaseFloatingPointColumn):
    @property
    def datatype(self):
        return "real"


# Text Columns


@dataclass
class VarcharColumn(BaseTextColumn):
    length: int = 16777216

    @property
    def datatype(self):
        return "varchar"

    @property
    def datatype_modifier(self):
        return f"({self.length})"


@dataclass
class CharColumn(BaseTextColumn):
    @property
    def datatype(self):
        return "char"


@dataclass
class StringColumn(BaseTextColumn):
    length: int = 16777216

    @property
    def datatype(self):
        return "string"

    @property
    def datatype_modifier(self):
        return f"({self.length})"


@dataclass
class TextColumn(BaseTextColumn):
    length: int = 16777216

    @property
    def datatype(self):
        return "text"

    @property
    def datatype_modifier(self):
        return f"({self.length})"


@dataclass
class BinaryColumn(BaseTextColumn):
    @property
    def datatype(self):
        return "binary"


@dataclass
class VarbinaryColumn(BaseTextColumn):
    @property
    def datatype(self):
        return "varbinary"


# Logical Columns
@dataclass
class BooleanColumn(Column):
    default: bool = None

    @property
    def datatype(self):
        return "boolean"


# Date & Time Columns
@dataclass
class DateColumn(BaseDateColumn):
    @property
    def datatype(self):
        return "date"


@dataclass
class DatetimeColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "datetime"


@dataclass
class TimeColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "time"


@dataclass
class TimestampColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "timestamp"


@dataclass
class TimestampLTZColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "timestamp_ltz"


@dataclass
class TimestampNTZColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "timestamp_ntz"


@dataclass
class TimestampTZColumn(BaseDatetimeColumn):
    @property
    def datatype(self):
        return "timestamp_tz"


# Semi-structured Columns
@dataclass
class VariantColumn(Column):
    default: Union[list, dict] = None

    @property
    def datatype(self):
        return "variant"


@dataclass
class ObjectColumn(Column):
    default: dict = None

    @property
    def datatype(self):
        return "object"


@dataclass
class ArrayColumn(Column):
    default: list = None

    @property
    def datatype(self):
        return "array"


# Geospatial Columns
@dataclass
class GeographyColumn(Column):
    default: Union[
        dict, str
    ] = None  # FIXME: string must be in WKT, WKB, EWKT, EWKB format

    @property
    def datatype(self):
        return "geography"


ACCEPTED_TABLE_COLUMNS = Union[
    NumberColumn,
    IntColumn,
    BigIntColumn,
    SmallIntColumn,
    TinyIntColumn,
    ByteIntColumn,
    FloatColumn,
    Float4Column,
    Float8Column,
    DoubleColumn,
    RealColumn,
    VarcharColumn,
    CharColumn,
    StringColumn,
    TextColumn,
    BooleanColumn,
    DateColumn,
    DatetimeColumn,
    TimeColumn,
    TimestampColumn,
    TimestampLTZColumn,
    TimestampNTZColumn,
    TimestampTZColumn,
    VariantColumn,
    ObjectColumn,
    ArrayColumn,
    GeographyColumn,
]


@dataclass
class Table(SchemaObject):
    name: str
    columns: List[ACCEPTED_TABLE_COLUMNS] = None
    cluster_keys: List[ACCEPTED_TABLE_COLUMNS] = None

    def __post_init__(self):
        for column in self.columns:
            setattr(self, f"_{column.name}", column)

    @property
    def resource_type(self):
        return "table"

    @property
    def _definition_sql(self):
        col_sql = ", ".join(c.sql for c in self.columns)
        return f"({col_sql})"

    @property
    def create(self):
        return f"create {self.resource_type} {self.fqn} {self._definition_sql};"

    @property
    def create_if_not_exists(self):
        return f"create {self.resource_type} if not exists {self.fqn} {self._definition_sql};"

    @property
    def create_or_replace(self):
        return (
            f"create or replace {self.resource_type} {self.fqn} {self._definition_sql};"
        )
