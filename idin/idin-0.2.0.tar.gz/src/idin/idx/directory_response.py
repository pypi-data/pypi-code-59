import typing

from lxml import etree

from idin import types
from idin.idx import utils
from idin.idx.base import IdxMessage


class DirectoryResponse(IdxMessage):
    _message_name = "DirectoryRes"

    def __init__(
        self,
        *,
        acquirer_id: str,
        create_timestamp=None,
        directory_timestamp=None,
        issuers: typing.List[types.CountryIssuers] = None,
    ):
        self.directory_timestamp = directory_timestamp or utils.utcnow()
        self.create_timestamp = create_timestamp or utils.utcnow()
        self.acquirer_id = acquirer_id
        self.issuers = issuers or []
        super().__init__()

    def serialize(self) -> etree._Element:
        root = super().serialize()

        elm = etree.SubElement(root, "Acquirer")
        self._add_text_node(elm, "acquirerID", self.acquirer_id)

        elm = etree.SubElement(root, "Directory")
        self._add_text_node(
            elm,
            "directoryDateTimestamp",
            utils.datetime_to_xml(self.directory_timestamp),
        )
        for country in self.issuers:
            node = etree.SubElement(elm, "Country")
            self._add_text_node(node, "countryNames", country.name)
            for issuer in country.issuers:
                issuer_node = etree.SubElement(node, "Issuer")
                self._add_text_node(issuer_node, "issuerID", issuer.id)
                self._add_text_node(issuer_node, "issuerName", issuer.name)

        return root

    @classmethod
    def deserialize(cls, document: etree._Document):
        issuers = []
        countries = cls._get_elements(document, "idx:Directory/idx:Country")
        for country_elm in countries:
            name_elm = cls._get_element(country_elm, "idx:countryNames")
            if name_elm is None:
                continue

            country = types.CountryIssuers(name=name_elm.text, issuers=[])
            for issuer_elm in cls._get_elements(country_elm, "idx:Issuer"):
                issuer_name = issuer_id = ""

                elm = cls._get_element(issuer_elm, "idx:issuerID")
                if elm is not None:
                    issuer_id = elm.text

                elm = cls._get_element(issuer_elm, "idx:issuerName")
                if elm is not None:
                    issuer_name = elm.text

                issuer = types.Issuer(id=issuer_id, name=issuer_name)
                country.issuers.append(issuer)

            issuers.append(country)

        return cls(
            create_timestamp=utils.xpath_datetime(document, "idx:createDateTimestamp"),
            acquirer_id=utils.xpath_text(document, "idx:Acquirer/idx:acquirerID"),
            directory_timestamp=utils.xpath_datetime(
                document, "idx:Directory/idx:directoryDateTimestamp"
            ),
            issuers=issuers,
        )

    @classmethod
    def _get_element(
        cls, element: etree._Element, path: str
    ) -> typing.Optional[etree._Element]:
        elements = cls._get_elements(element, path)
        if len(elements) == 1:
            return elements[0]
        elif len(elements) > 1:
            raise ValueError("Found multiple nodes for xpath %s" % path)
        return None

    @classmethod
    def _get_elements(cls, element, path: str) -> typing.List[etree._Element]:
        if element is None:
            return []
        found = element.xpath(path, namespaces={"idx": cls._namespace})
        return list(found)
