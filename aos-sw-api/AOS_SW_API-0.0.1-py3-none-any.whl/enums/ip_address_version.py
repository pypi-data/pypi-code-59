from enum import Enum


class IpAddressVersion(str, Enum):
    IAV_IP_V4 = "IAV_IP_V4"
    IAV_IP_V6 = "IAV_IP_V6"
