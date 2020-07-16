import logging
from typing import Optional, Iterable
from . import util


class Plugin:
    def __init__(self, pipeline: str, prid: Optional[int]):
        self.pipeline = pipeline
        self.prid = prid
        self.logger = PluginLoggerAdapter(util.get_class_logger(self), self.pipeline, self.prid)


class Input(Plugin):
    def __init__(self, pipeline: str, prid: int):
        super().__init__(pipeline, prid)
    
    def input(self, rows_prev: Optional[Iterable] = None, num_rows_prev: Optional[int] = None):
        raise NotImplementedError


class Processor(Plugin):
    def __init__(self, pipeline: str, prid: int):
        super().__init__(pipeline, prid)

    def process(self, rows: Iterable):
        raise NotImplementedError


class Output(Plugin):
    def __init__(self, pipeline: str, prid: int):
        super().__init__(pipeline, prid)

    def output(self, rows: Iterable, num_rows: Optional[int]):
        raise NotImplementedError


class Trigger(Plugin):
    def __init__(self, pipeline: str, prid: Optional[int] = None):
        super().__init__(pipeline, 0)
    
    def run(self):
        raise NotImplementedError


class PluginLoggerAdapter(logging.LoggerAdapter):
    def __init__(self, logger: logging.Logger, pipeline: str, prid: Optional[int]):
        super(PluginLoggerAdapter, self).__init__(logger, {})
        self.pipeline = pipeline
        self.prid = prid

    def process(self, msg, kwargs):
        pipeline_str = self.pipeline
        if self.prid != 0:
            pipeline_str += f':{self.prid}'
        return f'[{pipeline_str}] {msg}', kwargs
