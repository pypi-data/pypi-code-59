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

class DeviceStatus(object):
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
        'time': 'float',
        'platform_id': 'str',
        'master_status': 'dict(str, int)',
        'loader_status': 'dict(str, int)',
        'packer_status': 'dict(str, int)',
        'warehouse_status': 'dict(str, int)'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'platform_id': 'platform_id',
        'master_status': 'master_status',
        'loader_status': 'loader_status',
        'packer_status': 'packer_status',
        'warehouse_status': 'warehouse_status'
    }

    def __init__(self, id=None, time=None, platform_id=None, master_status=None, loader_status=None, packer_status=None, warehouse_status=None):  # noqa: E501
        """DeviceStatus - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = datetime.now().timestamp()
        self._platform_id = None
        self._master_status = dict()
        self._loader_status = dict()
        self._packer_status = dict()
        self._warehouse_status = dict()
        self.discriminator = None

        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        if platform_id is not None:
            self.platform_id = platform_id
        if master_status is not None:
            self.master_status = master_status
        if loader_status is not None:
            self.loader_status = loader_status
        if packer_status is not None:
            self.packer_status = packer_status
        if warehouse_status is not None:
            self.warehouse_status = warehouse_status

    @property
    def id(self):
        """Gets the id of this DeviceStatus.  # noqa: E501


        :return: The id of this DeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceStatus.


        :param id: The id of this DeviceStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this DeviceStatus.  # noqa: E501

        时间戳，以秒为单位  # noqa: E501

        :return: The time of this DeviceStatus.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DeviceStatus.

        时间戳，以秒为单位  # noqa: E501

        :param time: The time of this DeviceStatus.  # noqa: E501
        :type: float
        """
        if time is not None and time > 10000000000:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `10000000000`")  # noqa: E501
        if time is not None and time < 1000000000:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `1000000000`")  # noqa: E501

        self._time = time

    @property
    def platform_id(self):
        """Gets the platform_id of this DeviceStatus.  # noqa: E501


        :return: The platform_id of this DeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this DeviceStatus.


        :param platform_id: The platform_id of this DeviceStatus.  # noqa: E501
        :type: str
        """

        self._platform_id = platform_id

    @property
    def master_status(self):
        """Gets the master_status of this DeviceStatus.  # noqa: E501


        :return: The master_status of this DeviceStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._master_status

    @master_status.setter
    def master_status(self, master_status):
        """Sets the master_status of this DeviceStatus.


        :param master_status: The master_status of this DeviceStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._master_status = master_status

    @property
    def loader_status(self):
        """Gets the loader_status of this DeviceStatus.  # noqa: E501


        :return: The loader_status of this DeviceStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._loader_status

    @loader_status.setter
    def loader_status(self, loader_status):
        """Sets the loader_status of this DeviceStatus.


        :param loader_status: The loader_status of this DeviceStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._loader_status = loader_status

    @property
    def packer_status(self):
        """Gets the packer_status of this DeviceStatus.  # noqa: E501


        :return: The packer_status of this DeviceStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._packer_status

    @packer_status.setter
    def packer_status(self, packer_status):
        """Sets the packer_status of this DeviceStatus.


        :param packer_status: The packer_status of this DeviceStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._packer_status = packer_status

    @property
    def warehouse_status(self):
        """Gets the warehouse_status of this DeviceStatus.  # noqa: E501


        :return: The warehouse_status of this DeviceStatus.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._warehouse_status

    @warehouse_status.setter
    def warehouse_status(self, warehouse_status):
        """Sets the warehouse_status of this DeviceStatus.


        :param warehouse_status: The warehouse_status of this DeviceStatus.  # noqa: E501
        :type: dict(str, int)
        """

        self._warehouse_status = warehouse_status

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
        if issubclass(DeviceStatus, dict):
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
        if not isinstance(other, DeviceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
