import typing
from datetime import datetime
from enum import Enum

import attr
import pytz
import xmlsec
from cached_property import cached_property
from lxml import etree

from idin import xml, xsd

from .exceptions import RequesterException, ValidationError

NSMAP = {
    "saml": "urn:oasis:names:tc:SAML:2.0:assertion",
    "samlp": "urn:oasis:names:tc:SAML:2.0:protocol",
}


@attr.s(auto_attribs=True)
class AuthStatus:
    code: typing.Optional[str]
    subcode: typing.Optional[str]
    message: typing.Optional[str]


@attr.s(auto_attribs=True)
class Condition:
    """Represent an Assertion Condition"""

    not_before: typing.Optional[datetime]
    not_on_or_after: typing.Optional[datetime]
    audience_restriction: typing.List[str]
    one_time_use: bool


class AuthStatusCode(Enum):
    REQUESTER = "urn:oasis:names:tc:SAML:2.0:status:Requester"
    SUCCESS = "urn:oasis:names:tc:SAML:2.0:status:Success"


class AuthStatusSubCode(Enum):
    INCOMPLETE_ATTRIBUTE_SET = "urn:nl:bvn:bankid:1.0:status:IncompleteAttributeSet"
    INVALID_ATTR_NAME_OR_VALUE = (
        "urn:oasis:names:tc:SAML:2.0:status:InvalidAttrNameOrValue"
    )
    MISMATCH_WITH_IDX = "urn:nl:bvn:bankid:1.0:status:MismatchWithIDx"
    REQUEST_DENIED = "urn:oasis:names:tc:SAML:2.0:status:RequestDenied"
    REQUEST_UNSUPPORTED = "urn:oasis:names:tc:SAML:2.0:status:RequestUnsupported"
    SUCCESS = "urn:nl:bvn:bankid:1.0:status:Success"


class Response:
    def __init__(self, document: etree._Document, key: xmlsec.Key):
        self._document = document
        self._key = key

        self.validate()

    def validate(self):
        if self.status.code == AuthStatusCode.REQUESTER:
            raise RequesterException(self.status.message, code=self.status.subcode)

        assertion_elm = self._get_element(self._document, "saml:Assertion")
        if assertion_elm is None:
            raise ValueError("No saml:Assertion element found")

        xml.verify(self._document, key=None, id_elements=[assertion_elm])

        self.validate_conditions()

    def validate_conditions(self):
        current_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        for condition in self.conditions:

            if condition.not_before is not None and current_time < condition.not_before:
                raise ValidationError("The NotBefore condition is not met")
            if (
                condition.not_on_or_after is not None
                and current_time >= condition.not_on_or_after
            ):
                raise ValidationError("The NotOnOrAfter condition is not met")

    def get_issuers(self) -> typing.Optional[str]:
        element = self._get_element(self._document, "saml:Issuer")
        if element is not None:
            return element.text.strip()
        return None

    @cached_property
    def status(self) -> AuthStatus:
        """Deserialize the samlp:Status element"""
        status = AuthStatus(code=None, subcode=None, message=None)

        status_elm = self._get_element(self._document, "samlp:Status")

        if status_elm is None:
            raise ValueError("No status element found")

        statuscode_elm = self._get_element(status_elm, "samlp:StatusCode")
        if statuscode_elm is not None:
            status.code = AuthStatusCode(statuscode_elm.attrib.get("Value"))

            # Find optional subcode
            substatuscode_elm = self._get_element(statuscode_elm, "samlp:StatusCode")
            if substatuscode_elm is not None:
                status.subcode = AuthStatusSubCode(
                    substatuscode_elm.attrib.get("Value")
                )

        # Process the optional StatusMessage field
        statusmsg_elm = self._get_element(status_elm, "samlp:StatusMessage")
        if statusmsg_elm is not None:
            status.message = statusmsg_elm.attrib.get("Value")

        return status

    @cached_property
    def name_id(self) -> str:
        encrypted_elm = self._get_element(
            self._document, "saml:Assertion/saml:Subject/saml:EncryptedID"
        )
        if encrypted_elm is not None:
            elm = xml.decrypt(encrypted_elm, self._key)
        else:
            elm = self._get_element(
                self._document, "saml:Assertion/saml:Subject/saml:NameID"
            )
        return elm.text

    @cached_property
    def conditions(self) -> typing.List[Condition]:
        """Deserialize the saml:Conditions element

        TODO: Add support for the ProxyRestriction sub-element.
        """
        conditions: typing.List[Condition] = []
        elements = self._get_elements(self._document, "saml:Assertion/saml:Conditions")
        for element in elements:
            condition = Condition(
                not_before=None,
                not_on_or_after=None,
                audience_restriction=[],
                one_time_use=False,
            )
            conditions.append(condition)

            value = element.attrib.get("NotBefore")
            if value is not None:
                condition.not_before = xsd.parse_datetime(value)

            value = element.attrib.get("NotOnOrAfter")
            if value is not None:
                condition.not_on_or_after = xsd.parse_datetime(value)

            audiences = self._get_elements(
                element, "saml:AudienceRestriction/saml:Audience"
            )
            condition.audience_restriction = [a.text.strip() for a in audiences]

        return conditions

    def get_attributes(self) -> typing.Dict[str, typing.Any]:
        """Return a dict with all attributes in the assertion"""
        result = self._get_attributes()
        encrypted = self._get_encrypted_attributes()
        result.update(encrypted)
        return result

    def _get_attributes(self) -> typing.Dict[str, str]:
        """Return a dict with all key, values from the saml:Attribute"""
        elements = self._get_elements(
            self._document, "saml:Assertion/saml:AttributeStatement/saml:Attribute"
        )
        result = {}
        for element in elements:
            key, value = self._deserialize_attribute(element)
            result[key] = value
        return result

    def _get_encrypted_attributes(self) -> typing.Dict[str, str]:
        """Return a dict with all key, values from the saml:EncryptedAttribute"""
        elements = self._get_elements(
            self._document,
            "saml:Assertion/saml:AttributeStatement/saml:EncryptedAttribute",
        )
        result: typing.Dict[str, str] = {}
        for encrypted_elm in elements:
            element = xml.decrypt(encrypted_elm, self._key)

            key, value = self._deserialize_attribute(element)
            result[key] = value
        return result

    def _deserialize_attribute(self, element: etree._Element) -> typing.Tuple[str, str]:
        """Return the key and value from a saml:Attribute element"""
        key = element.attrib.get("Name")
        value = ""
        value_element = self._get_element(element, "saml:AttributeValue")
        if value_element is not None:
            value = value_element.text
        return key, value

    def _get_element(
        self, element: etree._Element, xpath: str
    ) -> typing.Optional[etree._Element]:
        elements = self._get_elements(element, xpath)
        if len(elements) == 1:
            return elements[0]
        elif len(elements) > 1:
            raise ValueError("Found multiple nodes for xpath %s" % xpath)
        return None

    def _get_elements(self, element, xpath) -> typing.List[etree._Element]:
        if element is None:
            return []
        found = element.xpath(xpath, namespaces=NSMAP)
        return list(found)
