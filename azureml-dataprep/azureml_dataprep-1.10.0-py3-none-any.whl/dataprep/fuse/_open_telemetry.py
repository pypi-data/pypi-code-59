from json import JSONEncoder, loads
from opentelemetry.trace import SpanContext


class SpanContextEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def deserialize(json_str):
    span_context = SpanContext(0, 0, True)
    span_context.__dict__ = loads(json_str)
    return span_context
