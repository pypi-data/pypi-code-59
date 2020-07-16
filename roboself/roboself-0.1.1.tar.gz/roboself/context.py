from typing import Any

from roboself import Client, serialize
from roboself.chat import Chat
from roboself.graph import Graph


class Context:
    """ Context interface connected to a running assistant.

    The context interface allows you to retrieve and set context information (key-value pairs).
    Also, it provides access to other components such as "chat" or "graph".

    # TODO: activate these one by one
    # progress: Progress
    # user: User
    """
    def __init__(self, client: Client, chat: Chat, graph: Graph):
        """ Constructor.

        :param client: The client used for the communication with the assistant runtime.
        :param chat: The chat interface to be used.
        :param graph: The graph interface to be used.
        """
        self.client = client
        self.chat = chat
        self.graph = graph

    def get(self, key: str):
        """Returns the value of a key in this context."""
        value = self.graph.client.request("/context/get", {
            "key": key
        })

        return serialize.from_json(value, graph=self.graph)

    def set(self, key: str, value: Any):
        """ Sets the value of a key in this context.

        The value can also include references to objects, or array of objects, in the
        knowledge graph. In this case they will be persisted only as references, not as
        specific values.

        :param key: The name of the key.
        :param value: The value of the key.
        :return: None
        """
        self.graph.client.request("/context/set", {
            "key": key,
            "value": serialize.to_json(value)
        })

    def __setitem__(self, item, value):
        """Shorthand helper for setting a context value.

        e.g. ctx["some_key"] = "some value"
        """
        return self.set(item, value)

    def __getitem__(self, item):
        """Shorthand helper for getting a context value.

        e.g. ctx["some_key"]
        """
        return self.get(item)
