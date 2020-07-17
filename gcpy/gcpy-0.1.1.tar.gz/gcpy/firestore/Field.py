from gcpy.firestore.FieldTypes.FirestoreType import FirestoreType

FieldType = FirestoreType.__class__


class Field:
    name: str
    type: FieldType

    def __init__(
            self,
            name: str,
            type: FieldType
    ):
        """
        
        Args:
            name: 
            type: 
        """
        self.name = name
        self.type = type
