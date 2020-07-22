class ContainerError(Exception):
    pass

class ConfigError(Exception):
    def __init__(self, msg, original_exception):
        super(ConfigError, self).__init__("{} : {}".format(msg, original_exception))
        self.original_exception = original_exception