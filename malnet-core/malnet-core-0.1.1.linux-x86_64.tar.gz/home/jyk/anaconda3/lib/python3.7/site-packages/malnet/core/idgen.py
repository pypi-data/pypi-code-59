import uuid

MALWARENET_ID_NAMESPACE = uuid.UUID("49652a79-aa85-451b-aa7f-46d5723f733e")
SCO_DET_ID_NAMESPACE = uuid.UUID("00abedb4-aa42-466c-9c01-fed23315a9b7")


class InvalidMethodError(ValueError):
    def __init__(self, method):
        ValueError.__init__(self, f"invalid IDGenerator method: {method}")


class IDMethod(object):
    INT = 1
    UUID4 = 2
    UUID5 = 3
    METHODS = (INT, UUID4, UUID5)


class IDGenerator(object):
    """Utility class for generating IDs for various entities"""
    def __init__(self,
                 method=IDMethod.UUID4,
                 prefix='malware',
                 namespace=MALWARENET_ID_NAMESPACE):
        self.prefix = str(prefix).strip().lower()
        self.namespace = namespace
        self.method = method
        self.reset()

    def reset(self):
        self.next_int = 1

    def create(
        self,
        name='',
    ):
        """Create an ID.

        Note that if `prefix` is not provided, it will be `malware`, even if the
        `method` is `METHOD_INT`.
        """
        prefix = self.prefix

        if self.method == IDMethod.UUID4:
            id_ = str(uuid.uuid4())
        elif self.method == IDMethod.INT:
            id_ = self.next_int
            self.next_int += 1
        elif self.method == IDMethod.UUID5:
            id_ = str(uuid.uuid5(self.namespace, name))
        else:
            raise InvalidMethodError(self.method)

        return f"{prefix}--{id_}"