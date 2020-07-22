import time
import json
import sqlite3
from datetime import datetime


def get_time(timestamp):
    return int(time.mktime(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timetuple()))


def custom_query_loopback(database, loopback=60, issue="", name="", component=""):
    try:
        connection = sqlite3.connect(database)
        crsr = connection.cursor()

        loopback = int(loopback * 60)
        finish_time = int(time.time())
        start_time = finish_time - loopback

        if (issue and type(issue) != list) or (name and type(name) != list) or \
            (component and type(component) != list):
            raise Exception("type of issue, name and component needs to be list")

        issue = tuple(issue)
        name = tuple(name)
        component = tuple(component)

        command = "select timestamp, count, issue, name, component from Failures where "

        if start_time and finish_time:
            command += "time >= " + str(start_time) + " and time <= " + str(finish_time) + " and "

        if issue:
            command += "issue in " + str(issue + ('', )) + " and "

        if name:
            command += "name in " + str(name + ('', )) + " and "

        if component:
            command += "component in " + str(component + ('', )) + " and "

        command = command.strip().rsplit(' ', 1)[0]

        crsr.execute(command)
        fetched_data = crsr.fetchall()

        return create_json(fetched_data)

    except Exception as e:
        return e


def custom_query_interval(database, start_time="", finish_time="", issue="", name="", component=""):
    try:
        connection = sqlite3.connect(database)
        crsr = connection.cursor()

        if start_time:
            start_time = get_time(str(start_time.replace(microsecond=0)))
        if finish_time:
            finish_time = get_time(str(finish_time.replace(microsecond=0)))
        
        if (issue and type(issue) != list) or (name and type(name) != list) or \
            (component and type(component) != list):
            raise Exception("type of issue, name and component needs to be list")

        issue = tuple(issue)
        name = tuple(name)
        component = tuple(component)

        command = "select timestamp, count, issue, name, component from Failures where "

        if start_time and finish_time:
            command += "time >= " + str(start_time) + " and time <= " + str(finish_time) + " and "
        elif start_time:
            command += "time >= " + str(start_time) + " and "
        elif finish_time:
            command += "time <= " + str(finish_time) + " and "

        if issue:
            command += "issue in " + str(issue + ('', )) + " and "

        if name:
            command += "name in " + str(name + ('', )) + " and "

        if component:
            command += "component in " + str(component + ('', )) + " and "

        command = command.strip().rsplit(' ', 1)[0]

        crsr.execute(command)
        fetched_data = crsr.fetchall()

        return create_json(fetched_data)

    except Exception as e:
        return e


def create_json(fetched_data):
    failures = []
    for data in fetched_data:
        failure = {"timestamp": data[0], "count": data[1], "issue": data[2],
                   "name": data[3], "component": data[4]}
        failures.append(failure)

    history = {"history": {"failures": failures}}

    return json.dumps(history, indent=4, separators=(',', ': '))
