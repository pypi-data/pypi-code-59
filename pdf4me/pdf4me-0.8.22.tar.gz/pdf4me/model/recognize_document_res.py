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


class RecognizeDocumentRes(object):
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
        'document': 'Document',
        'structured_data_json': 'str',
        'trace_id': 'str',
        'job_id': 'str',
        'subscription_usage': 'SubscriptionUsage'
    }

    attribute_map = {
        'document': 'document',
        'structured_data_json': 'structuredDataJson',
        'trace_id': 'traceId',
        'job_id': 'jobId',
        'subscription_usage': 'subscriptionUsage'
    }

    def __init__(self, document=None, structured_data_json=None, trace_id=None, job_id=None, subscription_usage=None):  # noqa: E501
        """RecognizeDocumentRes - a model defined in Swagger"""  # noqa: E501

        self._document = None
        self._structured_data_json = None
        self._trace_id = None
        self._job_id = None
        self._subscription_usage = None
        self.discriminator = None

        if document is not None:
            self.document = document
        if structured_data_json is not None:
            self.structured_data_json = structured_data_json
        if trace_id is not None:
            self.trace_id = trace_id
        if job_id is not None:
            self.job_id = job_id
        if subscription_usage is not None:
            self.subscription_usage = subscription_usage

    @property
    def document(self):
        """Gets the document of this RecognizeDocumentRes.  # noqa: E501


        :return: The document of this RecognizeDocumentRes.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this RecognizeDocumentRes.


        :param document: The document of this RecognizeDocumentRes.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def structured_data_json(self):
        """Gets the structured_data_json of this RecognizeDocumentRes.  # noqa: E501


        :return: The structured_data_json of this RecognizeDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._structured_data_json

    @structured_data_json.setter
    def structured_data_json(self, structured_data_json):
        """Sets the structured_data_json of this RecognizeDocumentRes.


        :param structured_data_json: The structured_data_json of this RecognizeDocumentRes.  # noqa: E501
        :type: str
        """

        self._structured_data_json = structured_data_json

    @property
    def trace_id(self):
        """Gets the trace_id of this RecognizeDocumentRes.  # noqa: E501


        :return: The trace_id of this RecognizeDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this RecognizeDocumentRes.


        :param trace_id: The trace_id of this RecognizeDocumentRes.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

    @property
    def job_id(self):
        """Gets the job_id of this RecognizeDocumentRes.  # noqa: E501


        :return: The job_id of this RecognizeDocumentRes.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RecognizeDocumentRes.


        :param job_id: The job_id of this RecognizeDocumentRes.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def subscription_usage(self):
        """Gets the subscription_usage of this RecognizeDocumentRes.  # noqa: E501


        :return: The subscription_usage of this RecognizeDocumentRes.  # noqa: E501
        :rtype: SubscriptionUsage
        """
        return self._subscription_usage

    @subscription_usage.setter
    def subscription_usage(self, subscription_usage):
        """Sets the subscription_usage of this RecognizeDocumentRes.


        :param subscription_usage: The subscription_usage of this RecognizeDocumentRes.  # noqa: E501
        :type: SubscriptionUsage
        """

        self._subscription_usage = subscription_usage

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
        if issubclass(RecognizeDocumentRes, dict):
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
        if not isinstance(other, RecognizeDocumentRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
