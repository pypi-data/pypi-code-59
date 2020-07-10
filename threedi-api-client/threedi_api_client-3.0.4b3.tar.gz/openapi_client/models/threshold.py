# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.11   3Di core release: 2.0.10  deployed on:  11:20AM (UTC) on July 10, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Threshold(object):
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
        'variable': 'str',
        'value': 'float'
    }

    attribute_map = {
        'variable': 'variable',
        'value': 'value'
    }

    def __init__(self, variable=None, value=None, local_vars_configuration=None):  # noqa: E501
        """Threshold - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._variable = None
        self._value = None
        self.discriminator = None

        self.variable = variable
        self.value = value

    @property
    def variable(self):
        """Gets the variable of this Threshold.  # noqa: E501


        :return: The variable of this Threshold.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this Threshold.


        :param variable: The variable of this Threshold.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and variable is None:  # noqa: E501
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501
        allowed_values = ["s1", "u1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and variable not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `variable` ({0}), must be one of {1}"  # noqa: E501
                .format(variable, allowed_values)
            )

        self._variable = variable

    @property
    def value(self):
        """Gets the value of this Threshold.  # noqa: E501


        :return: The value of this Threshold.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Threshold.


        :param value: The value of this Threshold.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, Threshold):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Threshold):
            return True

        return self.to_dict() != other.to_dict()
