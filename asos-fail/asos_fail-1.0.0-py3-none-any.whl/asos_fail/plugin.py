import logging

class Executor():

    def do(self, task, env):
        logging.info("Failing task on purpose")
        raise Exception("Failing task on purpose")

