from lxml import etree

from idin.idx import utils
from idin.idx.base import IdxMessage


class TransactionResponse(IdxMessage):
    _message_name = "AcquirerTrxRes"

    def __init__(
        self,
        *,
        acquirer_id: str,
        issuer_authentication_url: str,
        transaction_id: str,
        transaction_timestamp: str,
        create_timestamp=None,
    ):
        self.create_timestamp = create_timestamp or utils.utcnow()
        self.issuer_authentication_url = issuer_authentication_url
        self.acquirer_id = acquirer_id
        self.transaction_id = transaction_id
        self.transaction_timestamp = transaction_timestamp
        super().__init__()

    def serialize(self) -> etree._Element:
        root = super().serialize()
        elm = etree.SubElement(root, "Acquirer")
        self._add_text_node(elm, "acquirerID", self.acquirer_id)

        elm = etree.SubElement(root, "Issuer")
        self._add_text_node(
            elm, "issuerAuthenticationURL", self.issuer_authentication_url
        )

        elm = etree.SubElement(root, "Transaction")
        self._add_text_node(elm, "transactionID", self.transaction_id)
        self._add_text_node(
            elm,
            "transactionCreateDateTimestamp",
            utils.datetime_to_xml(self.transaction_timestamp),
        )
        return root

    @classmethod
    def deserialize(cls, document: etree._Document):
        obj = cls(
            create_timestamp=utils.xpath_text(document, "idx:createDateTimestamp"),
            acquirer_id=utils.xpath_text(document, "idx:Acquirer/idx:acquirerID"),
            issuer_authentication_url=utils.xpath_text(
                document, "idx:Issuer/idx:issuerAuthenticationURL"
            ),
            transaction_id=utils.xpath_text(
                document, "idx:Transaction/idx:transactionID"
            ),
            transaction_timestamp=utils.xpath_datetime(
                document, "idx:Transaction/idx:transactionCreateDateTimestamp"
            ),
        )
        return obj
