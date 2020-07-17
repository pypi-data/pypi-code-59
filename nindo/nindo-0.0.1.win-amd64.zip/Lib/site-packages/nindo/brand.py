class Brand(object):

    def __init__(self, id, name, url, branch, color):

        self.id = id
        self.name = name
        self.url = url
        self.branch = branch
        self.color = color

    def __repr__(self):

        return f"<nindo.api.Brand '{self.id}'>"