from gcpy.firestore.FieldTypes.FirestoreType import FirestoreType


class String(FirestoreType):
    value: str = None

    @staticmethod
    def map_change(changes: dict):
        if changes is None or not isinstance(changes, dict):
            raise ValueError("Changes for string value must be a dict containing a stringValue key")

        return String(value=changes.get('stringValue'))
