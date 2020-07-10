# coding: utf-8

"""
    工业互联网云端API

    工业互联网云端API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Dashboard2dTimeSeriesResponse(object):
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
        'length': 'int',
        'x_axis': 'list[str]',
        'y_axis': 'list[float]'
    }

    attribute_map = {
        'length': 'length',
        'x_axis': 'x_axis',
        'y_axis': 'y_axis'
    }

    def __init__(self, length=None, x_axis=None, y_axis=None):  # noqa: E501
        """Dashboard2dTimeSeriesResponse - a model defined in Swagger"""  # noqa: E501

        self._length = None
        self._x_axis = None
        self._y_axis = None
        self.discriminator = None

        if length is not None:
            self.length = length
        if x_axis is not None:
            self.x_axis = x_axis
        if y_axis is not None:
            self.y_axis = y_axis

    @property
    def length(self):
        """Gets the length of this Dashboard2dTimeSeriesResponse.  # noqa: E501


        :return: The length of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Dashboard2dTimeSeriesResponse.


        :param length: The length of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def x_axis(self):
        """Gets the x_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501

        x轴的数据  # noqa: E501

        :return: The x_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, x_axis):
        """Sets the x_axis of this Dashboard2dTimeSeriesResponse.

        x轴的数据  # noqa: E501

        :param x_axis: The x_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :type: list[str]
        """

        self._x_axis = x_axis

    @property
    def y_axis(self):
        """Gets the y_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501

        y轴的数据  # noqa: E501

        :return: The y_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, y_axis):
        """Sets the y_axis of this Dashboard2dTimeSeriesResponse.

        y轴的数据  # noqa: E501

        :param y_axis: The y_axis of this Dashboard2dTimeSeriesResponse.  # noqa: E501
        :type: list[float]
        """

        self._y_axis = y_axis

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
        if issubclass(Dashboard2dTimeSeriesResponse, dict):
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
        if not isinstance(other, Dashboard2dTimeSeriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
