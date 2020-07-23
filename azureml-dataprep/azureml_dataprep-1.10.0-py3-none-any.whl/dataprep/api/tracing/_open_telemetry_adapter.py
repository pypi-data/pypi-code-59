from typing import Optional

from azureml.dataprep.api.engineapi.typedefinitions import DPrepSpanContext, ActivityTraceFlags
from opentelemetry.trace import SpanContext


def to_dprep_span_context(span_context: Optional[SpanContext]) -> Optional[DPrepSpanContext]:
    # https://www.w3.org/TR/trace-context/#trace-id
    return DPrepSpanContext(
        is_remote=span_context.is_remote,
        span_id=span_context.span_id.to_bytes(8, 'big').hex(),
        trace_flags=ActivityTraceFlags(span_context.trace_flags),
        trace_id=span_context.trace_id.to_bytes(16, 'big').hex(),
        tracestate=span_context.trace_state
    ) if span_context else None
