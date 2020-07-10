# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class Status(object):
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
        'versions': 'list[Version]',
        'online_workers': 'list[Worker]',
        'online_content_apps': 'list[ContentAppStatus]',
        'database_connection': 'DatabaseConnection',
        'redis_connection': 'RedisConnection',
        'storage': 'Storage'
    }

    attribute_map = {
        'versions': 'versions',
        'online_workers': 'online_workers',
        'online_content_apps': 'online_content_apps',
        'database_connection': 'database_connection',
        'redis_connection': 'redis_connection',
        'storage': 'storage'
    }

    def __init__(self, versions=None, online_workers=None, online_content_apps=None, database_connection=None, redis_connection=None, storage=None, local_vars_configuration=None):  # noqa: E501
        """Status - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._versions = None
        self._online_workers = None
        self._online_content_apps = None
        self._database_connection = None
        self._redis_connection = None
        self._storage = None
        self.discriminator = None

        self.versions = versions
        self.online_workers = online_workers
        self.online_content_apps = online_content_apps
        self.database_connection = database_connection
        self.redis_connection = redis_connection
        if storage is not None:
            self.storage = storage

    @property
    def versions(self):
        """Gets the versions of this Status.  # noqa: E501

        Version information of Pulp components  # noqa: E501

        :return: The versions of this Status.  # noqa: E501
        :rtype: list[Version]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Status.

        Version information of Pulp components  # noqa: E501

        :param versions: The versions of this Status.  # noqa: E501
        :type: list[Version]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

    @property
    def online_workers(self):
        """Gets the online_workers of this Status.  # noqa: E501

        List of online workers known to the application. An online worker is actively heartbeating and can respond to new work  # noqa: E501

        :return: The online_workers of this Status.  # noqa: E501
        :rtype: list[Worker]
        """
        return self._online_workers

    @online_workers.setter
    def online_workers(self, online_workers):
        """Sets the online_workers of this Status.

        List of online workers known to the application. An online worker is actively heartbeating and can respond to new work  # noqa: E501

        :param online_workers: The online_workers of this Status.  # noqa: E501
        :type: list[Worker]
        """
        if self.local_vars_configuration.client_side_validation and online_workers is None:  # noqa: E501
            raise ValueError("Invalid value for `online_workers`, must not be `None`")  # noqa: E501

        self._online_workers = online_workers

    @property
    def online_content_apps(self):
        """Gets the online_content_apps of this Status.  # noqa: E501

        List of online content apps known to the application. An online content app is actively heartbeating and can serve data to clients  # noqa: E501

        :return: The online_content_apps of this Status.  # noqa: E501
        :rtype: list[ContentAppStatus]
        """
        return self._online_content_apps

    @online_content_apps.setter
    def online_content_apps(self, online_content_apps):
        """Sets the online_content_apps of this Status.

        List of online content apps known to the application. An online content app is actively heartbeating and can serve data to clients  # noqa: E501

        :param online_content_apps: The online_content_apps of this Status.  # noqa: E501
        :type: list[ContentAppStatus]
        """
        if self.local_vars_configuration.client_side_validation and online_content_apps is None:  # noqa: E501
            raise ValueError("Invalid value for `online_content_apps`, must not be `None`")  # noqa: E501

        self._online_content_apps = online_content_apps

    @property
    def database_connection(self):
        """Gets the database_connection of this Status.  # noqa: E501


        :return: The database_connection of this Status.  # noqa: E501
        :rtype: DatabaseConnection
        """
        return self._database_connection

    @database_connection.setter
    def database_connection(self, database_connection):
        """Sets the database_connection of this Status.


        :param database_connection: The database_connection of this Status.  # noqa: E501
        :type: DatabaseConnection
        """
        if self.local_vars_configuration.client_side_validation and database_connection is None:  # noqa: E501
            raise ValueError("Invalid value for `database_connection`, must not be `None`")  # noqa: E501

        self._database_connection = database_connection

    @property
    def redis_connection(self):
        """Gets the redis_connection of this Status.  # noqa: E501


        :return: The redis_connection of this Status.  # noqa: E501
        :rtype: RedisConnection
        """
        return self._redis_connection

    @redis_connection.setter
    def redis_connection(self, redis_connection):
        """Sets the redis_connection of this Status.


        :param redis_connection: The redis_connection of this Status.  # noqa: E501
        :type: RedisConnection
        """
        if self.local_vars_configuration.client_side_validation and redis_connection is None:  # noqa: E501
            raise ValueError("Invalid value for `redis_connection`, must not be `None`")  # noqa: E501

        self._redis_connection = redis_connection

    @property
    def storage(self):
        """Gets the storage of this Status.  # noqa: E501


        :return: The storage of this Status.  # noqa: E501
        :rtype: Storage
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this Status.


        :param storage: The storage of this Status.  # noqa: E501
        :type: Storage
        """

        self._storage = storage

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
        if not isinstance(other, Status):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Status):
            return True

        return self.to_dict() != other.to_dict()
