from enum import Enum


class LacpStatusEnum(str, Enum):
    LAS_DISABLED = "LAS_DISABLED"
    LAS_ACTIVE = "LAS_ACTIVE"
    LAS_PASSIVE = "LAS_PASSIVE"
