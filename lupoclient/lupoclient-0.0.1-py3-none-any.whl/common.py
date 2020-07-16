API_URL = 'https://api.zorro.staq.ai/'

def join_paths(path1, path2):
    """ Joins two URL paths with a single slash. Removes extra slashes/Adds a slash if necessary. """
    if path1.endswith("/"):
        path1 = path1[:-1]
    
    if path2.startswith("/"):
        path2 = path2[1:]
    
    return path1 + "/" + path2

def parse_seconds(interval):
    """ Parses the seconds of an interval in NNNN_[s/m/h/d/w] format """
    intervals = {"s": 1, "m" : 60, "h" : 3600, "d" : 3600*24, "w" : 3600*24*7}
    return int(interval.split("_")[0]) * intervals[interval.split("_")[1]]