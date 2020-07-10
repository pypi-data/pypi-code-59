# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.07.09
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class ListIssuerExtensionsResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'issuer_extensions': 'list[Issuer]',
        'limit': 'int'
    }

    attribute_map = {
        'issuer_extensions': 'issuer_extensions',
        'limit': 'limit'
    }

    def __init__(self, issuer_extensions=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ListIssuerExtensionsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._issuer_extensions = None
        self._limit = None
        self.discriminator = None

        if issuer_extensions is not None:
            self.issuer_extensions = issuer_extensions
        self.limit = limit

    @property
    def issuer_extensions(self):
        """Gets the issuer_extensions of this ListIssuerExtensionsResponse.  # noqa: E501

        List of Issuers  # noqa: E501

        :return: The issuer_extensions of this ListIssuerExtensionsResponse.  # noqa: E501
        :rtype: list[Issuer]
        """
        return self._issuer_extensions

    @issuer_extensions.setter
    def issuer_extensions(self, issuer_extensions):
        """Sets the issuer_extensions of this ListIssuerExtensionsResponse.

        List of Issuers  # noqa: E501

        :param issuer_extensions: The issuer_extensions of this ListIssuerExtensionsResponse.  # noqa: E501
        :type: list[Issuer]
        """

        self._issuer_extensions = issuer_extensions

    @property
    def limit(self):
        """Gets the limit of this ListIssuerExtensionsResponse.  # noqa: E501

        Limit of issuers in the response  # noqa: E501

        :return: The limit of this ListIssuerExtensionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssuerExtensionsResponse.

        Limit of issuers in the response  # noqa: E501

        :param limit: The limit of this ListIssuerExtensionsResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListIssuerExtensionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListIssuerExtensionsResponse):
            return True

        return self.to_dict() != other.to_dict()
