import logging
from typing import Optional, List
from . import util


class Plugin:
    def __init__(self, pipeline: str, prid: Optional[int]):
        self.pipeline = pipeline
        self.prid = prid
        self.logger = PluginLoggerAdapter(util.get_class_logger(self), self.pipeline, self.prid)


class Input(Plugin):
    def __init__(self, pipeline: str, prid: Optional[int]):
        super().__init__(pipeline, prid)
    
    def input(self, rows_prev: Optional[List] = None, num_rows_prev: Optional[int] = None):
        raise NotImplementedError


class Processor(Plugin):
    def __init__(self, pipeline: str, prid: Optional[int]):
        super().__init__(pipeline, prid)

    def process(self, rows: []):
        raise NotImplementedError


class Output(Plugin):
    def __init__(self, pipeline: str, prid: Optional[int]):
        super().__init__(pipeline, prid)

    def output(self, rows: [], num_rows: Optional[int]):
        raise NotImplementedError


class Trigger(Plugin):
    def __init__(self, pipeline: str, prid: Optional[int]):
        super().__init__(pipeline, prid)
    
    def run(self):
        raise NotImplementedError


class PluginLoggerAdapter(logging.LoggerAdapter):
    def __init__(self, logger: logging.Logger, pipeline: str, prid: Optional[int]):
        super(PluginLoggerAdapter, self).__init__(logger, {})
        self.pipeline = pipeline
        self.prid = prid

    def process(self, msg, kwargs):
        return f'[{self.pipeline}:{self.prid}] {msg}', kwargs
