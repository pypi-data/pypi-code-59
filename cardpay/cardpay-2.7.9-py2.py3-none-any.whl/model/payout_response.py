# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cardpay.model.payout_payment_data import PayoutPaymentData  # noqa: F401,E501
from cardpay.model.payout_response_card_account import (
    PayoutResponseCardAccount,
)  # noqa: F401,E501
from cardpay.model.payout_response_cryptocurrency_account import (
    PayoutResponseCryptocurrencyAccount,
)  # noqa: F401,E501
from cardpay.model.payout_response_customer import (
    PayoutResponseCustomer,
)  # noqa: F401,E501
from cardpay.model.payout_response_e_wallet_account import (
    PayoutResponseEWalletAccount,
)  # noqa: F401,E501
from cardpay.model.payout_response_payout_data import (
    PayoutResponsePayoutData,
)  # noqa: F401,E501
from cardpay.model.transaction_response_merchant_order import (
    TransactionResponseMerchantOrder,
)  # noqa: F401,E501


class PayoutResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "card_account": "PayoutResponseCardAccount",
        "cryptocurrency_account": "PayoutResponseCryptocurrencyAccount",
        "customer": "PayoutResponseCustomer",
        "ewallet_account": "PayoutResponseEWalletAccount",
        "payment_data": "PayoutPaymentData",
        "payout_data": "PayoutResponsePayoutData",
        "payment_method": "str",
        "merchant_order": "TransactionResponseMerchantOrder",
    }

    attribute_map = {
        "card_account": "card_account",
        "cryptocurrency_account": "cryptocurrency_account",
        "customer": "customer",
        "ewallet_account": "ewallet_account",
        "payment_data": "payment_data",
        "payout_data": "payout_data",
        "payment_method": "payment_method",
        "merchant_order": "merchant_order",
    }

    def __init__(
        self,
        card_account=None,
        cryptocurrency_account=None,
        customer=None,
        ewallet_account=None,
        payment_data=None,
        payout_data=None,
        payment_method=None,
        merchant_order=None,
    ):  # noqa: E501
        """PayoutResponse - a model defined in Swagger"""  # noqa: E501

        self._card_account = None
        self._cryptocurrency_account = None
        self._customer = None
        self._ewallet_account = None
        self._payment_data = None
        self._payout_data = None
        self._payment_method = None
        self._merchant_order = None
        self.discriminator = None

        if card_account is not None:
            self.card_account = card_account
        if cryptocurrency_account is not None:
            self.cryptocurrency_account = cryptocurrency_account
        if customer is not None:
            self.customer = customer
        if ewallet_account is not None:
            self.ewallet_account = ewallet_account
        if payment_data is not None:
            self.payment_data = payment_data
        self.payout_data = payout_data
        if payment_method is not None:
            self.payment_method = payment_method
        if merchant_order is not None:
            self.merchant_order = merchant_order

    @property
    def card_account(self):
        """Gets the card_account of this PayoutResponse.  # noqa: E501

        Card account data *(for BANKCARD method only)*  # noqa: E501

        :return: The card_account of this PayoutResponse.  # noqa: E501
        :rtype: PayoutResponseCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this PayoutResponse.

        Card account data *(for BANKCARD method only)*  # noqa: E501

        :param card_account: The card_account of this PayoutResponse.  # noqa: E501
        :type: PayoutResponseCardAccount
        """

        self._card_account = card_account

    @property
    def cryptocurrency_account(self):
        """Gets the cryptocurrency_account of this PayoutResponse.  # noqa: E501

        Cryptocurrency account data *(for BITCOIN method only)*  # noqa: E501

        :return: The cryptocurrency_account of this PayoutResponse.  # noqa: E501
        :rtype: PayoutResponseCryptocurrencyAccount
        """
        return self._cryptocurrency_account

    @cryptocurrency_account.setter
    def cryptocurrency_account(self, cryptocurrency_account):
        """Sets the cryptocurrency_account of this PayoutResponse.

        Cryptocurrency account data *(for BITCOIN method only)*  # noqa: E501

        :param cryptocurrency_account: The cryptocurrency_account of this PayoutResponse.  # noqa: E501
        :type: PayoutResponseCryptocurrencyAccount
        """

        self._cryptocurrency_account = cryptocurrency_account

    @property
    def customer(self):
        """Gets the customer of this PayoutResponse.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this PayoutResponse.  # noqa: E501
        :rtype: PayoutResponseCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PayoutResponse.

        Customer data  # noqa: E501

        :param customer: The customer of this PayoutResponse.  # noqa: E501
        :type: PayoutResponseCustomer
        """

        self._customer = customer

    @property
    def ewallet_account(self):
        """Gets the ewallet_account of this PayoutResponse.  # noqa: E501

        eWallet account data *(for payout methods only)*  # noqa: E501

        :return: The ewallet_account of this PayoutResponse.  # noqa: E501
        :rtype: PayoutResponseEWalletAccount
        """
        return self._ewallet_account

    @ewallet_account.setter
    def ewallet_account(self, ewallet_account):
        """Sets the ewallet_account of this PayoutResponse.

        eWallet account data *(for payout methods only)*  # noqa: E501

        :param ewallet_account: The ewallet_account of this PayoutResponse.  # noqa: E501
        :type: PayoutResponseEWalletAccount
        """

        self._ewallet_account = ewallet_account

    @property
    def payment_data(self):
        """Gets the payment_data of this PayoutResponse.  # noqa: E501

        Payment data  # noqa: E501

        :return: The payment_data of this PayoutResponse.  # noqa: E501
        :rtype: PayoutPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this PayoutResponse.

        Payment data  # noqa: E501

        :param payment_data: The payment_data of this PayoutResponse.  # noqa: E501
        :type: PayoutPaymentData
        """

        self._payment_data = payment_data

    @property
    def payout_data(self):
        """Gets the payout_data of this PayoutResponse.  # noqa: E501

        Payout data  # noqa: E501

        :return: The payout_data of this PayoutResponse.  # noqa: E501
        :rtype: PayoutResponsePayoutData
        """
        return self._payout_data

    @payout_data.setter
    def payout_data(self, payout_data):
        """Sets the payout_data of this PayoutResponse.

        Payout data  # noqa: E501

        :param payout_data: The payout_data of this PayoutResponse.  # noqa: E501
        :type: PayoutResponsePayoutData
        """
        if payout_data is None:
            raise ValueError(
                "Invalid value for `payout_data`, must not be `None`"
            )  # noqa: E501

        self._payout_data = payout_data

    @property
    def payment_method(self):
        """Gets the payment_method of this PayoutResponse.  # noqa: E501

        Used payment method type name from payment methods list  # noqa: E501

        :return: The payment_method of this PayoutResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PayoutResponse.

        Used payment method type name from payment methods list  # noqa: E501

        :param payment_method: The payment_method of this PayoutResponse.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def merchant_order(self):
        """Gets the merchant_order of this PayoutResponse.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this PayoutResponse.  # noqa: E501
        :rtype: TransactionResponseMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this PayoutResponse.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this PayoutResponse.  # noqa: E501
        :type: TransactionResponseMerchantOrder
        """

        self._merchant_order = merchant_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(PayoutResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayoutResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
