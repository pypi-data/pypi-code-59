class ErrorCode:
    faq_import_error = 10010
    faq_train_error = 10011
    kg_import_error = 10020
    kg_train_error = 10021


class BfEngineException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.message = msg

    def __str__(self):
        return '{}: {}'.format(self.code, self.message)
