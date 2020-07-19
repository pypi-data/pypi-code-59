class DarwinError(Exception):
    def __init__(self, error_message="", response_code=None, response_body=None):
        Exception.__init__(self, error_message)
        self.response_code = response_code
        self.response_body = response_body
        self.error_message = error_message

    def __str__(self):
        if self.response_code:
            return "{}: {}".format(self.response_code, self.error_message)
        return self.error_message


class DarwinHttpError(DarwinError):
    pass