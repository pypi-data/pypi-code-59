from dataclasses import dataclass
from ..event import Event
from ..base_input import NodeInput


@dataclass
class OnDemandCounterNodeInput(NodeInput):
    """
    A NodeInput that returns values whenever needed, 
    with the key count going up.
    """
    count: int = 0

    async def consume(self) -> Event:
        self.count += 1
        return Event(key=str(self.count))
