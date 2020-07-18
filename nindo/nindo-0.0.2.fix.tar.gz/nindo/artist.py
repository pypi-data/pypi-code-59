class Artist(object):

    def __init__(self, name, id):

        self.name = name
        self.id = id

    def __repr__(self):

        return f"<nindo.api.Artist '{self.id}'>"