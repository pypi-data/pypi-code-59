import asyncio
from ..core import Node, NodeInput, NodeOutput


async def run_node_gen(node: Node, node_input: NodeInput, node_output: NodeOutput):
    async for in_event in node_input:
        out_event = await node.process(in_event)
        if out_event is not None:
            yield await node_output.dispatch(out_event)


async def run_node(node: Node, node_input: NodeInput, node_output: NodeOutput):
    return [event async for event in run_node_gen(node, node_input, node_output)]
