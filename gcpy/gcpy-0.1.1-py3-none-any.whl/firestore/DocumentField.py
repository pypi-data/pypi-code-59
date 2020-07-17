from gcpy.firestore.FieldTypes.FirestoreType import TypeDefinition


class DocumentField:
    def __init__(
            self,
            name: str,
            field_type: TypeDefinition
    ):
        """

        Creates a DocumentField

        :param name: name of the field
        :param field_type: FieldType type function e.g. FieldType.number
        """
        self.name = name
        self.field_type = field_type