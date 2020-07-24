import json

class FilterNotGood(Exception):
    def __init__(self, filter, accepted_filters):
        message = "Cloudimg currently doens not support filter \"%s\" or its value is not good. Accepted filters are: \n%s" % (filter, ', '.join([', '.join(filter["name_list"]) for filter in accepted_filters]))
        super().__init__(message)