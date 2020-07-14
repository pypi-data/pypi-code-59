from instapv.utils.auto_mapper import AutoMapper
import jsonobject as mapper

class LoginResponse(AutoMapper):

    def __init__(self, data: dict):
        self.response = self._auto_mapper(data)
        self.as_json = data