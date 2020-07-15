import datetime
import json
import logging
import time
import requests

class Executor():

    def do(self, task, env):
        if task['task_type'] != 'curl':
            raise Exception("Task type not supported")

        request_type = task['request_type'].lower()
        request_function = getattr(requests, request_type)
        logging.debug("Request type: %s" % request_type)

        if 'get_params' in task:
            params = task['get_params']
            logging.debug("Request GET params: %s" % params)
        else:
            params = {}

        if 'post_data' in task:
            data = task['post_data']
            logging.debug("Request POST data: %s" % data)
        else:
            data = {}

        _start = time.time()
        _timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        response = request_function(url=task['url'], data=data, params=params)
        time_spent = response.elapsed.total_seconds()
        status_code = response.status_code
        _finish = time.time()

        logging.debug("Time spent on request: %s sec." % time_spent)
        logging.debug("Time spent on whole thing: %s sec." % (_finish - _start))

        report = {
            "executor": env['uuid'],
            "group_id": task['task_group_id'],
            "timestamp": _timestamp,
            "url": response.url,
            "status_code": status_code,
            "time_spent": time_spent,
            "_start": _start,
            "_finish": _finish,
            "response": {
                "text": response.text,
                "code": response.status_code,
            }
        }

        return time_spent, json.dumps(report)

