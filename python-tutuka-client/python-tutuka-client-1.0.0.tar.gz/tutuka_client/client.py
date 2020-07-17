from datetime import datetime
from xmlrpc import client as xmlrpc_client

import requests

from tutuka_client.errors import TutukaException
from tutuka_client.response_codes import (
    ERROR_RESPONSE_CODES_EXCEPTIONS,
    SUCCESS_RESPONSE_CODES,
)
from tutuka_client.stop_reasons import CARD_STOP_REASONS
from tutuka_client.utils import hmac_with_sha1, normalize_argument


class LocalApiClient(object):
    def __init__(self, terminal_id, password, host, path, http_client=requests):
        self.terminal_id = terminal_id
        self.password = password
        self.host = host
        self.path = path
        self.session = http_client.Session()
        self.session.headers.update({'Content-Type': 'application/xml'})

    def create_linked_card(
        self,
        reference_id: str,
        first_name: str,
        last_name: str,
        id_or_passport: str,
        expiry_date: datetime,
        transaction_id: str,
        cell_phone_number: str = '',
    ):
        return self._execute(
            method_name='CreateLinkedCard',
            arguments=[
                self.terminal_id,
                reference_id,
                first_name,
                last_name,
                id_or_passport,
                cell_phone_number,
                expiry_date,
                transaction_id,
            ],
        )

    def link_card(
        self,
        reference_id: str,
        card_identifier: str,
        first_name: str,
        last_name: str,
        id_or_passport: str,
        transaction_id: str,
        cell_phone_number: str = '',
    ):
        return self._execute(
            method_name='LinkCard',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                first_name,
                last_name,
                id_or_passport,
                cell_phone_number,
                transaction_id,
            ],
        )

    def order_card(
        self,
        title: str,
        last_name: str,
        transaction_id: str,
        initials: str = '',
        address1: str = '',
        address2: str = '',
        address3: str = '',
        address4: str = '',
        address5: str = '',
        additional_data: str = '',
    ):
        return self._execute(
            method_name='OrderCard',
            arguments=[
                self.terminal_id,
                title,
                initials,
                last_name,
                address1,
                address2,
                address3,
                address4,
                address5,
                additional_data,
                transaction_id,
            ],
        )

    def order_card_with_pin_block(  # noqa: WPS211
        self,
        title: str,
        last_name: str,
        pin_block: str,
        transaction_id: str,
        initials: str = '',
        address1: str = '',
        address2: str = '',
        address3: str = '',
        address4: str = '',
        address5: str = '',
        additional_data: str = '',
    ):
        return self._execute(
            method_name='OrderCardWithPinBlock',
            arguments=[
                self.terminal_id,
                title,
                initials,
                last_name,
                address1,
                address2,
                address3,
                address4,
                address5,
                additional_data,
                pin_block,
                transaction_id,
            ],
        )

    def activate_card(self, card_identifier: str, transaction_id: str):
        return self._execute(
            method_name='ActivateCard',
            arguments=[
                self.terminal_id,
                card_identifier,
                transaction_id,
            ],
        )

    def get_active_linked_cards(self, reference_id: str, transaction_id: str):
        return self._execute(
            method_name='GetActiveLinkedCards',
            arguments=[
                self.terminal_id,
                reference_id,
                transaction_id,
            ],
        )

    def change_pin(
        self,
        reference_id: str,
        card_identifier: str,
        new_pin: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='ChangePin',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                new_pin,
                transaction_id,
            ],
        )

    def reset_pin(self, reference_id: str, card_identifier: str, transaction_id: str):
        return self._execute(
            method_name='ResetPin',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                transaction_id,
            ],
        )

    def update_bearer(
        self,
        reference_id: str,
        card_identifier: str,
        first_name: str,
        last_name: str,
        id_or_passport: str,
        cell_phone_number: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='UpdateBearer',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                first_name,
                last_name,
                id_or_passport,
                cell_phone_number,
                transaction_id,
            ],
        )

    def transfer_link(
        self,
        reference_id: str,
        old_card_identifier: str,
        new_card_identifier: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='TransferLink',
            arguments=[
                self.terminal_id,
                reference_id,
                old_card_identifier,
                new_card_identifier,
                transaction_id,
            ],
        )

    def stop_card(
        self,
        reference_id: str,
        card_identifier: str,
        reason: str,
        note: str,
        transaction_id: str,
    ):
        if reason not in CARD_STOP_REASONS:
            raise TutukaException(
                'invalid card stop reason: {reason}'.format(reason=reason),
            )

        return self._execute(
            method_name='StopCard',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                CARD_STOP_REASONS[reason],
                note,
                transaction_id,
            ],
        )

    def unstop_card(
        self,
        reference_id: str,
        card_identifier: str,
        note: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='UnstopCard',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                note,
                transaction_id,
            ],
        )

    def status(self, reference_id: str, card_identifier: str, transaction_id: str):
        return self._execute(
            method_name='Status',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                transaction_id,
            ],
        )

    def set3d_secure_code(
        self,
        reference_id: str,
        card_identifier: str,
        code: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='Set3dSecureCode',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                code,
                transaction_id,
            ],
        )

    def update_cvv(
        self,
        reference_id: str,
        card_identifier: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='UpdateCVV',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                transaction_id,
            ],
        )

    def retire_card(
        self,
        reference_id: str,
        card_identifier: str,
        transaction_id: str,
    ):
        return self._execute(
            method_name='RetireCard',
            arguments=[
                self.terminal_id,
                reference_id,
                card_identifier,
                transaction_id,
            ],
        )

    def _generate_checksum(self, method_name: str, arguments: list = None):
        if arguments is None:
            arguments = []
        concat = ''.join([normalize_argument(argument) for argument in arguments])
        string_to_sign = method_name + concat
        return hmac_with_sha1(
            self.password.encode('utf-8'),
            string_to_sign.encode('utf-8'),
        )

    @classmethod
    def _dumps(cls, method_name: str, arguments: list):
        return xmlrpc_client.dumps(tuple(arguments), method_name)

    @classmethod
    def _loads(cls, response: bytes):
        return xmlrpc_client.loads(response)

    def _execute(self, method_name: str, arguments: list):
        arguments.append(datetime.now())
        checksum = self._generate_checksum(method_name, arguments)
        arguments.append(checksum)
        body = self._dumps(method_name, arguments)
        response = self.session.post(
            '{host}{path}'.format(host=self.host, path=self.path), data=body,
        )
        loads_result = self._loads(response.content)[0][0]
        if 'resultCode' not in loads_result:
            raise TutukaException('no result code')
        result_code = loads_result['resultCode']
        if result_code not in SUCCESS_RESPONSE_CODES.values():
            result_text = loads_result['resultText']
            error = ERROR_RESPONSE_CODES_EXCEPTIONS[str(result_code)]
            raise error(result_text, result_code)
        return loads_result
