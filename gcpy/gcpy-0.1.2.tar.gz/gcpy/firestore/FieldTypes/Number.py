from gcpy.firestore.FieldTypes.FirestoreType import FirestoreType


class Number(FirestoreType):
    value: float = None

    @staticmethod
    def map_change(changes: dict):
        if changes is None or not isinstance(changes, dict):
            raise ValueError("Changes for Number value must be a dict containing a integerValue or a doubleValue key")
        integer_value = changes.get('integerValue')
        if integer_value is not None:
            return Number(value=float(integer_value))
        return Number(value=changes.get('doubleValue'))
