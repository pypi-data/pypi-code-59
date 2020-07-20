import typing
from datetime import datetime
from enum import Enum

import attr

from .saml2.response import AuthStatus


@attr.s(auto_attribs=True, slots=True)
class UserInformation:
    gender: typing.Optional[int] = None
    legallastname: typing.Optional[str] = None
    preferredlastname: typing.Optional[str] = None
    partnerlastname: typing.Optional[str] = None
    legallastnameprefix: typing.Optional[str] = None
    preferredlastnameprefix: typing.Optional[str] = None
    partnerlastnameprefix: typing.Optional[str] = None
    initials: typing.Optional[str] = None
    dateofbirth: typing.Optional[datetime] = None
    is18orolder: typing.Optional[bool] = None
    street: typing.Optional[str] = None
    houseno: typing.Optional[str] = None
    housenosuf: typing.Optional[str] = None
    addressextra: typing.Optional[str] = None
    postalcode: typing.Optional[str] = None
    city: typing.Optional[str] = None
    intaddressline1: typing.Optional[str] = None
    intaddressline2: typing.Optional[str] = None
    intaddressline3: typing.Optional[str] = None
    country: typing.Optional[str] = None
    telephone: typing.Optional[str] = None
    email: typing.Optional[str] = None

    _mapping = {
        "urn:nl:bvn:bankid:1.0:consumer.addressextra": "addressextra",
        "urn:nl:bvn:bankid:1.0:consumer.legallastname": "legallastname",
        "urn:nl:bvn:bankid:1.0:consumer.preferredlastname": "preferredlastname",
        "urn:nl:bvn:bankid:1.0:consumer.partnerlastname": "partnerlastname",
        "urn:nl:bvn:bankid:1.0:consumer.legallastnameprefix": "legallastnameprefix",
        "urn:nl:bvn:bankid:1.0:consumer.preferredlastnameprefix": "preferredlastnameprefix",
        "urn:nl:bvn:bankid:1.0:consumer.partnerlastnameprefix": "partnerlastnameprefix",
        "urn:nl:bvn:bankid:1.0:consumer.initials": "initials",
        "urn:nl:bvn:bankid:1.0:consumer.street": "street",
        "urn:nl:bvn:bankid:1.0:consumer.houseno": "houseno",
        "urn:nl:bvn:bankid:1.0:consumer.housenosuf": "housenosuf",
        "urn:nl:bvn:bankid:1.0:consumer.postalcode": "postalcode",
        "urn:nl:bvn:bankid:1.0:consumer.city": "city",
        "urn:nl:bvn:bankid:1.0:consumer.country": "country",
        "urn:nl:bvn:bankid:1.0:consumer.dateofbirth": "dateofbirth",
        "urn:nl:bvn:bankid:1.0:consumer.gender": "gender",
        "urn:nl:bvn:bankid:1.0:consumer.telephone": "telephone",
        "urn:nl:bvn:bankid:1.0:consumer.email": "email",
    }

    @classmethod
    def from_response(cls, attributes):
        obj = cls()
        for src, dst in cls._mapping.items():
            setattr(obj, dst, attributes.get(src))
        return obj


@attr.s(auto_attribs=True, slots=True)
class Transaction:
    redirect_url: str
    transaction_id: str


class TransactionStatus(Enum):
    """Represent the transaction status

    Status of the transaction: related to whether the transaction has been
    authenticated/authorized by the Consumer.
    """

    # The Consumer approved the transaction and the Issuer has confirmed this
    # approval.
    SUCCESS = "Success"

    # Final status not yet known. This is the initial status value for all
    # parties for all transactions.
    OPEN = "Open"

    # The transaction has not been approved; cancelled by the Consumer.
    CANCELLED = "Cancelled"

    # The transaction has not been approved within the BankID.expirationPeriod
    # set by the Merchant or the default BankID.expirationPeriod.
    EXPIRED = "Expired"

    # The transaction has not been approved; unknown reason
    FAILURE = "Failure"

    # NOTE: Part of the XSD, not of the documentation
    PENDING = "Pending"


@attr.s(auto_attribs=True, slots=True)
class Status:
    transaction_id: str
    transaction_status: TransactionStatus
    transaction_timestamp: datetime
    name_id: typing.Optional[str]
    user: typing.Optional[UserInformation]
    auth_status: typing.Optional[AuthStatus]


@attr.s(auto_attribs=True, slots=True)
class Issuer:
    id: str
    name: str


@attr.s(auto_attribs=True, slots=True)
class CountryIssuers:
    name: str
    issuers: typing.List[Issuer]
