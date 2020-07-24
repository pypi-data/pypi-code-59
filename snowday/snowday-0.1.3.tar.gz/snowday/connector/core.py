import atexit
from contextlib import contextmanager
from typing import Union, Iterator

import snowflake.connector as sf_connector

from snowday.logger import get_logger
from snowday.objects.account import (
    Account,
    ManagedAccount,
    AwsApiIntegration,
    NetworkPolicy,
    ResourceMonitor,
    Share,
    Warehouse,
    Role,
    User,
    AzureNotificationIntegration,
    SecurityIntegrationOAuth,
    SecurityIntegrationOAuthPartnerApp,
    SecurityIntegrationOAuthCustom,
    SecurityIntegrationSAML2,
    SecurityIntegrationSCIM,
    StorageIntegrationS3,
    StorageIntegrationGCS,
    StorageIntegrationAzure,
)
from snowday.objects.database import (
    Database,
    DatabaseFromShare,
    DatabaseReplica,
    Schema,
)
from snowday.objects.schema import (
    Integration,
    Stage,
    Task,
    View,
    MaterializedView,
    MaskingPolicy,
    FileFormat,
    InternalStage,
    ExternalStage,
    Pipe,
    Stream,
    Function,
    Procedure,
    Sequence,
)
from snowday.objects.table import Table

LOG = get_logger()

ALL_OBJS = Union[
    Account,
    ManagedAccount,
    AwsApiIntegration,
    NetworkPolicy,
    ResourceMonitor,
    Share,
    Warehouse,
    Role,
    User,
    AzureNotificationIntegration,
    SecurityIntegrationOAuth,
    SecurityIntegrationOAuthPartnerApp,
    SecurityIntegrationOAuthCustom,
    SecurityIntegrationSAML2,
    SecurityIntegrationSCIM,
    StorageIntegrationS3,
    StorageIntegrationGCS,
    StorageIntegrationAzure,
    Database,
    DatabaseFromShare,
    DatabaseReplica,
    Schema,
    Integration,
    Stage,
    Task,
    View,
    MaterializedView,
    MaskingPolicy,
    FileFormat,
    InternalStage,
    ExternalStage,
    Pipe,
    Stream,
    Function,
    Procedure,
    Sequence,
    Table,
]


UTC = "UTC"
APP = "PythonConnector [snowday]"
Q_TAG = "[snowday]"


class Connector:
    def __init__(self, **connection_kwargs):
        self.verbose = True
        for k, v in connection_kwargs.items():
            if k.lower() != "password":
                setattr(self, k, v)
            else:
                setattr(self, k, "*" * len(v))
        self.query_tag = Q_TAG
        self.search_path = None
        self.connection = sf_connector.connect(
            application=APP,
            internal_application_name=APP,
            session_parameters={"QUERY_TAG": Q_TAG},
            **connection_kwargs,
        )
        self.cursor = self.connection.cursor(sf_connector.DictCursor)

        def snowstopper() -> None:  # pragma: no cover
            self.cursor.close()
            self.connection.close()

        atexit.register(snowstopper)

    def __enter__(self, **kwargs):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()

    def enable_verbose(self) -> None:
        self.verbose = True

    def disable_verbose(self) -> None:
        self.verbose = False

    def execute_safe(self, sql: str) -> dict:
        try:
            if self.verbose:
                LOG.info(sql)
            return self.cursor.execute(sql)
        except Exception as e:
            self.cursor.execute("rollback;")
            if self.verbose:
                LOG.error(sql)
                LOG.debug(e)
            raise e

    def use(self, subject: Union[Warehouse, Database, Schema]) -> dict:
        """A way to quickly navigate the primary search path.
        """
        if subject.__class__ == Warehouse:
            self.warehouse = subject.fqn
        else:
            self.search_path = subject.fqn
        sql = f"use {subject.resource_type} {subject.fqn};"
        return self.fetch(sql)

    def set_session_params(self, **session_params) -> None:
        for param, val in session_params.items():
            self.execute_safe(f"alter session set {param} = '{val}';")

    def set_query_tag(self, query_tag) -> None:
        q_tag = f"{query_tag} {Q_TAG}"
        self.query_tag = q_tag
        self.set_session_params(query_tag=q_tag)

    def set_utc(self) -> None:
        self.set_session_params(timezone=UTC)

    def fetchone(self, sql: str) -> dict:
        return self.execute_safe(sql).fetchone()

    def fetch(self, sql: str) -> dict:
        """An alias for fetchone
        """
        return self.fetchone(sql)

    def fetchall(self, sql: str) -> list:
        return self.execute_safe(sql).fetchall()

    def fetchone_by_key(self, sql: str, key: str):
        return self.fetchone(sql)[key]

    def fetch_by_key(self, sql: str, key: str):
        """An alias for fetchone_by_key
        """
        return self.fetchone_by_key(sql, key)

    def fetchall_by_key(self, sql: str, key: str):
        return [row[key] for row in self.fetchall(sql)]

    def yield_all(self, sql: str) -> Iterator[dict]:
        for row in self.fetchall(sql):
            yield row

    def yield_all_by_key(self, sql: str, key: str) -> Iterator:
        for row in self.fetchall(sql):
            yield row[key]

    def commit(self) -> dict:
        return self.cursor.execute("commit;").fetchone()

    def rollback(self) -> dict:
        return self.cursor.execute("rollback;").fetchone()

    def create(self, obj: ALL_OBJS) -> dict:
        return self.fetch(obj.create)

    def create_if_not_exists(self, obj: ALL_OBJS) -> dict:
        return self.fetch(obj.create_if_not_exists)

    def create_or_replace(self, obj: ALL_OBJS) -> dict:
        return self.fetch(obj.create_or_replace)

    def drop(self, obj: ALL_OBJS) -> dict: # FIXME! Add force= param to this?
        # if force: # FIXME! Do this.
        return self.fetch(obj.drop)

    def describe(self, obj: ALL_OBJS) -> dict:
        return self.fetch(obj.describe)
