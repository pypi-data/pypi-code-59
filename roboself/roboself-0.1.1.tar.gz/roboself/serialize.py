from typing import Union, Any

from roboself import Node, Graph


def _node_to_dict(node: Node):
    """Helper to convert a node to a dict that can be converted to JSON."""
    if node is None:
        return None

    d = {
        "_id": node.id,
    }

    return d


def _is_dict_node(v):
    """Helper method to check if a value represents a dict Node."""
    if not isinstance(v, dict):
        return False

    return "_id" in v or "_ref" in v


def _dict_to_node(d, graph):
    """Converts a JSON dict instance to a node."""
    node_id = d.get("_id")
    if node_id is None:
        node_id = d.get("_ref")

        if node_id is None:
            raise Exception(f"Did not find any node id for: {d}")

    return Node(graph, d)


def to_json(data: Union[dict, list, Node, Any]):
    """Serializes data to a dict format which can be safely converted to JSON string.

    Currently it does the following:
    - converts Node instances to { "_id": 1, ... }
    - converts arrays of Nodes to arrays of dicts

    It also goes recursively on dicts.
    """
    if isinstance(data, dict):
        return {
            prop: to_json(value) for prop, value in data.items()
        }
    elif isinstance(data, list):
        return [to_json(x) for x in data]
    elif isinstance(data, Node):
        return _node_to_dict(data)
    else:
        return data


def from_json(data: Union[dict, list, Node, Any], graph: Graph):
    """Deserializes data from a JSON dict to a python dict.

    It's the opposite of the `to_json`. It recreates Node instances.
    """
    if isinstance(data, dict):
        if _is_dict_node(data):
            return _dict_to_node(data, graph)
        else:
            return {
                prop: from_json(value, graph) for prop, value in data.items()
            }
    elif isinstance(data, list):
        return [from_json(x, graph) for x in data]
    else:
        return data
