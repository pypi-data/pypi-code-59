import logging

class Executor():
    
    def __init__(self):
        self.counter = 0

    def do(self, task, env):
        self.counter += 1
        skip = False
        
        if "fail_period" in task:
            logging.debug("Failing period configured: %s current loop: %s" % (task['fail_period'], self.counter))
            if self.counter % task['fail_period'] == 0:
                logging.debug("Supposed to fail every %s loops, now loop %s." % (task['fail_period'], self.counter))
                skip = False
            else:
                logging.debug("Not going to fail")
                skip = True

        if skip:
            logging.debug("Skipping due to task configuration.")
            return None, "{}"
        else:
            logging.info("Failing task on purpose")
            raise Exception("Failing task on purpose")

