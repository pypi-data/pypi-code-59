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


class DocTemplate(object):
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
        'name': 'str',
        'language': 'str',
        'sort_order': 'int',
        'process_type': 'str',
        'doc_type': 'str',
        'doc_template_set_id': 'str',
        'doc_render_type': 'str',
        'doc_template_content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'language': 'language',
        'sort_order': 'sortOrder',
        'process_type': 'processType',
        'doc_type': 'docType',
        'doc_template_set_id': 'docTemplateSetId',
        'doc_render_type': 'docRenderType',
        'doc_template_content': 'docTemplateContent'
    }

    def __init__(self, name=None, language=None, sort_order=None, process_type=None, doc_type=None, doc_template_set_id=None, doc_render_type=None, doc_template_content=None):  # noqa: E501
        """DocTemplate - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._language = None
        self._sort_order = None
        self._process_type = None
        self._doc_type = None
        self._doc_template_set_id = None
        self._doc_render_type = None
        self._doc_template_content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if language is not None:
            self.language = language
        if sort_order is not None:
            self.sort_order = sort_order
        if process_type is not None:
            self.process_type = process_type
        if doc_type is not None:
            self.doc_type = doc_type
        if doc_template_set_id is not None:
            self.doc_template_set_id = doc_template_set_id
        if doc_render_type is not None:
            self.doc_render_type = doc_render_type
        if doc_template_content is not None:
            self.doc_template_content = doc_template_content

    @property
    def name(self):
        """Gets the name of this DocTemplate.  # noqa: E501


        :return: The name of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocTemplate.


        :param name: The name of this DocTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def language(self):
        """Gets the language of this DocTemplate.  # noqa: E501


        :return: The language of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DocTemplate.


        :param language: The language of this DocTemplate.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def sort_order(self):
        """Gets the sort_order of this DocTemplate.  # noqa: E501


        :return: The sort_order of this DocTemplate.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DocTemplate.


        :param sort_order: The sort_order of this DocTemplate.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def process_type(self):
        """Gets the process_type of this DocTemplate.  # noqa: E501


        :return: The process_type of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this DocTemplate.


        :param process_type: The process_type of this DocTemplate.  # noqa: E501
        :type: str
        """

        self._process_type = process_type

    @property
    def doc_type(self):
        """Gets the doc_type of this DocTemplate.  # noqa: E501


        :return: The doc_type of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this DocTemplate.


        :param doc_type: The doc_type of this DocTemplate.  # noqa: E501
        :type: str
        """

        self._doc_type = doc_type

    @property
    def doc_template_set_id(self):
        """Gets the doc_template_set_id of this DocTemplate.  # noqa: E501


        :return: The doc_template_set_id of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._doc_template_set_id

    @doc_template_set_id.setter
    def doc_template_set_id(self, doc_template_set_id):
        """Sets the doc_template_set_id of this DocTemplate.


        :param doc_template_set_id: The doc_template_set_id of this DocTemplate.  # noqa: E501
        :type: str
        """

        self._doc_template_set_id = doc_template_set_id

    @property
    def doc_render_type(self):
        """Gets the doc_render_type of this DocTemplate.  # noqa: E501


        :return: The doc_render_type of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._doc_render_type

    @doc_render_type.setter
    def doc_render_type(self, doc_render_type):
        """Sets the doc_render_type of this DocTemplate.


        :param doc_render_type: The doc_render_type of this DocTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["undef", "wordMailMerge", "pdfStatic", "pdfForm", "excel", "report"]  # noqa: E501
        if doc_render_type not in allowed_values:
            raise ValueError(
                "Invalid value for `doc_render_type` ({0}), must be one of {1}"  # noqa: E501
                .format(doc_render_type, allowed_values)
            )

        self._doc_render_type = doc_render_type

    @property
    def doc_template_content(self):
        """Gets the doc_template_content of this DocTemplate.  # noqa: E501


        :return: The doc_template_content of this DocTemplate.  # noqa: E501
        :rtype: str
        """
        return self._doc_template_content

    @doc_template_content.setter
    def doc_template_content(self, doc_template_content):
        """Sets the doc_template_content of this DocTemplate.


        :param doc_template_content: The doc_template_content of this DocTemplate.  # noqa: E501
        :type: str
        """
        if doc_template_content is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', doc_template_content):  # noqa: E501
            raise ValueError(r"Invalid value for `doc_template_content`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._doc_template_content = doc_template_content

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
        if issubclass(DocTemplate, dict):
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
        if not isinstance(other, DocTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
