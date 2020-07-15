from ..event import Event
from ..base_output import NodeOutput


class NullNodeOutput(NodeOutput):
    async def dispatch(self, event: Event):
        pass
