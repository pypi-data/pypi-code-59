# 'datetimeValue'
# from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from datetime import datetime

from gcpy.firestore.FieldTypes.FirestoreType import FirestoreType


class DateTime(FirestoreType):
    value: datetime = None

    @staticmethod
    def map_change(changes: dict):
        if changes is None or not isinstance(changes, dict):
            raise ValueError("changes must be dict")

        raise ValueError("not implemented")
