from opentelemetry.sdk.trace.export import BatchExportSpanProcessor, SpanExporter, SimpleExportSpanProcessor
from opentelemetry.trace import Span


try:
    from azureml.core import Run
    _run_id = Run.get_context().id
except:
    _run_id = None


class AmlSimpleSpanProcessor(SimpleExportSpanProcessor):
    def __init__(self, span_exporter: SpanExporter):
        super().__init__(span_exporter=span_exporter)

    def on_start(self, span: Span) -> None:
        super().on_start(span)
        _add_aml_context(span)


class AmlBatchSpanProcessor(BatchExportSpanProcessor):
    def __int__(
            self,
            span_exporter: SpanExporter,
            max_queue_size: int = 2048,
            schedule_delay_millis: float = 5000,
            max_export_batch_size: int = 512,
    ):
        super().__init__(span_exporter=span_exporter, max_queue_size=max_queue_size,
                         schedule_delay_millis=schedule_delay_millis, max_export_batch_size=max_export_batch_size)

    def on_start(self, span: Span) -> None:
        super().on_start(span)
        _add_aml_context(span)


def _add_aml_context(span: Span):
    from .._loggerfactory import session_id

    span.set_attribute('sessionId', session_id)
    span.set_attribute('runId', _run_id)
