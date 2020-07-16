class TestCase(object):
    name: str
    id: str
    sourceTagNames: list
    lines: list
    status: str
    uri: str
    featureFileName: str

    def __init__(self):
        self.name = str()
        self.id = str()
        self.sourceTagNames = list()
        self.lines = list()
        self.status = str()
        self.uri = str()
        self.featureFileName = str()
