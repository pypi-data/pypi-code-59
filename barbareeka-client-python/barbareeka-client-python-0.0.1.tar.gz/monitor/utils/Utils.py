import datetime


class Utils(object):

    def get_current_time(self):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        return datetime.datetime.strftime(datetime.datetime.now(), date_format)[:-3]
