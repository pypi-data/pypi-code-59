# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Contact(object):
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
        'contact_id': 'str',
        'contact_phone_numbers': 'list[ContactPhoneNumber]',
        'contact_uri': 'str',
        'emails': 'list[str]',
        'error_details': 'ErrorDetails',
        'name': 'str',
        'organization': 'str',
        'shared': 'str',
        'signing_group': 'str',
        'signing_group_name': 'str'
    }

    attribute_map = {
        'contact_id': 'contactId',
        'contact_phone_numbers': 'contactPhoneNumbers',
        'contact_uri': 'contactUri',
        'emails': 'emails',
        'error_details': 'errorDetails',
        'name': 'name',
        'organization': 'organization',
        'shared': 'shared',
        'signing_group': 'signingGroup',
        'signing_group_name': 'signingGroupName'
    }

    def __init__(self, contact_id=None, contact_phone_numbers=None, contact_uri=None, emails=None, error_details=None, name=None, organization=None, shared=None, signing_group=None, signing_group_name=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._contact_id = None
        self._contact_phone_numbers = None
        self._contact_uri = None
        self._emails = None
        self._error_details = None
        self._name = None
        self._organization = None
        self._shared = None
        self._signing_group = None
        self._signing_group_name = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if contact_phone_numbers is not None:
            self.contact_phone_numbers = contact_phone_numbers
        if contact_uri is not None:
            self.contact_uri = contact_uri
        if emails is not None:
            self.emails = emails
        if error_details is not None:
            self.error_details = error_details
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if shared is not None:
            self.shared = shared
        if signing_group is not None:
            self.signing_group = signing_group
        if signing_group_name is not None:
            self.signing_group_name = signing_group_name

    @property
    def contact_id(self):
        """Gets the contact_id of this Contact.  # noqa: E501

          # noqa: E501

        :return: The contact_id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Contact.

          # noqa: E501

        :param contact_id: The contact_id of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def contact_phone_numbers(self):
        """Gets the contact_phone_numbers of this Contact.  # noqa: E501

          # noqa: E501

        :return: The contact_phone_numbers of this Contact.  # noqa: E501
        :rtype: list[ContactPhoneNumber]
        """
        return self._contact_phone_numbers

    @contact_phone_numbers.setter
    def contact_phone_numbers(self, contact_phone_numbers):
        """Sets the contact_phone_numbers of this Contact.

          # noqa: E501

        :param contact_phone_numbers: The contact_phone_numbers of this Contact.  # noqa: E501
        :type: list[ContactPhoneNumber]
        """

        self._contact_phone_numbers = contact_phone_numbers

    @property
    def contact_uri(self):
        """Gets the contact_uri of this Contact.  # noqa: E501

          # noqa: E501

        :return: The contact_uri of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_uri

    @contact_uri.setter
    def contact_uri(self, contact_uri):
        """Sets the contact_uri of this Contact.

          # noqa: E501

        :param contact_uri: The contact_uri of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_uri = contact_uri

    @property
    def emails(self):
        """Gets the emails of this Contact.  # noqa: E501

          # noqa: E501

        :return: The emails of this Contact.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Contact.

          # noqa: E501

        :param emails: The emails of this Contact.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def error_details(self):
        """Gets the error_details of this Contact.  # noqa: E501


        :return: The error_details of this Contact.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Contact.


        :param error_details: The error_details of this Contact.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def name(self):
        """Gets the name of this Contact.  # noqa: E501

          # noqa: E501

        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contact.

          # noqa: E501

        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Contact.  # noqa: E501

          # noqa: E501

        :return: The organization of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Contact.

          # noqa: E501

        :param organization: The organization of this Contact.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def shared(self):
        """Gets the shared of this Contact.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Contact.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this Contact.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def signing_group(self):
        """Gets the signing_group of this Contact.  # noqa: E501

          # noqa: E501

        :return: The signing_group of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._signing_group

    @signing_group.setter
    def signing_group(self, signing_group):
        """Sets the signing_group of this Contact.

          # noqa: E501

        :param signing_group: The signing_group of this Contact.  # noqa: E501
        :type: str
        """

        self._signing_group = signing_group

    @property
    def signing_group_name(self):
        """Gets the signing_group_name of this Contact.  # noqa: E501

        The display name for the signing group.   Maximum Length: 100 characters.   # noqa: E501

        :return: The signing_group_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._signing_group_name

    @signing_group_name.setter
    def signing_group_name(self, signing_group_name):
        """Sets the signing_group_name of this Contact.

        The display name for the signing group.   Maximum Length: 100 characters.   # noqa: E501

        :param signing_group_name: The signing_group_name of this Contact.  # noqa: E501
        :type: str
        """

        self._signing_group_name = signing_group_name

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
