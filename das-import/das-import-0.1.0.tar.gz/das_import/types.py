import enum
from typing import NamedTuple


class CardType(enum.Enum):
    BLACK = "black"
    WHITE = "white"


class Expansion(NamedTuple):
    id: int


class Card(NamedTuple):
    type: CardType
    content: str
