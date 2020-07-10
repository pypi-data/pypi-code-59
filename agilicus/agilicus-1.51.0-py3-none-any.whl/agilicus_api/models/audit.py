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


class Audit(object):
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
        'user_id': 'str',
        'target_resource_type': 'str',
        'api_name': 'str',
        'org_id': 'str',
        'time': 'datetime',
        'action': 'str',
        'source_ip': 'str',
        'target_id': 'str',
        'token_id': 'str',
        'trace_id': 'str',
        'session': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'target_resource_type': 'target_resource_type',
        'api_name': 'api_name',
        'org_id': 'org_id',
        'time': 'time',
        'action': 'action',
        'source_ip': 'source_ip',
        'target_id': 'target_id',
        'token_id': 'token_id',
        'trace_id': 'trace_id',
        'session': 'session'
    }

    def __init__(self, user_id=None, target_resource_type=None, api_name=None, org_id=None, time=None, action=None, source_ip=None, target_id=None, token_id=None, trace_id=None, session=None, local_vars_configuration=None):  # noqa: E501
        """Audit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._target_resource_type = None
        self._api_name = None
        self._org_id = None
        self._time = None
        self._action = None
        self._source_ip = None
        self._target_id = None
        self._token_id = None
        self._trace_id = None
        self._session = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if target_resource_type is not None:
            self.target_resource_type = target_resource_type
        if api_name is not None:
            self.api_name = api_name
        if org_id is not None:
            self.org_id = org_id
        if time is not None:
            self.time = time
        if action is not None:
            self.action = action
        if source_ip is not None:
            self.source_ip = source_ip
        if target_id is not None:
            self.target_id = target_id
        if token_id is not None:
            self.token_id = token_id
        if trace_id is not None:
            self.trace_id = trace_id
        if session is not None:
            self.session = session

    @property
    def user_id(self):
        """Gets the user_id of this Audit.  # noqa: E501

        The id of the user performing the action  # noqa: E501

        :return: The user_id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Audit.

        The id of the user performing the action  # noqa: E501

        :param user_id: The user_id of this Audit.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def target_resource_type(self):
        """Gets the target_resource_type of this Audit.  # noqa: E501

        The name of the resource type which was affected by the event which generated this record. The `target_id` field will uniquely identify, if possible, the record within the resource type.   # noqa: E501

        :return: The target_resource_type of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        """Sets the target_resource_type of this Audit.

        The name of the resource type which was affected by the event which generated this record. The `target_id` field will uniquely identify, if possible, the record within the resource type.   # noqa: E501

        :param target_resource_type: The target_resource_type of this Audit.  # noqa: E501
        :type: str
        """

        self._target_resource_type = target_resource_type

    @property
    def api_name(self):
        """Gets the api_name of this Audit.  # noqa: E501

        The name of the API which generated the event. This will typically be a single value for many different target_resource_types.   # noqa: E501

        :return: The api_name of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this Audit.

        The name of the API which generated the event. This will typically be a single value for many different target_resource_types.   # noqa: E501

        :param api_name: The api_name of this Audit.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def org_id(self):
        """Gets the org_id of this Audit.  # noqa: E501

        The organization of the user performing the action  # noqa: E501

        :return: The org_id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Audit.

        The organization of the user performing the action  # noqa: E501

        :param org_id: The org_id of this Audit.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def time(self):
        """Gets the time of this Audit.  # noqa: E501

        the time at which the log was generated  # noqa: E501

        :return: The time of this Audit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Audit.

        the time at which the log was generated  # noqa: E501

        :param time: The time of this Audit.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def action(self):
        """Gets the action of this Audit.  # noqa: E501

        The type of action performed on the target  # noqa: E501

        :return: The action of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Audit.

        The type of action performed on the target  # noqa: E501

        :param action: The action of this Audit.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def source_ip(self):
        """Gets the source_ip of this Audit.  # noqa: E501

        The IP address of the host initating the action  # noqa: E501

        :return: The source_ip of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this Audit.

        The IP address of the host initating the action  # noqa: E501

        :param source_ip: The source_ip of this Audit.  # noqa: E501
        :type: str
        """

        self._source_ip = source_ip

    @property
    def target_id(self):
        """Gets the target_id of this Audit.  # noqa: E501

        The id of the resource affected by the action  # noqa: E501

        :return: The target_id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Audit.

        The id of the resource affected by the action  # noqa: E501

        :param target_id: The target_id of this Audit.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def token_id(self):
        """Gets the token_id of this Audit.  # noqa: E501

        The id of the bearer token used to authenticate when performing the action  # noqa: E501

        :return: The token_id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this Audit.

        The id of the bearer token used to authenticate when performing the action  # noqa: E501

        :param token_id: The token_id of this Audit.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def trace_id(self):
        """Gets the trace_id of this Audit.  # noqa: E501

        A correlation ID associated with requests related to this action  # noqa: E501

        :return: The trace_id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this Audit.

        A correlation ID associated with requests related to this action  # noqa: E501

        :param trace_id: The trace_id of this Audit.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

    @property
    def session(self):
        """Gets the session of this Audit.  # noqa: E501

        The session associated with this action. Sessions typically span multiple tokens.   # noqa: E501

        :return: The session of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Audit.

        The session associated with this action. Sessions typically span multiple tokens.   # noqa: E501

        :param session: The session of this Audit.  # noqa: E501
        :type: str
        """

        self._session = session

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
        if not isinstance(other, Audit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Audit):
            return True

        return self.to_dict() != other.to_dict()
