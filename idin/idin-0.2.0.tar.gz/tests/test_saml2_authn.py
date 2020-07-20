from idin import ServiceID
from idin.saml2 import authn


def test_autnrequest():

    request = authn.AuthnRequest(
        issuer="TEST", return_url="https://example.org/foo", service_id=ServiceID.all()
    )
    document = request.serialize()
    # print(etree.tostring(document, pretty_print=True).decode('utf-8'))
