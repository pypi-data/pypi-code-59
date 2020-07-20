from lxml import etree

from idin.idx import utils
from idin.idx.base import IdxMessage


class StatusRequest(IdxMessage):
    _message_name = "AcquirerStatusReq"

    def __init__(
        self,
        *,
        merchant_id: str,
        merchant_sub_id: str,
        transaction_id: str,
        create_timestamp=None,
    ):
        self.create_timestamp = create_timestamp or utils.utcnow()
        self.merchant_id = merchant_id
        self.merchant_sub_id = merchant_sub_id
        self.transaction_id = transaction_id
        super().__init__()

    def serialize(self) -> etree._Element:
        root = super().serialize()

        elm = etree.SubElement(root, "Merchant")
        self._add_text_node(elm, "merchantID", self.merchant_id)
        self._add_text_node(elm, "subID", self.merchant_sub_id)

        elm = etree.SubElement(root, "Transaction")
        self._add_text_node(elm, "transactionID", self.transaction_id)
        return root

    @classmethod
    def deserialize(cls, document: etree._Document):
        obj = cls(
            create_timestamp=utils.xpath_text(document, "idx:createDateTimestamp"),
            merchant_id=utils.xpath_text(document, "idx:Merchant/idx:merchantID"),
            merchant_sub_id=utils.xpath_text(document, "idx:Merchant/idx:subID"),
            transaction_id=utils.xpath_text(
                document, "idx:Transaction/idx:transactionID"
            ),
        )
        return obj
