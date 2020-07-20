def get_date(days=0, separator='-'):
    import datetime
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime(f"%Y{separator}%m{separator}%d")


def get_today(separator='-'):
    return get_date(days=0, separator=separator)
