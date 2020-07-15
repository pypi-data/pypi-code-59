from abc import ABC, abstractmethod
from .event import Event


class NodeInput(ABC):

    @abstractmethod
    async def consume(self) -> Event:
        pass

    async def __anext__(self) -> Event:
        return await self.consume()

    def __aiter__(self):
        return self
