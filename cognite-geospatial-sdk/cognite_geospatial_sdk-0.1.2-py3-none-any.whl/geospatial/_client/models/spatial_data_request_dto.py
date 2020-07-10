# coding: utf-8

"""
    Cognite API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: playground
    Contact: support@cognite.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cognite.geospatial._client.configuration import Configuration


class SpatialDataRequestDTO(object):
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
        'spatial_id': 'EitherIdDTO',
        'name': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'spatial_id': 'spatialId',
        'name': 'name',
        'limit': 'limit'
    }

    def __init__(self, spatial_id=None, name=None, limit=1, local_vars_configuration=None):  # noqa: E501
        """SpatialDataRequestDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._spatial_id = None
        self._name = None
        self._limit = None
        self.discriminator = None

        if spatial_id is not None:
            self.spatial_id = spatial_id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit

    @property
    def spatial_id(self):
        """Gets the spatial_id of this SpatialDataRequestDTO.  # noqa: E501


        :return: The spatial_id of this SpatialDataRequestDTO.  # noqa: E501
        :rtype: EitherIdDTO
        """
        return self._spatial_id

    @spatial_id.setter
    def spatial_id(self, spatial_id):
        """Sets the spatial_id of this SpatialDataRequestDTO.


        :param spatial_id: The spatial_id of this SpatialDataRequestDTO.  # noqa: E501
        :type: EitherIdDTO
        """

        self._spatial_id = spatial_id

    @property
    def name(self):
        """Gets the name of this SpatialDataRequestDTO.  # noqa: E501


        :return: The name of this SpatialDataRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpatialDataRequestDTO.


        :param name: The name of this SpatialDataRequestDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def limit(self):
        """Gets the limit of this SpatialDataRequestDTO.  # noqa: E501

        Limits the maximum number of latest results to be returned by search.  # noqa: E501

        :return: The limit of this SpatialDataRequestDTO.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SpatialDataRequestDTO.

        Limits the maximum number of latest results to be returned by search.  # noqa: E501

        :param limit: The limit of this SpatialDataRequestDTO.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit > 10):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit < 1):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._limit = limit

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
        if not isinstance(other, SpatialDataRequestDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpatialDataRequestDTO):
            return True

        return self.to_dict() != other.to_dict()
