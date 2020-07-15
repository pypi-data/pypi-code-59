class ZaleyCashException(Exception):
    pass


class ZaleyCashNetworkError(ZaleyCashException):
    def __init__(self, original):
        self.original = original


class ZaleyCashError(ZaleyCashException):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ZaleyCashAuthError(ZaleyCashError):
    pass


class ZaleyCashBadRequest(ZaleyCashError):
    pass


class ZaleyCashBadResponse(ZaleyCashError):
    pass


class ZaleyCashUnauthorizedAccessError(ZaleyCashError):
    pass


class ZaleyCashServerError(ZaleyCashError):
    pass


class ZaleyCashNotFound(ZaleyCashError):
    pass


class ZaleyCashUnknownError(ZaleyCashError):
    pass
