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


class SmartSectionAnchorPosition(object):
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
        'page_number': 'int',
        'x_position': 'float',
        'y_position': 'float'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'x_position': 'xPosition',
        'y_position': 'yPosition'
    }

    def __init__(self, page_number=None, x_position=None, y_position=None):  # noqa: E501
        """SmartSectionAnchorPosition - a model defined in Swagger"""  # noqa: E501

        self._page_number = None
        self._x_position = None
        self._y_position = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if x_position is not None:
            self.x_position = x_position
        if y_position is not None:
            self.y_position = y_position

    @property
    def page_number(self):
        """Gets the page_number of this SmartSectionAnchorPosition.  # noqa: E501

        Specifies the page number on which the tab is located.  # noqa: E501

        :return: The page_number of this SmartSectionAnchorPosition.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this SmartSectionAnchorPosition.

        Specifies the page number on which the tab is located.  # noqa: E501

        :param page_number: The page_number of this SmartSectionAnchorPosition.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def x_position(self):
        """Gets the x_position of this SmartSectionAnchorPosition.  # noqa: E501

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The x_position of this SmartSectionAnchorPosition.  # noqa: E501
        :rtype: float
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """Sets the x_position of this SmartSectionAnchorPosition.

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param x_position: The x_position of this SmartSectionAnchorPosition.  # noqa: E501
        :type: float
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """Gets the y_position of this SmartSectionAnchorPosition.  # noqa: E501

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The y_position of this SmartSectionAnchorPosition.  # noqa: E501
        :rtype: float
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """Sets the y_position of this SmartSectionAnchorPosition.

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param y_position: The y_position of this SmartSectionAnchorPosition.  # noqa: E501
        :type: float
        """

        self._y_position = y_position

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
        if issubclass(SmartSectionAnchorPosition, dict):
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
        if not isinstance(other, SmartSectionAnchorPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
