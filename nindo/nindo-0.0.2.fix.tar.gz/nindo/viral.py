class Viral(object):

    def __init__(self, id, platform, timestamp, type, value):

        self.id = id,
        self.platform = platform
        self.timestamp = timestamp
        self.type = type
        self.value = value

    def __repr__(self):

        return f"<nindo.api.Viral '{self.id}'>"