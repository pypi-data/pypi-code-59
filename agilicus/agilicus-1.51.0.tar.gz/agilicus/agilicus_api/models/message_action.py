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


class MessageAction(object):
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
        'title': 'str',
        'uri': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'title': 'title',
        'uri': 'uri',
        'icon': 'icon'
    }

    def __init__(self, title=None, uri=None, icon=None, local_vars_configuration=None):  # noqa: E501
        """MessageAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._uri = None
        self._icon = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if uri is not None:
            self.uri = uri
        if icon is not None:
            self.icon = icon

    @property
    def title(self):
        """Gets the title of this MessageAction.  # noqa: E501

        The text the user is shown  # noqa: E501

        :return: The title of this MessageAction.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MessageAction.

        The text the user is shown  # noqa: E501

        :param title: The title of this MessageAction.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def uri(self):
        """Gets the uri of this MessageAction.  # noqa: E501

        the URI to invoke (with context) when selected  # noqa: E501

        :return: The uri of this MessageAction.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this MessageAction.

        the URI to invoke (with context) when selected  # noqa: E501

        :param uri: The uri of this MessageAction.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def icon(self):
        """Gets the icon of this MessageAction.  # noqa: E501

        the URI to an icon-button (if supported)  # noqa: E501

        :return: The icon of this MessageAction.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this MessageAction.

        the URI to an icon-button (if supported)  # noqa: E501

        :param icon: The icon of this MessageAction.  # noqa: E501
        :type: str
        """

        self._icon = icon

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
        if not isinstance(other, MessageAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageAction):
            return True

        return self.to_dict() != other.to_dict()
