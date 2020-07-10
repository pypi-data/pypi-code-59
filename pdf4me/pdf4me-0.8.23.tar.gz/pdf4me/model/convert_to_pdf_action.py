# coding: utf-8

"""
    Pdf4me

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConvertToPdfAction(object):
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
        'pdf_conformance': 'str',
        'conversion_mode': 'str',
        'action_id': 'str'
    }

    attribute_map = {
        'pdf_conformance': 'pdfConformance',
        'conversion_mode': 'conversionMode',
        'action_id': 'actionId'
    }

    def __init__(self, pdf_conformance=None, conversion_mode=None, action_id=None):  # noqa: E501
        """ConvertToPdfAction - a model defined in Swagger"""  # noqa: E501

        self._pdf_conformance = None
        self._conversion_mode = None
        self._action_id = None
        self.discriminator = None

        if pdf_conformance is not None:
            self.pdf_conformance = pdf_conformance
        if conversion_mode is not None:
            self.conversion_mode = conversion_mode
        if action_id is not None:
            self.action_id = action_id

    @property
    def pdf_conformance(self):
        """Gets the pdf_conformance of this ConvertToPdfAction.  # noqa: E501


        :return: The pdf_conformance of this ConvertToPdfAction.  # noqa: E501
        :rtype: str
        """
        return self._pdf_conformance

    @pdf_conformance.setter
    def pdf_conformance(self, pdf_conformance):
        """Sets the pdf_conformance of this ConvertToPdfAction.


        :param pdf_conformance: The pdf_conformance of this ConvertToPdfAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["pdf17", "pdfA1", "pdfA2", "pdfA3"]  # noqa: E501
        if pdf_conformance not in allowed_values:
            raise ValueError(
                "Invalid value for `pdf_conformance` ({0}), must be one of {1}"  # noqa: E501
                .format(pdf_conformance, allowed_values)
            )

        self._pdf_conformance = pdf_conformance

    @property
    def conversion_mode(self):
        """Gets the conversion_mode of this ConvertToPdfAction.  # noqa: E501


        :return: The conversion_mode of this ConvertToPdfAction.  # noqa: E501
        :rtype: str
        """
        return self._conversion_mode

    @conversion_mode.setter
    def conversion_mode(self, conversion_mode):
        """Sets the conversion_mode of this ConvertToPdfAction.


        :param conversion_mode: The conversion_mode of this ConvertToPdfAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["fast", "detailed"]  # noqa: E501
        if conversion_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `conversion_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(conversion_mode, allowed_values)
            )

        self._conversion_mode = conversion_mode

    @property
    def action_id(self):
        """Gets the action_id of this ConvertToPdfAction.  # noqa: E501


        :return: The action_id of this ConvertToPdfAction.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ConvertToPdfAction.


        :param action_id: The action_id of this ConvertToPdfAction.  # noqa: E501
        :type: str
        """

        self._action_id = action_id

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
        if issubclass(ConvertToPdfAction, dict):
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
        if not isinstance(other, ConvertToPdfAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
