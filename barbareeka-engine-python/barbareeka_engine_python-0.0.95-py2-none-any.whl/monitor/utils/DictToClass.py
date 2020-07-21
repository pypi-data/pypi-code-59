class DictToClass(dict):
    def __init__(self, *args, **kwargs):
        super(DictToClass, self).__init__(*args, **kwargs)
        self.__dict__ = self
