import os

import attr
import pytest
import xmlsec

from idin import Certificate


def load_key(filename) -> bytes:
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "keys", filename)
    with open(path, "rb") as fh:
        return fh.read()


@pytest.fixture
def xmlsec_key(merchant_cert):
    return merchant_cert.key


@pytest.fixture
def merchant_cert():
    return Certificate(
        private_key=load_key("key.pem"), certificate=load_key("cert.pem")
    )


@pytest.fixture
def acquirer_cert():
    return Certificate(
        private_key=load_key("acquirer_key.pem"),
        certificate=load_key("acquirer_cert.pem"),
    )
