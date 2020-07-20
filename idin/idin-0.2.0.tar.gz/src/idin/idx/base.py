import attr
from lxml import etree

from .utils import datetime_to_xml


@attr.s(auto_attribs=True)
class IdxMessage:
    _version = "1.0.0"
    _product_id = "NL:BVN:BankID:1.0"
    _namespace = "http://www.betaalvereniging.nl/iDx/messages/Merchant-Acquirer/1.0.0"

    def serialize(self):
        root = etree.Element(self._message_name, nsmap={None: self._namespace})
        root.set("version", self._version)
        root.set("productID", self._product_id)
        self._add_timestamp(root)
        return root

    def _add_timestamp(self, element):
        self._add_text_node(
            element, "createDateTimestamp", datetime_to_xml(self.create_timestamp)
        )

    def _add_text_node(self, parent, name, text) -> None:
        nsmap = {None: self._namespace}
        node = etree.SubElement(parent, name, nsmap=nsmap)
        if text:
            node.text = text

    @classmethod
    def qname(cls):
        return "{%s}%s" % (cls._namespace, cls._message_name)
