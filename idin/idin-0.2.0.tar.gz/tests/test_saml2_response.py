from datetime import datetime

import pytz
from freezegun import freeze_time

from idin import xml
from idin.saml2.response import AuthStatus, AuthStatusCode, AuthStatusSubCode, Response

from .utils import get_file


@freeze_time("2015-01-01T09:30:47Z")
def test_parse_response(xmlsec_key):
    with open(get_file("datafiles/saml2_response.xml"), "rb") as fh:
        content = fh.read()

    document = xml.load(content)
    response = Response(document, xmlsec_key)

    assert response.get_issuers() == "1234"
    assert response.status == AuthStatus(
        code=AuthStatusCode.SUCCESS, subcode=AuthStatusSubCode.SUCCESS, message=None,
    )

    conditions = response.conditions
    assert len(conditions) == 1
    assert conditions[0].not_before == datetime(2015, 1, 1, 9, 30, 47, tzinfo=pytz.utc)
    assert conditions[0].not_on_or_after == datetime(
        2015, 1, 1, 9, 31, 17, 123000, tzinfo=pytz.utc
    )
    assert conditions[0].audience_restriction == ["NL69ZZZ123456780000"]
    assert response.get_attributes() == {
        "urn:nl:bvn:bankid:1.0:bankid.deliveredserviceid": "21952",
        "urn:nl:bvn:bankid:1.0:consumer.addressextra": "woonboot t.o. de Albert Heijn",
        "urn:nl:bvn:bankid:1.0:consumer.city": "Amsterdam",
        "urn:nl:bvn:bankid:1.0:consumer.country": "NL",
        "urn:nl:bvn:bankid:1.0:consumer.dateofbirth": "19850101",
        "urn:nl:bvn:bankid:1.0:consumer.gender": "1",
        "urn:nl:bvn:bankid:1.0:consumer.houseno": "33",
        "urn:nl:bvn:bankid:1.0:consumer.housenosuf": "bis",
        "urn:nl:bvn:bankid:1.0:consumer.initials": "JV",
        "urn:nl:bvn:bankid:1.0:consumer.legallastname": "Vries",
        "urn:nl:bvn:bankid:1.0:consumer.legallastnameprefix": "de",
        "urn:nl:bvn:bankid:1.0:consumer.partnerlastname": "Jansen",
        "urn:nl:bvn:bankid:1.0:consumer.postalcode": "1082MS",
        "urn:nl:bvn:bankid:1.0:consumer.preferredlastname": "Vries-Jansen",
        "urn:nl:bvn:bankid:1.0:consumer.preferredlastnameprefix": "de",
        "urn:nl:bvn:bankid:1.0:consumer.street": "Gustav Mahlerplein",
    }
