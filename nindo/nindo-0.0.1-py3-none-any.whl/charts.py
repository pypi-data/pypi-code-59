from .types import TYPES
class Chart(object):

    def __init__(self, id, rank, artist, value, chartType):

        self.id = id
        self.rank = rank
        self.artists = artist
        self.value = value
        self.type = TYPES.Charts.DISPLAY[chartType]

    def __repr__(self):

        return f"<nindo.api.Chart '{self.id}'>"