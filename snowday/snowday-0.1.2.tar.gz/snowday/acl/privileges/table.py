from snowday.acl.privileges.common import ALL, OWNERSHIP
from snowday.acl.privileges.schema_objects import (
    SELECT,
    INSERT,
    UPDATE,
    DELETE,
    TRUNCATE,
    REFERENCES,
)


TABLE_PRIVILEGES = [
    ALL,
    SELECT,
    INSERT,
    UPDATE,
    DELETE,
    TRUNCATE,
    REFERENCES,
]
