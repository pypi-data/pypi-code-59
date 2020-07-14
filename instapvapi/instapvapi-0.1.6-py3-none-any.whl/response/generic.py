from instapv.utils.auto_mapper import AutoMapper

class GenericResponse(AutoMapper):

    def __init__(self, data: dict):
        self.response = self._auto_mapper(data)
        self.as_json = data
