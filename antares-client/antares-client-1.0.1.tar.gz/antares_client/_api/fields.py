from io import StringIO

import pandas as pd
from marshmallow import fields

from .api import get_resource, list_resource


class Lightcurve(fields.Field):
    """Field that represents an ANTARES lightcurve as a pandas dataframe"""

    def _deserialize(self, value, attr, obj, **kwargs):
        return pd.read_csv(StringIO(value))


class IncludeRelated(fields.Field):
    """Field that includes an entire related resource collection"""

    def __init__(self, schema, many=False, **kwargs):
        self.schema = schema
        self.many = many
        super().__init__(**kwargs)

    def _deserialize(self, value, attr, obj, **kwargs):
        if self.many:
            return list(list_resource(value["links"]["related"], self.schema))
        else:
            return get_resource(value["links"]["related"], self.schema)
