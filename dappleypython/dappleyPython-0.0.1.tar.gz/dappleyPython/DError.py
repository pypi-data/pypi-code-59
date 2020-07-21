class ParamError(Exception):
    def __init__(self, error, message):
        super(ParamError, self).__init__(message)
        self.error = error
