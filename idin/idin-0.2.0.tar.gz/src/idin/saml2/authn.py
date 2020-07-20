from lxml import etree
from lxml.builder import ElementMaker

from idin.idx.utils import datetime_to_xml, utcnow

NSMAP = {
    "samlp": "urn:oasis:names:tc:SAML:2.0:protocol",
    "saml": "urn:oasis:names:tc:SAML:2.0:assertion",
}


class AuthnRequest:
    def __init__(self, issuer: str, service_id: int, return_url: str):
        self.return_url = return_url
        self.issuer = issuer
        self.service_id = service_id

    def serialize(self):
        samlp = ElementMaker(namespace=NSMAP["samlp"], nsmap=NSMAP)
        saml = ElementMaker(namespace=NSMAP["saml"])
        elm = samlp.AuthnRequest(
            {
                "Version": "2.0",
                "ProtocolBinding": "nl:bvn:bankid:1.0:protocol:iDx",
                "AttributeConsumingServiceIndex": str(self.service_id),
                "AssertionConsumerServiceURL": self.return_url,
                "IssueInstant": datetime_to_xml(utcnow()),
                "ID": "REF1234567890",
            },
            saml.Issuer(self.issuer),
            samlp.RequestedAuthnContext(
                {"Comparison": "minimum",},
                saml.AuthnContextClassRef("nl:bvn:bankid:1.0:loa3"),
            ),
        )
        return elm
