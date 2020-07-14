import json
from collections import namedtuple


class AutoMapper:

    def _json_object_hook(self, d): 
        return namedtuple('AutoMapperTuple', d.keys())(*d.values())

    def _auto_mapper(self, json_data): 
        json_data = json.dumps(
            json_data
        )
        return json.loads(json_data, object_hook=self._json_object_hook)

