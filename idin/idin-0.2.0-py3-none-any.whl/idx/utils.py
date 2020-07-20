import typing
from datetime import datetime

import pytz
from lxml import etree

from idin import xsd

NSMAP = {
    "idx": "http://www.betaalvereniging.nl/iDx/messages/Merchant-Acquirer/1.0.0",
    "ds": "http://www.w3.org/2000/09/xmldsig#",
}


def utcnow():
    return datetime.utcnow().replace(tzinfo=pytz.utc)


def datetime_to_xml(value) -> str:
    """Return datetime object as string using ISO 8601.

    UTC time format (no daylight saving) in format YYYY-MM-DDThh:mm:ss.sssZ
    e.g. 2015-10-13T14:41:12.123Z

    - Merchants are allowed to use zero to three decimals behind the seconds.
      DateTimestamp in messages from the Routing Service will always have three
      decimals after the seconds
    - YYYY is the calendar year hh is 24-hour notation.
    - 12-hour notation must not be used

    Note that we use `+00:00` instead of `Z` for the timezone information. It
    should work
    """
    value = value.isoformat(timespec="milliseconds")
    if value.endswith("+00:00"):
        return value[:-6] + "Z"


def xpath_text(node, path):
    elm = xpath_elm(node, path)
    if elm is not None:
        return elm.text


def xpath_datetime(node, path) -> typing.Optional[datetime]:
    text = xpath_text(node, path)
    if text:
        return xsd.parse_datetime(text)
    return None


def xpath_elm(node, path):
    elm = node.xpath(path, namespaces=NSMAP)
    if len(elm) > 0:
        return elm[0]


def add_text_element(parent, name, text):
    node = etree.SubElement(parent, name, nsmap=NSMAP)
    node.text = text
