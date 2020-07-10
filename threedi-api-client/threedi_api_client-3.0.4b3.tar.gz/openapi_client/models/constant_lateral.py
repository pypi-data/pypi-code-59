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


class ConstantLateral(object):
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
        'url': 'str',
        'simulation': 'str',
        'offset': 'int',
        'duration': 'int',
        'value': 'float',
        'units': 'str',
        'point': 'str',
        'connection_node': 'int',
        'state': 'str',
        'state_detail': 'object',
        'grid_id': 'int',
        'uid': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'value': 'value',
        'units': 'units',
        'point': 'point',
        'connection_node': 'connection_node',
        'state': 'state',
        'state_detail': 'state_detail',
        'grid_id': 'grid_id',
        'uid': 'uid',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, offset=None, duration=None, value=None, units=None, point=None, connection_node=None, state=None, state_detail=None, grid_id=None, uid=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ConstantLateral - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._value = None
        self._units = None
        self._point = None
        self._connection_node = None
        self._state = None
        self._state_detail = None
        self._grid_id = None
        self._uid = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.value = value
        self.units = units
        self.point = point
        self.connection_node = connection_node
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail
        if grid_id is not None:
            self.grid_id = grid_id
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this ConstantLateral.  # noqa: E501


        :return: The url of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConstantLateral.


        :param url: The url of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this ConstantLateral.  # noqa: E501


        :return: The simulation of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ConstantLateral.


        :param simulation: The simulation of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this ConstantLateral.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ConstantLateral.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this ConstantLateral.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ConstantLateral.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._duration = duration

    @property
    def value(self):
        """Gets the value of this ConstantLateral.  # noqa: E501


        :return: The value of this ConstantLateral.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConstantLateral.


        :param value: The value of this ConstantLateral.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def units(self):
        """Gets the units of this ConstantLateral.  # noqa: E501

        'm3/s' (only option for now)  # noqa: E501

        :return: The units of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ConstantLateral.

        'm3/s' (only option for now)  # noqa: E501

        :param units: The units of this ConstantLateral.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["m3/s"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and units not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def point(self):
        """Gets the point of this ConstantLateral.  # noqa: E501


        :return: The point of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this ConstantLateral.


        :param point: The point of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._point = point

    @property
    def connection_node(self):
        """Gets the connection_node of this ConstantLateral.  # noqa: E501


        :return: The connection_node of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._connection_node

    @connection_node.setter
    def connection_node(self, connection_node):
        """Sets the connection_node of this ConstantLateral.


        :param connection_node: The connection_node of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                connection_node is not None and connection_node > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `connection_node`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_node is not None and connection_node < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `connection_node`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._connection_node = connection_node

    @property
    def state(self):
        """Gets the state of this ConstantLateral.  # noqa: E501


        :return: The state of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ConstantLateral.


        :param state: The state of this ConstantLateral.  # noqa: E501
        :type: str
        """
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this ConstantLateral.  # noqa: E501


        :return: The state_detail of this ConstantLateral.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this ConstantLateral.


        :param state_detail: The state_detail of this ConstantLateral.  # noqa: E501
        :type: object
        """

        self._state_detail = state_detail

    @property
    def grid_id(self):
        """Gets the grid_id of this ConstantLateral.  # noqa: E501


        :return: The grid_id of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._grid_id

    @grid_id.setter
    def grid_id(self, grid_id):
        """Sets the grid_id of this ConstantLateral.


        :param grid_id: The grid_id of this ConstantLateral.  # noqa: E501
        :type: int
        """

        self._grid_id = grid_id

    @property
    def uid(self):
        """Gets the uid of this ConstantLateral.  # noqa: E501


        :return: The uid of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ConstantLateral.


        :param uid: The uid of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this ConstantLateral.  # noqa: E501


        :return: The id of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstantLateral.


        :param id: The id of this ConstantLateral.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, ConstantLateral):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstantLateral):
            return True

        return self.to_dict() != other.to_dict()
