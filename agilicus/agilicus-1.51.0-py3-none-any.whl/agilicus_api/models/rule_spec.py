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


class RuleSpec(object):
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
        'app_id': 'str',
        'comments': 'str',
        'condition': 'HttpRule',
        'org_id': 'str',
        'scope': 'RuleScope'
    }

    attribute_map = {
        'app_id': 'app_id',
        'comments': 'comments',
        'condition': 'condition',
        'org_id': 'org_id',
        'scope': 'scope'
    }

    def __init__(self, app_id=None, comments=None, condition=None, org_id=None, scope=None, local_vars_configuration=None):  # noqa: E501
        """RuleSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._comments = None
        self._condition = None
        self._org_id = None
        self._scope = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if comments is not None:
            self.comments = comments
        if condition is not None:
            self.condition = condition
        if org_id is not None:
            self.org_id = org_id
        if scope is not None:
            self.scope = scope

    @property
    def app_id(self):
        """Gets the app_id of this RuleSpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The app_id of this RuleSpec.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RuleSpec.

        Unique identifier  # noqa: E501

        :param app_id: The app_id of this RuleSpec.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def comments(self):
        """Gets the comments of this RuleSpec.  # noqa: E501

        A description of the rule. The comments have no functional effect, but can help to clarify the purpose of a rule when the name is not sufficient.   # noqa: E501

        :return: The comments of this RuleSpec.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RuleSpec.

        A description of the rule. The comments have no functional effect, but can help to clarify the purpose of a rule when the name is not sufficient.   # noqa: E501

        :param comments: The comments of this RuleSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                comments is not None and len(comments) > 2047):
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `2047`")  # noqa: E501

        self._comments = comments

    @property
    def condition(self):
        """Gets the condition of this RuleSpec.  # noqa: E501


        :return: The condition of this RuleSpec.  # noqa: E501
        :rtype: HttpRule
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this RuleSpec.


        :param condition: The condition of this RuleSpec.  # noqa: E501
        :type: HttpRule
        """

        self._condition = condition

    @property
    def org_id(self):
        """Gets the org_id of this RuleSpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The org_id of this RuleSpec.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this RuleSpec.

        Unique identifier  # noqa: E501

        :param org_id: The org_id of this RuleSpec.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def scope(self):
        """Gets the scope of this RuleSpec.  # noqa: E501


        :return: The scope of this RuleSpec.  # noqa: E501
        :rtype: RuleScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this RuleSpec.


        :param scope: The scope of this RuleSpec.  # noqa: E501
        :type: RuleScope
        """

        self._scope = scope

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
        if not isinstance(other, RuleSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleSpec):
            return True

        return self.to_dict() != other.to_dict()
