from multiprocessing import Process
from .logger import logger

class ForkRun:
    def __init__(self, procs):
        self._procs = procs

    def __enter__(self):
        logger.info(f"Starting fork run.")
        for proc in self._procs:
            proc.start()
        return self

    def __exit__(self, type, value, traceback):
        logger.info(f"Stopping fork run.")
        for proc in self._procs:
            proc.terminate()
        for proc in self._procs:
            proc.join()

    def all_running(self):
        return all(proc.is_alive() for proc in self._procs)

class Fork:
    def __init__(self, constructor = None, *, workers = 1):
        self._constructor = constructor
        self._workers = workers

    def construct_input(self):
        if self._constructor is None:
            raise RuntimeError("No constructor was provided.")
        return self._constructor()

    def run(self):
        procs = list()
        for _ in range(self._workers):
            target, args = self.construct_input()
            procs.append(Process(target = target, args = args))
        return ForkRun(procs)