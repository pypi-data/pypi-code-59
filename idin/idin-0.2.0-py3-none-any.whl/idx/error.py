from lxml import etree

from idin.idx import utils
from idin.idx.base import IdxMessage


class IdinException(IOError):
    def __init__(self, message, code, detail, suggested_action, consumer_message):
        super().__init__("%s: %s - %s" % (code, message, detail))
        self.message = message
        self.code = code
        self.detail = detail
        self.suggested_action = suggested_action
        self.consumer_message = consumer_message


class ErrorResponse(IdxMessage):
    _message_name = "AcquirerErrorRes"

    def __init__(
        self,
        *,
        code=None,
        message=None,
        detail=None,
        suggested_action=None,
        consumer_message=None
    ):
        self.code = code
        self.message = message
        self.detail = detail
        self.suggested_action = suggested_action
        self.consumer_message = consumer_message
        super().__init__()

    def serialize(self) -> etree._Element:
        raise NotImplementedError()

    @classmethod
    def deserialize(cls, document: etree._Document):
        return cls(
            code=utils.xpath_text(document, "idx:Error/idx:errorCode"),
            message=utils.xpath_text(document, "idx:Error/idx:errorMessage"),
            detail=utils.xpath_text(document, "idx:Error/idx:errorDetail"),
            suggested_action=utils.xpath_text(
                document, "idx:Error/idx:suggestedAction"
            ),
            consumer_message=utils.xpath_text(
                document, "idx:Error/idx:consumerMessage"
            ),
        )

    def as_exception(self):
        return IdinException(
            self.message,
            code=self.code,
            detail=self.detail,
            suggested_action=self.suggested_action,
            consumer_message=self.consumer_message,
        )
