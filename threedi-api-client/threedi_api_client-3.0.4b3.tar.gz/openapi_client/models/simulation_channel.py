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


class SimulationChannel(object):
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
        'id': 'int',
        'simulation': 'str',
        'channel_name': 'str',
        'created': 'datetime',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'simulation': 'simulation',
        'channel_name': 'channel_name',
        'created': 'created',
        'state': 'state'
    }

    def __init__(self, id=None, simulation=None, channel_name=None, created=None, state=None, local_vars_configuration=None):  # noqa: E501
        """SimulationChannel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._simulation = None
        self._channel_name = None
        self._created = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if simulation is not None:
            self.simulation = simulation
        if channel_name is not None:
            self.channel_name = channel_name
        if created is not None:
            self.created = created
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this SimulationChannel.  # noqa: E501


        :return: The id of this SimulationChannel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulationChannel.


        :param id: The id of this SimulationChannel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def simulation(self):
        """Gets the simulation of this SimulationChannel.  # noqa: E501


        :return: The simulation of this SimulationChannel.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this SimulationChannel.


        :param simulation: The simulation of this SimulationChannel.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def channel_name(self):
        """Gets the channel_name of this SimulationChannel.  # noqa: E501


        :return: The channel_name of this SimulationChannel.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this SimulationChannel.


        :param channel_name: The channel_name of this SimulationChannel.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                channel_name is not None and len(channel_name) < 1):
            raise ValueError("Invalid value for `channel_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._channel_name = channel_name

    @property
    def created(self):
        """Gets the created of this SimulationChannel.  # noqa: E501


        :return: The created of this SimulationChannel.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SimulationChannel.


        :param created: The created of this SimulationChannel.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def state(self):
        """Gets the state of this SimulationChannel.  # noqa: E501


        :return: The state of this SimulationChannel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SimulationChannel.


        :param state: The state of this SimulationChannel.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "confirmed", "timeout"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, SimulationChannel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationChannel):
            return True

        return self.to_dict() != other.to_dict()
