# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountPasswordStrengthType(object):
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
        'options': 'list[AccountPasswordStrengthTypeOption]'
    }

    attribute_map = {
        'options': 'options'
    }

    def __init__(self, options=None):  # noqa: E501
        """AccountPasswordStrengthType - a model defined in Swagger"""  # noqa: E501

        self._options = None
        self.discriminator = None

        if options is not None:
            self.options = options

    @property
    def options(self):
        """Gets the options of this AccountPasswordStrengthType.  # noqa: E501

          # noqa: E501

        :return: The options of this AccountPasswordStrengthType.  # noqa: E501
        :rtype: list[AccountPasswordStrengthTypeOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AccountPasswordStrengthType.

          # noqa: E501

        :param options: The options of this AccountPasswordStrengthType.  # noqa: E501
        :type: list[AccountPasswordStrengthTypeOption]
        """

        self._options = options

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
        if issubclass(AccountPasswordStrengthType, dict):
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
        if not isinstance(other, AccountPasswordStrengthType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
