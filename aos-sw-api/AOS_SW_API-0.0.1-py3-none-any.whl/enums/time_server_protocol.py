from enum import Enum


class TimeServerProtocol(str, Enum):
    TSP_NTP = "TSP_NTP"
    TSP_SNTP = "TSP_SNTP"
