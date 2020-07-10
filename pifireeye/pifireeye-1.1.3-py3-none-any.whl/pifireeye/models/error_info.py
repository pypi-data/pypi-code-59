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
from datetime import datetime

class ErrorInfo(object):
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
        'id': 'str',
        'platform_id': 'str',
        'time': 'float',
        'code': 'str',
        'description': 'str',
        'action': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'platform_id': 'platform_id',
        'time': 'time',
        'code': 'code',
        'description': 'description',
        'action': 'action',
        'status': 'status'
    }

    def __init__(self, id=None, platform_id=None, time=None, code=None, description=None, action=None, status=None):  # noqa: E501
        """ErrorInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._platform_id = None
        self._time = datetime.now().timestamp()
        self._code = None
        self._description = None
        self._action = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if platform_id is not None:
            self.platform_id = platform_id
        if time is not None:
            self.time = time
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ErrorInfo.  # noqa: E501


        :return: The id of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErrorInfo.


        :param id: The id of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def platform_id(self):
        """Gets the platform_id of this ErrorInfo.  # noqa: E501


        :return: The platform_id of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this ErrorInfo.


        :param platform_id: The platform_id of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._platform_id = platform_id

    @property
    def time(self):
        """Gets the time of this ErrorInfo.  # noqa: E501

        时间戳，以秒为单位  # noqa: E501

        :return: The time of this ErrorInfo.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ErrorInfo.

        时间戳，以秒为单位  # noqa: E501

        :param time: The time of this ErrorInfo.  # noqa: E501
        :type: float
        """
        if time is not None and time > 10000000000:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `10000000000`")  # noqa: E501
        if time is not None and time < 1000000000:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `1000000000`")  # noqa: E501

        self._time = time

    @property
    def code(self):
        """Gets the code of this ErrorInfo.  # noqa: E501

        故障代码  # noqa: E501

        :return: The code of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorInfo.

        故障代码  # noqa: E501

        :param code: The code of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this ErrorInfo.  # noqa: E501

        故障描述  # noqa: E501

        :return: The description of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ErrorInfo.

        故障描述  # noqa: E501

        :param description: The description of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def action(self):
        """Gets the action of this ErrorInfo.  # noqa: E501

        处理方式  # noqa: E501

        :return: The action of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ErrorInfo.

        处理方式  # noqa: E501

        :param action: The action of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def status(self):
        """Gets the status of this ErrorInfo.  # noqa: E501

        处理状态  # noqa: E501

        :return: The status of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ErrorInfo.

        处理状态  # noqa: E501

        :param status: The status of this ErrorInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["untouched", "processing", "done", "abandoned"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ErrorInfo, dict):
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
        if not isinstance(other, ErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
