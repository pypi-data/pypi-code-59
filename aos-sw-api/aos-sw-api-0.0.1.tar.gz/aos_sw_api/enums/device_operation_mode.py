from enum import Enum


class DeviceOperationMode(str, Enum):
    DOM_CLOUD = "DOM_CLOUD"
    DOM_CLOUD_WITH_SUPPORT = "DOM_CLOUD_WITH_SUPPORT"
    DOM_AUTONOMOUS = "DOM_AUTONOMOUS"
