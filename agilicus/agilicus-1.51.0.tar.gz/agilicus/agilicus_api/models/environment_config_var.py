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


class EnvironmentConfigVar(object):
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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None, local_vars_configuration=None):  # noqa: E501
        """EnvironmentConfigVar - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this EnvironmentConfigVar.  # noqa: E501

        The name of an environment variable. It must be a C_IDENTIFIER. An Identifier can only have alphanumeric characters(a-z , A-Z , 0-9) and underscore( _ ). It is also case-sensitive.   # noqa: E501

        :return: The name of this EnvironmentConfigVar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentConfigVar.

        The name of an environment variable. It must be a C_IDENTIFIER. An Identifier can only have alphanumeric characters(a-z , A-Z , 0-9) and underscore( _ ). It is also case-sensitive.   # noqa: E501

        :param name: The name of this EnvironmentConfigVar.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'[A-Za-z_][A-Za-z0-9_]*', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/[A-Za-z_][A-Za-z0-9_]*/`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this EnvironmentConfigVar.  # noqa: E501

        The value of the environment variable to be passed to the running application's environment.   # noqa: E501

        :return: The value of this EnvironmentConfigVar.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EnvironmentConfigVar.

        The value of the environment variable to be passed to the running application's environment.   # noqa: E501

        :param value: The value of this EnvironmentConfigVar.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) > 32767):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EnvironmentConfigVar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvironmentConfigVar):
            return True

        return self.to_dict() != other.to_dict()
