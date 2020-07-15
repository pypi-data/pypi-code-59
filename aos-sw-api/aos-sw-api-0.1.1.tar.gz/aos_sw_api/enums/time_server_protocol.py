from enum import Enum


class TimeServerProtocolEnum(str, Enum):
    TSP_NTP = "TSP_NTP"
    TSP_SNTP = "TSP_SNTP"
