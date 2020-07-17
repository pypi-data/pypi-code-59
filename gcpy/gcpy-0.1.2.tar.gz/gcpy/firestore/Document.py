from gcpy.firestore.Changes import Changes
import google.cloud.firestore_v1.document as firestore_document


class Document:

    @classmethod
    def map_changes(cls, change):
        fields = cls.__annotations__
        new = cls()
        for field in fields:
            # print(field)
            # print(fields[field].map_change({}))
            new.__setattr__(field, fields[field].map_change(change.get(field, {})))
        return new

    @classmethod
    def changes(cls, changes: dict):
        return Changes(
            old=cls.map_changes(changes.get('oldValue', {})),
            new=cls.map_changes(changes.get('newValue', {}))
        )

    @classmethod
    def from_doc(cls, doc: firestore_document.DocumentReference):
        data = doc.get().to_dict()
        result = cls()
        for key in data:
            if key in cls.__annotations__:
                result.__setattr__(key, data[key])

    def __iter__(self):
        for key in self.__annotations__:
            yield key, self.__getattribute__(key).value
