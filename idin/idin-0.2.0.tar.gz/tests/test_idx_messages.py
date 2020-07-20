import os
from datetime import datetime

from lxml import etree

from idin import idx, types, xml, xsd
from idin.idx.utils import utcnow


def test_transaction_request_serialize(xmlsec_key):

    container = etree.Element("foobar")
    message = idx.TransactionRequest(
        issuer_id="BANKNL2U",
        merchant_id="1234567890",
        merchant_sub_id="1",
        merchant_return_url="https://merchantwebsite.nl/returnPage.php?param1=true&param2=3",
        language="nl",
        entrance_code="1234567890abcdefghijABCDEFGHIJ1234567890",
        container=container,
    )
    document = message.serialize()

    xml.sign(document, xmlsec_key)
    document = etree.fromstring(etree.tostring(document))

    _assert_valid_idx_document(document)

    xml.verify(document, xmlsec_key)

    result = idx.TransactionRequest.deserialize(document)
    assert result.issuer_id == message.issuer_id
    assert result.merchant_id == message.merchant_id
    assert result.merchant_sub_id == message.merchant_sub_id
    assert result.merchant_return_url == message.merchant_return_url
    assert result.language == message.language
    assert result.entrance_code == message.entrance_code


def test_transaction_response_serialize(xmlsec_key):

    timestamp = utcnow()
    message = idx.TransactionResponse(
        acquirer_id="1234",
        issuer_authentication_url="https://issuer.nl?param=true&amp;paramRandom=123456789012345678901234567890",
        transaction_id="1234123456789012",
        transaction_timestamp=timestamp,
    )
    document = message.serialize()
    xml.sign(document, xmlsec_key)
    document = etree.fromstring(etree.tostring(document))

    _assert_valid_idx_document(document)

    xml.verify(document, xmlsec_key)

    result = idx.TransactionResponse.deserialize(document)
    assert result.acquirer_id == message.acquirer_id
    assert result.issuer_authentication_url == message.issuer_authentication_url
    assert result.transaction_id == message.transaction_id
    _compare_timestamps(result.transaction_timestamp, message.transaction_timestamp)


def test_status_request_serialize(xmlsec_key):

    message = idx.StatusRequest(
        merchant_id="1234567890",
        merchant_sub_id="12345",
        transaction_id="1234123456789012",
    )
    document = message.serialize()
    xml.sign(document, xmlsec_key)
    document = etree.fromstring(etree.tostring(document))

    _assert_valid_idx_document(document)

    xml.verify(document, xmlsec_key)

    result = idx.StatusRequest.deserialize(document)
    assert result.merchant_id == message.merchant_id
    assert result.merchant_sub_id == message.merchant_sub_id
    assert result.transaction_id == message.transaction_id


def test_status_response_serialize(xmlsec_key):
    container = etree.Element("foobar")

    timestamp = utcnow()
    message = idx.StatusResponse(
        acquirer_id="1234",
        transaction_id="1234567890123456",
        transaction_status="Open",
        transaction_status_timestamp=timestamp,
        container=container,
    )
    document = message.serialize()
    xml.sign(document, xmlsec_key)

    document = etree.fromstring(etree.tostring(document))

    _assert_valid_idx_document(document)

    xml.verify(document, xmlsec_key)

    result = idx.StatusResponse.deserialize(document)
    assert result.acquirer_id == message.acquirer_id
    assert result.transaction_id == message.transaction_id
    assert result.transaction_status == message.transaction_status
    _compare_timestamps(
        result.transaction_status_timestamp, message.transaction_status_timestamp
    )


def test_directory_response_serialize(xmlsec_key):
    container = etree.Element("foobar")

    message = idx.DirectoryResponse(
        acquirer_id="1234",
        issuers=[
            types.CountryIssuers(
                name="Nederland",
                issuers=[
                    types.Issuer(id="BANKNL2U", name="Bank 1"),
                    types.Issuer(id="BANANL2U", name="Bank 2"),
                    types.Issuer(id="BANBNL2UXXX", name="Bank 3"),
                    types.Issuer(id="BANCNL2U", name="Bank 4"),
                ],
            ),
            types.CountryIssuers(
                name="België/Belgiqu",
                issuers=[types.Issuer(id="BANKBE2U", name="Banque 1"),],
            ),
        ],
    )
    document = message.serialize()
    xml.sign(document, xmlsec_key)

    document = etree.fromstring(etree.tostring(document))

    _assert_valid_idx_document(document)

    xml.verify(document, xmlsec_key)

    result = idx.DirectoryResponse.deserialize(document)
    assert result.acquirer_id == message.acquirer_id
    _compare_timestamps(result.directory_timestamp, message.directory_timestamp)
    _compare_timestamps(result.create_timestamp, message.create_timestamp)


def _compare_timestamps(obj1: datetime, obj2: datetime):
    value1 = xsd.parse_datetime(obj1.isoformat(timespec="milliseconds"))
    value2 = xsd.parse_datetime(obj2.isoformat(timespec="milliseconds"))
    assert value1 == value2


def _assert_valid_idx_document(document) -> None:
    path = os.path.join(os.path.dirname(__file__), "idx.merchant-acquirer.1.0.xsd")
    xmlschema_doc = etree.parse(path)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xmlschema.assertValid(document)
