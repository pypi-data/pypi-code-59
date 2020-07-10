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


class FormDataItem(object):
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
        'error_details': 'ErrorDetails',
        'list_selected_value': 'str',
        'name': 'str',
        'original_value': 'str',
        'value': 'str'
    }

    attribute_map = {
        'error_details': 'errorDetails',
        'list_selected_value': 'listSelectedValue',
        'name': 'name',
        'original_value': 'originalValue',
        'value': 'value'
    }

    def __init__(self, error_details=None, list_selected_value=None, name=None, original_value=None, value=None):  # noqa: E501
        """FormDataItem - a model defined in Swagger"""  # noqa: E501

        self._error_details = None
        self._list_selected_value = None
        self._name = None
        self._original_value = None
        self._value = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details
        if list_selected_value is not None:
            self.list_selected_value = list_selected_value
        if name is not None:
            self.name = name
        if original_value is not None:
            self.original_value = original_value
        if value is not None:
            self.value = value

    @property
    def error_details(self):
        """Gets the error_details of this FormDataItem.  # noqa: E501


        :return: The error_details of this FormDataItem.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this FormDataItem.


        :param error_details: The error_details of this FormDataItem.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def list_selected_value(self):
        """Gets the list_selected_value of this FormDataItem.  # noqa: E501

          # noqa: E501

        :return: The list_selected_value of this FormDataItem.  # noqa: E501
        :rtype: str
        """
        return self._list_selected_value

    @list_selected_value.setter
    def list_selected_value(self, list_selected_value):
        """Sets the list_selected_value of this FormDataItem.

          # noqa: E501

        :param list_selected_value: The list_selected_value of this FormDataItem.  # noqa: E501
        :type: str
        """

        self._list_selected_value = list_selected_value

    @property
    def name(self):
        """Gets the name of this FormDataItem.  # noqa: E501

          # noqa: E501

        :return: The name of this FormDataItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormDataItem.

          # noqa: E501

        :param name: The name of this FormDataItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_value(self):
        """Gets the original_value of this FormDataItem.  # noqa: E501

        The initial value of the tab when it was sent to the recipient.   # noqa: E501

        :return: The original_value of this FormDataItem.  # noqa: E501
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this FormDataItem.

        The initial value of the tab when it was sent to the recipient.   # noqa: E501

        :param original_value: The original_value of this FormDataItem.  # noqa: E501
        :type: str
        """

        self._original_value = original_value

    @property
    def value(self):
        """Gets the value of this FormDataItem.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this FormDataItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FormDataItem.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this FormDataItem.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(FormDataItem, dict):
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
        if not isinstance(other, FormDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
