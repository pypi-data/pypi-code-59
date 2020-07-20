import pytest
from freezegun import freeze_time

import idin

from .utils import get_file


@freeze_time("2015-01-01T09:30:47.1Z")
def test_client(merchant_cert, acquirer_cert, requests_mock):
    with open(get_file("datafiles/idx_trx_response.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())

    client = idin.Client(
        language="nl",
        merchant_id="1234",
        merchant_sub_id=None,
        endpoint="https://localhost:8000/idin",
        certificate=merchant_cert,
        certificate_acquirer=acquirer_cert,
    )
    transaction = client.start_transaction(
        issuer="BANK",
        entrance_code=None,
        service_id=idin.ServiceID.all(),
        merchant_return_url="https://example.org/idin-return",
    )
    assert transaction.redirect_url
    assert transaction.transaction_id

    with open(get_file("datafiles/idx_status_response.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())
    status = client.get_status(transaction_id=transaction.transaction_id)
    assert status.auth_status.code == idin.AuthStatusCode.SUCCESS
    assert status.auth_status.subcode == idin.AuthStatusSubCode.SUCCESS

    # test all mappings
    assert status.user.addressextra == "woonboot t.o. de Albert Heijn"
    assert status.user.city == "Amsterdam"
    assert status.user.country == "NL"
    assert status.user.dateofbirth == "19850101"
    assert status.user.gender == "1"
    assert status.user.houseno == "33"
    assert status.user.housenosuf == "bis"
    assert status.user.initials == "JV"
    assert status.user.legallastname == "Vries"
    assert status.user.legallastnameprefix == "de"
    assert status.user.partnerlastname == "Jansen"
    assert status.user.postalcode == "1082MS"
    assert status.user.preferredlastname == "Vries-Jansen"
    assert status.user.preferredlastnameprefix == "de"
    assert status.user.street == "Gustav Mahlerplein"


@freeze_time("2015-01-01T09:30:46.9Z")
def test_condition_not_before(merchant_cert, acquirer_cert, requests_mock):
    with open(get_file("datafiles/idx_status_response.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())

    client = idin.Client(
        language="nl",
        merchant_id="1234",
        merchant_sub_id=None,
        endpoint="https://localhost:8000/idin",
        certificate=merchant_cert,
        certificate_acquirer=acquirer_cert,
    )

    with pytest.raises(idin.ValidationError):
        status = client.get_status(transaction_id="foobar")


@freeze_time("2015-01-01T09:39:46.9Z")
def test_condition_not_on_or_after(merchant_cert, acquirer_cert, requests_mock):
    with open(get_file("datafiles/idx_status_response.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())

    client = idin.Client(
        language="nl",
        merchant_id="1234",
        merchant_sub_id=None,
        endpoint="https://localhost:8000/idin",
        certificate=merchant_cert,
        certificate_acquirer=acquirer_cert,
    )

    with pytest.raises(idin.ValidationError):
        status = client.get_status(transaction_id="foobar")


def test_client_denied(merchant_cert, acquirer_cert, requests_mock):

    client = idin.Client(
        language="nl",
        merchant_id="1234",
        merchant_sub_id=None,
        endpoint="https://localhost:8000/idin",
        certificate=merchant_cert,
        certificate_acquirer=acquirer_cert,
    )

    with open(get_file("datafiles/idx_status_response_denied.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())
    with pytest.raises(idin.RequesterException) as exc:
        client.get_status(transaction_id="0000001000000001")
    assert exc.value.code == idin.AuthStatusSubCode.REQUEST_DENIED


def test_client_error(merchant_cert, acquirer_cert, requests_mock):

    client = idin.Client(
        language="nl",
        merchant_id="1234",
        merchant_sub_id=None,
        endpoint="https://localhost:8000/idin",
        certificate=merchant_cert,
        certificate_acquirer=acquirer_cert,
    )

    with open(get_file("datafiles/idx_status_response_error.xml"), "rb") as fh:
        requests_mock.post("https://localhost:8000/idin", content=fh.read())
    with pytest.raises(idin.IdinException) as exc:
        client.get_status(transaction_id="0000001000000001")
    assert exc.value.code == "SO1000"
    assert (
        exc.value.consumer_message
        == "Het is op dit moment niet mogelijk om iDIN te gebruiken. Probeer het later nog een keer."
    )
