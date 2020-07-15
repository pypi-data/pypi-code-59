from lins_servico.exception_classes import ProcessInterrupted

from datetime import timedelta
import threading
import signal

import logging

class Thread(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)

        self.daemon = False
        self.stopped = threading.Event()
        self.interval = timedelta(seconds=interval)
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            try:
                self.execute(*self.args, **self.kwargs)
            except Exception as err:
                logging.critical(err, exc_info=True)

    def signal_handler(self, signum, frame):
        raise ProcessInterrupted