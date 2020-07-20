import os
import uuid
from functools import lru_cache

UUID_VAR = 'REMO_UUID'


@lru_cache()
def get_uuid() -> str:
    value = os.getenv(UUID_VAR)
    if value:
        return value

    value = str(uuid.uuid4())
    os.environ[UUID_VAR] = value
    return value


def set_uuid(uuid: str):
    os.environ[UUID_VAR] = uuid
