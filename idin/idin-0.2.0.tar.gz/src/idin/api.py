import typing
import uuid

import requests
from lxml import etree

from idin import idx, saml2, types, xml
from idin.certificate import Certificate


class Client:
    def __init__(
        self,
        *,
        language: str,
        merchant_id: str,
        endpoint: str,
        certificate: Certificate,
        certificate_acquirer: Certificate,
        merchant_sub_id: typing.Optional[str] = None,
    ):
        self.merchant_id = merchant_id
        self.merchant_sub_id = merchant_sub_id or "0"
        self.language = language
        self.endpoint = endpoint
        self._certificate = certificate
        self._certificate_acquirer = certificate_acquirer

    def get_issuers(self) -> typing.List[types.CountryIssuers]:
        """Return the available issuers.

        Note that IDIN recommends that the return value is cached for +/- 24
        hours since the list of issuers don't change often.

        """
        message = idx.DirectoryRequest(
            merchant_id=self.merchant_id, merchant_sub_id=self.merchant_sub_id,
        )

        document = self._do_request(message)
        response = idx.DirectoryResponse.deserialize(document)
        return response.issuers

    def start_transaction(
        self,
        issuer: str,
        service_id: int,
        merchant_return_url: str,
        entrance_code: typing.Optional[str] = None,
        expiration_period: str = "PT5M",
    ) -> types.Transaction:
        """Start a new IDIN transaction

        issuer
        entrance_code
        expiration_period

        """
        if not entrance_code:
            entrance_code = uuid.uuid4().hex

        auth_request = saml2.AuthnRequest(
            issuer=self.merchant_id,
            service_id=service_id,
            return_url=merchant_return_url,
        )

        message = idx.TransactionRequest(
            issuer_id=issuer,
            merchant_id=self.merchant_id,
            merchant_sub_id=self.merchant_sub_id,
            merchant_return_url=merchant_return_url,
            language=self.language,
            entrance_code=entrance_code,
            container=auth_request.serialize(),
        )

        document = self._do_request(message)
        response = idx.TransactionResponse.deserialize(document)

        return types.Transaction(
            redirect_url=response.issuer_authentication_url,
            transaction_id=response.transaction_id,
        )

    def get_status(self, transaction_id: str) -> types.Status:
        """The status requests uses SAML2 as data exchange format for the user
        information.

        """
        message = idx.StatusRequest(
            merchant_id=self.merchant_id,
            merchant_sub_id=self.merchant_sub_id,
            transaction_id=transaction_id,
        )

        document = self._do_request(message)
        response = idx.StatusResponse.deserialize(document)

        result = types.Status(
            transaction_id=response.transaction_id,
            transaction_status=types.TransactionStatus(response.transaction_status),
            transaction_timestamp=response.transaction_status_timestamp,
            auth_status=None,
            name_id=None,
            user=None,
        )

        # The container element in the response is only availavble if the
        # transaction status = Success. It contains a SAML 2.0 Response
        # element.
        if result.transaction_status == types.TransactionStatus.SUCCESS:
            saml2_response = saml2.Response(response.container, self._certificate.key)
            result.auth_status = saml2_response.status
            result.name_id = saml2_response.name_id
            result.user = types.UserInformation.from_response(
                saml2_response.get_attributes()
            )
        return result

    def _do_request(self, message) -> etree._Document:
        document = message.serialize()
        xml.sign(document, self._certificate.key)

        content = etree.tostring(document).decode("utf-8")

        response = requests.post(self.endpoint, data=content)
        response.raise_for_status()

        content = response.content.decode("utf-8")
        document = xml.load(response.content)

        xml.verify(document, self._certificate_acquirer.key)

        if document.tag == idx.ErrorResponse.qname():
            obj = idx.ErrorResponse.deserialize(document)
            raise obj.as_exception()

        return document
