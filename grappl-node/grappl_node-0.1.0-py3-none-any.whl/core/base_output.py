from abc import ABC, abstractmethod
from .event import Event


class NodeOutput(ABC):

    @abstractmethod
    async def dispatch(self, event: Event) -> None:
        pass
