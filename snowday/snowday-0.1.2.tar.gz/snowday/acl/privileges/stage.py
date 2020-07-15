from snowday.acl.privileges.common import ALL, OWNERSHIP, USAGE


READ = "read"
WRITE = "write"

INTERNAL_STAGE_PRIVILEGES = [
    ALL,
    OWNERSHIP,
    READ,
    USAGE,
    WRITE,
]
EXTERNAL_STAGE_PRIVILEGES = [ALL, OWNERSHIP, USAGE]
