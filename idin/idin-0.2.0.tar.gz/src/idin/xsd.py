from datetime import datetime

from dateutil import parser


def parse_datetime(value: str) -> datetime:
    return parser.parse(value)
