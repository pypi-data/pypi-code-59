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


class LizardTimeseriesSourcesSinks(object):
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
        'reference_uuid': 'str',
        'start_datetime': 'datetime',
        'interpolate': 'bool',
        'values': 'list[list[float]]',
        'uid': 'str'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'reference_uuid': 'reference_uuid',
        'start_datetime': 'start_datetime',
        'interpolate': 'interpolate',
        'values': 'values',
        'uid': 'uid'
    }

    def __init__(self, url=None, simulation=None, offset=None, duration=None, reference_uuid=None, start_datetime=None, interpolate=None, values=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """LizardTimeseriesSourcesSinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._reference_uuid = None
        self._start_datetime = None
        self._interpolate = None
        self._values = None
        self._uid = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.reference_uuid = reference_uuid
        self.start_datetime = start_datetime
        if interpolate is not None:
            self.interpolate = interpolate
        if values is not None:
            self.values = values
        if uid is not None:
            self.uid = uid

    @property
    def url(self):
        """Gets the url of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The url of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LizardTimeseriesSourcesSinks.


        :param url: The url of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The simulation of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this LizardTimeseriesSourcesSinks.


        :param simulation: The simulation of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this LizardTimeseriesSourcesSinks.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this LizardTimeseriesSourcesSinks.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this LizardTimeseriesSourcesSinks.  # noqa: E501
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
        """Gets the duration of this LizardTimeseriesSourcesSinks.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this LizardTimeseriesSourcesSinks.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this LizardTimeseriesSourcesSinks.  # noqa: E501
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
    def reference_uuid(self):
        """Gets the reference_uuid of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The reference_uuid of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._reference_uuid

    @reference_uuid.setter
    def reference_uuid(self, reference_uuid):
        """Sets the reference_uuid of this LizardTimeseriesSourcesSinks.


        :param reference_uuid: The reference_uuid of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_uuid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reference_uuid is not None and len(reference_uuid) > 40):
            raise ValueError("Invalid value for `reference_uuid`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reference_uuid is not None and len(reference_uuid) < 1):
            raise ValueError("Invalid value for `reference_uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._reference_uuid = reference_uuid

    @property
    def start_datetime(self):
        """Gets the start_datetime of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The start_datetime of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this LizardTimeseriesSourcesSinks.


        :param start_datetime: The start_datetime of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_datetime is None:  # noqa: E501
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def interpolate(self):
        """Gets the interpolate of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The interpolate of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate

    @interpolate.setter
    def interpolate(self, interpolate):
        """Sets the interpolate of this LizardTimeseriesSourcesSinks.


        :param interpolate: The interpolate of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: bool
        """

        self._interpolate = interpolate

    @property
    def values(self):
        """Gets the values of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The values of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this LizardTimeseriesSourcesSinks.


        :param values: The values of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: list[list[float]]
        """

        self._values = values

    @property
    def uid(self):
        """Gets the uid of this LizardTimeseriesSourcesSinks.  # noqa: E501


        :return: The uid of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this LizardTimeseriesSourcesSinks.


        :param uid: The uid of this LizardTimeseriesSourcesSinks.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, LizardTimeseriesSourcesSinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LizardTimeseriesSourcesSinks):
            return True

        return self.to_dict() != other.to_dict()
