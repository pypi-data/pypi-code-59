from lxml import etree

from idin.idx import utils
from idin.idx.base import IdxMessage


class TransactionRequest(IdxMessage):
    _message_name = "AcquirerTrxReq"

    def __init__(
        self,
        *,
        issuer_id: str,
        merchant_id: str,
        merchant_sub_id: str,
        merchant_return_url: str,
        language: str,
        entrance_code: str,
        container: etree._Element,
        create_timestamp=None,
    ):
        self.create_timestamp = create_timestamp or utils.utcnow()
        self.issuer_id = issuer_id
        self.merchant_id = merchant_id
        self.merchant_sub_id = merchant_sub_id
        self.merchant_return_url = merchant_return_url
        self.language = language
        self.entrance_code = entrance_code
        self.container = container
        super().__init__()

    def serialize(self) -> etree._Element:
        root = super().serialize()

        elm = etree.SubElement(root, "Issuer")
        self._add_text_node(elm, "issuerID", self.issuer_id)

        elm = etree.SubElement(root, "Merchant")
        self._add_text_node(elm, "merchantID", self.merchant_id)
        self._add_text_node(elm, "subID", self.merchant_sub_id)
        self._add_text_node(elm, "merchantReturnURL", self.merchant_return_url)

        elm = etree.SubElement(root, "Transaction")
        self._add_text_node(elm, "expirationPeriod", "PT5M")
        self._add_text_node(elm, "language", self.language)
        self._add_text_node(elm, "entranceCode", self.entrance_code)

        container = etree.SubElement(elm, "container")
        container.append(self.container)
        return root

    @classmethod
    def deserialize(cls, document: etree._Document):
        obj = cls(
            create_timestamp=utils.xpath_text(document, "idx:createDateTimestamp"),
            issuer_id=utils.xpath_text(document, "idx:Issuer/idx:issuerID"),
            merchant_id=utils.xpath_text(document, "idx:Merchant/idx:merchantID"),
            merchant_sub_id=utils.xpath_text(document, "idx:Merchant/idx:subID"),
            merchant_return_url=utils.xpath_text(
                document, "idx:Merchant/idx:merchantReturnURL"
            ),
            language=utils.xpath_text(document, "idx:Transaction/idx:language"),
            entrance_code=utils.xpath_text(
                document, "idx:Transaction/idx:entranceCode"
            ),
            container=utils.xpath_elm(document, "idx:Transaction/idx:container"),
        )
        return obj
