# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailSettings(object):
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
        'bcc_email_addresses': 'list[BccEmailAddress]',
        'reply_email_address_override': 'str',
        'reply_email_name_override': 'str'
    }

    attribute_map = {
        'bcc_email_addresses': 'bccEmailAddresses',
        'reply_email_address_override': 'replyEmailAddressOverride',
        'reply_email_name_override': 'replyEmailNameOverride'
    }

    def __init__(self, bcc_email_addresses=None, reply_email_address_override=None, reply_email_name_override=None):  # noqa: E501
        """EmailSettings - a model defined in Swagger"""  # noqa: E501

        self._bcc_email_addresses = None
        self._reply_email_address_override = None
        self._reply_email_name_override = None
        self.discriminator = None

        if bcc_email_addresses is not None:
            self.bcc_email_addresses = bcc_email_addresses
        if reply_email_address_override is not None:
            self.reply_email_address_override = reply_email_address_override
        if reply_email_name_override is not None:
            self.reply_email_name_override = reply_email_name_override

    @property
    def bcc_email_addresses(self):
        """Gets the bcc_email_addresses of this EmailSettings.  # noqa: E501

        A list of email addresses that receive a copy of all email communications for an envelope. You can use this for archiving purposes.  # noqa: E501

        :return: The bcc_email_addresses of this EmailSettings.  # noqa: E501
        :rtype: list[BccEmailAddress]
        """
        return self._bcc_email_addresses

    @bcc_email_addresses.setter
    def bcc_email_addresses(self, bcc_email_addresses):
        """Sets the bcc_email_addresses of this EmailSettings.

        A list of email addresses that receive a copy of all email communications for an envelope. You can use this for archiving purposes.  # noqa: E501

        :param bcc_email_addresses: The bcc_email_addresses of this EmailSettings.  # noqa: E501
        :type: list[BccEmailAddress]
        """

        self._bcc_email_addresses = bcc_email_addresses

    @property
    def reply_email_address_override(self):
        """Gets the reply_email_address_override of this EmailSettings.  # noqa: E501

          # noqa: E501

        :return: The reply_email_address_override of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._reply_email_address_override

    @reply_email_address_override.setter
    def reply_email_address_override(self, reply_email_address_override):
        """Sets the reply_email_address_override of this EmailSettings.

          # noqa: E501

        :param reply_email_address_override: The reply_email_address_override of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._reply_email_address_override = reply_email_address_override

    @property
    def reply_email_name_override(self):
        """Gets the reply_email_name_override of this EmailSettings.  # noqa: E501

          # noqa: E501

        :return: The reply_email_name_override of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._reply_email_name_override

    @reply_email_name_override.setter
    def reply_email_name_override(self, reply_email_name_override):
        """Sets the reply_email_name_override of this EmailSettings.

          # noqa: E501

        :param reply_email_name_override: The reply_email_name_override of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._reply_email_name_override = reply_email_name_override

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EmailSettings, dict):
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
        if not isinstance(other, EmailSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
