import json
import os
from typing import Optional, Sequence

from opentelemetry.sdk.trace import Span, Event as OTEvent
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult
from opentelemetry.sdk.util import BoundedDict, ns_to_iso_str

logger = None


def get_logger():
    from azureml.dataprep.api._loggerfactory import _LoggerFactory

    global logger
    if logger is not None:
        return logger

    logger = _LoggerFactory.get_logger("JsonLineExporter")
    return logger


class JsonLineExporter(SpanExporter):
    def __init__(self, session_id: str, base_directory: Optional[str] = None):
        path = os.path.join(base_directory, 'python_span_{}.jsonl'.format(session_id))
        self._file = open(path, 'w')

    def export(self, spans: Sequence[Span]) -> SpanExportResult:
        json_lines = '\n'.join(map(self.__class__.to_json, spans))
        self._file.write('{}\n'.format(json_lines))
        self._file.flush()
        return SpanExportResult.SUCCESS

    def shutdown(self) -> None:
        self._file.close()

    @staticmethod
    def to_json(span_data: Span) -> str:
        if not span_data:
            return ''

        def serialize_span(span: Span):
            return json.dumps({
                'traceId': span.get_context().trace_id.to_bytes(16, 'big').hex(),
                'spanId': span.get_context().span_id.to_bytes(8, 'big').hex(),
                'parentSpanId': span.parent.span_id.to_bytes(8, 'big').hex() if span.parent else '',
                'name': span.name,
                'kind': str(span.kind),
                'startTime': ns_to_iso_str(span.start_time),
                'endTime': ns_to_iso_str(span.end_time),
                'attributes': convert_attributes(span.attributes),
                'events': convert_events(span.events)
            })

        def convert_events(events: Sequence[OTEvent]):
            return list(map(lambda event: {
                'name': event.name,
                'timeStamp': ns_to_iso_str(event.timestamp),
                'attributes': convert_attributes(event.attributes)
            }, events))

        def convert_attributes(attributes):
            if isinstance(attributes, BoundedDict):
                return attributes._dict
            return attributes

        return serialize_span(span_data)
