from lxml import etree

from idin.idx import utils
from idin.idx.base import IdxMessage


class StatusResponse(IdxMessage):
    _message_name = "AcquirerStatusRes"

    def __init__(
        self,
        *,
        acquirer_id: str,
        transaction_id: str,
        transaction_status: str,
        transaction_status_timestamp: str,
        container: etree._Element,
        create_timestamp=None,
    ):
        self.create_timestamp = create_timestamp or utils.utcnow()
        self.acquirer_id = acquirer_id
        self.transaction_id = transaction_id
        self.transaction_status = transaction_status
        self.transaction_status_timestamp = transaction_status_timestamp
        self.container = container
        super().__init__()

    def serialize(self) -> etree._Element:
        root = super().serialize()

        elm = etree.SubElement(root, "Acquirer")
        self._add_text_node(elm, "acquirerID", self.acquirer_id)

        elm = etree.SubElement(root, "Transaction")
        self._add_text_node(elm, "transactionID", self.transaction_id)
        self._add_text_node(elm, "status", self.transaction_status)
        self._add_text_node(
            elm,
            "statusDateTimestamp",
            utils.datetime_to_xml(self.transaction_status_timestamp),
        )
        container = etree.SubElement(elm, "container")
        container.append(self.container)
        return root

    @classmethod
    def deserialize(cls, document: etree._Document):
        container_element = utils.xpath_elm(document, "idx:Transaction/idx:container")

        obj = cls(
            create_timestamp=utils.xpath_datetime(document, "idx:createDateTimestamp"),
            acquirer_id=utils.xpath_text(document, "idx:Acquirer/idx:acquirerID"),
            transaction_id=utils.xpath_text(
                document, "idx:Transaction/idx:transactionID"
            ),
            transaction_status=utils.xpath_text(document, "idx:Transaction/idx:status"),
            transaction_status_timestamp=utils.xpath_datetime(
                document, "idx:Transaction/idx:statusDateTimestamp"
            ),
            container=container_element[0] if container_element is not None else None,
        )

        return obj
