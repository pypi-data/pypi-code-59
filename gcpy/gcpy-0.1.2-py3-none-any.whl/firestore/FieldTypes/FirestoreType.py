import google.cloud.firestore_v1.document as firestore_document


class FirestoreType:
    """
        Firestore type definition
    """
    value: int = 0

    def __init__(self, value):
        self.value = value

    @staticmethod
    def map_change(changes: dict):
        """
        Initialising the new instance with a `Value`_ dictionary

        Args:
            changes (dict): The value represented by a `Value`

        .. _Value:
            https://cloud.google.com/firestore/docs/reference/rest/v1/Value

        """
        pass

    #
    # def __init__(self,
    #              doc: firestore_document.DocumentReference):
    #     """
    #     Initialising the new instance with a `DocumentReference`_ object
    #
    #     Args:
    #         doc (DocumentReference): a `DocumentReference`
    #
    #     .. _DocumentReference:
    #         https://googleapis.dev/python/firestore/latest/document.html
    #
    #     """
    #
    #     self.x = x
