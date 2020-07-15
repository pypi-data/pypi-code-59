'''malnet exception'''


class MalnetCriticalError(Exception):
    pass


class MalnetConfigError(MalnetCriticalError):
    pass


class MalnetDBError(MalnetCriticalError):
    pass