from enum import Enum


class PortTrunkTypeEnum(str, Enum):
    PTT_TRUNK = "PTT_TRUNK"
    PTT_LACP = "PTT_LACP"
    PTT_NONE = "PTT_NONE"
