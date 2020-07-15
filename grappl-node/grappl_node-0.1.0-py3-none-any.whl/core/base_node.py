from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Union
from .event import Event


class Node(ABC):
    """
    Class that specifies the interface for creating a node.
    """

    @abstractmethod
    async def process(self, event: Event) -> Union[Event, List[Event], None]:
        pass
