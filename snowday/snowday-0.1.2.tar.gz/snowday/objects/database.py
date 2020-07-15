from dataclasses import dataclass, field
from typing import List

from snowday.acl.privileges import DATABASE_PRIVILEGES, SCHEMA_PRIVILEGES
from snowday.objects.base import BaseSnowflakeObject
from snowday.objects.account import Share
from snowday.util import get_resource_type, settings_str_from


# https://docs.snowflake.com/en/sql-reference/sql/create.html


def get_fqn(db_schema_or_string):
    if isinstance(db_schema_or_string, str):
        return db_schema_or_string
    else:
        return db_schema_or_string.fqn


@dataclass
class Database(BaseSnowflakeObject):
    transient: bool = False
    comment: str = ""
    data_retention_time_in_days: int = 1
    default_ddl_collation: str = None

    @property
    def resource_type(self):
        if self.transient:
            return "transient database"
        return "database"


@dataclass
class DatabaseFromShare(BaseSnowflakeObject):
    provider_account: str
    share: Share

    @property
    def _settings_str(self):
        return f"from share {self.provider_account}.{self.share.name}"

    @property
    def resource_type(self):
        return "database"

    @property
    def create_or_replace(self):
        raise UnsupportedFeatureException(
            "Create or replace for snowflake database from share is unsupported."
        )

    @property
    def create_if_not_exists(self):
        raise UnsupportedFeatureException(
            "Create if not exists for snowflake database from share is unsupported."
        )


@dataclass
class DatabaseReplica(BaseSnowflakeObject):
    src_region_name: str
    src_account_name: str
    src_database_name: str
    auto_refresh_materialized_views: bool = False

    @property
    def _settings_str(self):
        return (
            f"as replica of {self.src_region_name}.{self.src_account_name}.{self.src_database_name} "
            f"auto_refresh_materialized_views_on_secondary={self.auto_refresh_materialized_views}"
        )

    @property
    def resource_type(self):
        return "database"

    @property
    def create_or_replace(self):
        raise UnsupportedFeatureException(
            "Create or replace for snowflake database replica is unsupported."
        )

    @property
    def create_if_not_exists(self):
        raise UnsupportedFeatureException(
            "Create if not exists for snowflake database replica is unsupported."
        )


# See: https://docs.snowflake.com/en/sql-reference/sql/create.html
@dataclass
class Schema(BaseSnowflakeObject):
    database: Database
    transient: bool = False
    with_managed_access: bool = False
    data_retention_time_in_days: int = 1
    default_ddl_collation: str = None
    comment: str = ""

    def __post_init__(self):
        self._available_privileges = SCHEMA_PRIVILEGES

    @property
    def resource_type(self):
        if self.transient:
            return "transient schema"
        return "schema"

    @property
    def fqn(self):
        return f"{self.database.name}.{self.name}"

    def _ddl_collation_string(self):
        if self.default_ddl_collation:
            return f"default_ddl_collation={self.default_ddl_collation} "
        else:
            return ""

    @property
    def _settings_str(self):
        return (
            f"{'with managed access ' if self.with_managed_access else ''}"
            f"data_retention_time_in_days={self.data_retention_time_in_days} "
            f"{self._ddl_collation_string()}"
            f"comment='{self.comment}'"
        )


@dataclass
class SchemaObject(BaseSnowflakeObject):
    schema: Schema
    comment: str

    @property
    def fqn(self):
        return f"{self.schema.fqn}.{self.name}"


# @dataclass
# class View(SchemaObject):
#     pass


# @dataclass
# class MaterializedView(SchemaObject):
#     pass


# @dataclass
# class FileFormatTypeOptions:
#     pass


# @dataclass
# class FileFormat(SchemaObject):
#     pass


# @dataclass
# class InternalStage(SchemaObject):
#     pass


# @dataclass
# class ExternalStage(SchemaObject):
#     pass


# @dataclass
# class Pipe(SchemaObject):
#     pass


# @dataclass
# class Stream(SchemaObject):
#     pass


# @dataclass
# class Function(SchemaObject):
#     pass


# @dataclass
# class Procedure(SchemaObject):
#     pass


# @dataclass
# class Sequence(SchemaObject):
#   pass
