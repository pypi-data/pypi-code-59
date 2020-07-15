from dataclasses import dataclass, field
from typing import Union


@dataclass
class Event:
    key: str
    headers: dict = field(default_factory=dict)
    data: Union[dict, int, float, str, bytes] = None
