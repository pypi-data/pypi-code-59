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


class UserSignature(object):
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
        'adopted_date_time': 'str',
        'created_date_time': 'str',
        'date_stamp_properties': 'DateStampProperties',
        'error_details': 'ErrorDetails',
        'external_id': 'str',
        'image_type': 'str',
        'initials150_image_id': 'str',
        'initials_image_uri': 'str',
        'is_default': 'str',
        'phonetic_name': 'str',
        'signature150_image_id': 'str',
        'signature_font': 'str',
        'signature_id': 'str',
        'signature_image_uri': 'str',
        'signature_initials': 'str',
        'signature_name': 'str',
        'signature_type': 'str',
        'stamp_format': 'str',
        'stamp_image_uri': 'str',
        'stamp_size_mm': 'str',
        'stamp_type': 'str'
    }

    attribute_map = {
        'adopted_date_time': 'adoptedDateTime',
        'created_date_time': 'createdDateTime',
        'date_stamp_properties': 'dateStampProperties',
        'error_details': 'errorDetails',
        'external_id': 'externalID',
        'image_type': 'imageType',
        'initials150_image_id': 'initials150ImageId',
        'initials_image_uri': 'initialsImageUri',
        'is_default': 'isDefault',
        'phonetic_name': 'phoneticName',
        'signature150_image_id': 'signature150ImageId',
        'signature_font': 'signatureFont',
        'signature_id': 'signatureId',
        'signature_image_uri': 'signatureImageUri',
        'signature_initials': 'signatureInitials',
        'signature_name': 'signatureName',
        'signature_type': 'signatureType',
        'stamp_format': 'stampFormat',
        'stamp_image_uri': 'stampImageUri',
        'stamp_size_mm': 'stampSizeMM',
        'stamp_type': 'stampType'
    }

    def __init__(self, adopted_date_time=None, created_date_time=None, date_stamp_properties=None, error_details=None, external_id=None, image_type=None, initials150_image_id=None, initials_image_uri=None, is_default=None, phonetic_name=None, signature150_image_id=None, signature_font=None, signature_id=None, signature_image_uri=None, signature_initials=None, signature_name=None, signature_type=None, stamp_format=None, stamp_image_uri=None, stamp_size_mm=None, stamp_type=None):  # noqa: E501
        """UserSignature - a model defined in Swagger"""  # noqa: E501

        self._adopted_date_time = None
        self._created_date_time = None
        self._date_stamp_properties = None
        self._error_details = None
        self._external_id = None
        self._image_type = None
        self._initials150_image_id = None
        self._initials_image_uri = None
        self._is_default = None
        self._phonetic_name = None
        self._signature150_image_id = None
        self._signature_font = None
        self._signature_id = None
        self._signature_image_uri = None
        self._signature_initials = None
        self._signature_name = None
        self._signature_type = None
        self._stamp_format = None
        self._stamp_image_uri = None
        self._stamp_size_mm = None
        self._stamp_type = None
        self.discriminator = None

        if adopted_date_time is not None:
            self.adopted_date_time = adopted_date_time
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if date_stamp_properties is not None:
            self.date_stamp_properties = date_stamp_properties
        if error_details is not None:
            self.error_details = error_details
        if external_id is not None:
            self.external_id = external_id
        if image_type is not None:
            self.image_type = image_type
        if initials150_image_id is not None:
            self.initials150_image_id = initials150_image_id
        if initials_image_uri is not None:
            self.initials_image_uri = initials_image_uri
        if is_default is not None:
            self.is_default = is_default
        if phonetic_name is not None:
            self.phonetic_name = phonetic_name
        if signature150_image_id is not None:
            self.signature150_image_id = signature150_image_id
        if signature_font is not None:
            self.signature_font = signature_font
        if signature_id is not None:
            self.signature_id = signature_id
        if signature_image_uri is not None:
            self.signature_image_uri = signature_image_uri
        if signature_initials is not None:
            self.signature_initials = signature_initials
        if signature_name is not None:
            self.signature_name = signature_name
        if signature_type is not None:
            self.signature_type = signature_type
        if stamp_format is not None:
            self.stamp_format = stamp_format
        if stamp_image_uri is not None:
            self.stamp_image_uri = stamp_image_uri
        if stamp_size_mm is not None:
            self.stamp_size_mm = stamp_size_mm
        if stamp_type is not None:
            self.stamp_type = stamp_type

    @property
    def adopted_date_time(self):
        """Gets the adopted_date_time of this UserSignature.  # noqa: E501

        The date and time the user adopted their signature.  # noqa: E501

        :return: The adopted_date_time of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._adopted_date_time

    @adopted_date_time.setter
    def adopted_date_time(self, adopted_date_time):
        """Sets the adopted_date_time of this UserSignature.

        The date and time the user adopted their signature.  # noqa: E501

        :param adopted_date_time: The adopted_date_time of this UserSignature.  # noqa: E501
        :type: str
        """

        self._adopted_date_time = adopted_date_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this UserSignature.  # noqa: E501

        Indicates the date and time the item was created.  # noqa: E501

        :return: The created_date_time of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this UserSignature.

        Indicates the date and time the item was created.  # noqa: E501

        :param created_date_time: The created_date_time of this UserSignature.  # noqa: E501
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def date_stamp_properties(self):
        """Gets the date_stamp_properties of this UserSignature.  # noqa: E501


        :return: The date_stamp_properties of this UserSignature.  # noqa: E501
        :rtype: DateStampProperties
        """
        return self._date_stamp_properties

    @date_stamp_properties.setter
    def date_stamp_properties(self, date_stamp_properties):
        """Sets the date_stamp_properties of this UserSignature.


        :param date_stamp_properties: The date_stamp_properties of this UserSignature.  # noqa: E501
        :type: DateStampProperties
        """

        self._date_stamp_properties = date_stamp_properties

    @property
    def error_details(self):
        """Gets the error_details of this UserSignature.  # noqa: E501


        :return: The error_details of this UserSignature.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this UserSignature.


        :param error_details: The error_details of this UserSignature.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def external_id(self):
        """Gets the external_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The external_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserSignature.

          # noqa: E501

        :param external_id: The external_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def image_type(self):
        """Gets the image_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The image_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this UserSignature.

          # noqa: E501

        :param image_type: The image_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._image_type = image_type

    @property
    def initials150_image_id(self):
        """Gets the initials150_image_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The initials150_image_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._initials150_image_id

    @initials150_image_id.setter
    def initials150_image_id(self, initials150_image_id):
        """Sets the initials150_image_id of this UserSignature.

          # noqa: E501

        :param initials150_image_id: The initials150_image_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._initials150_image_id = initials150_image_id

    @property
    def initials_image_uri(self):
        """Gets the initials_image_uri of this UserSignature.  # noqa: E501

        Contains the URI for an endpoint that you can use to retrieve the initials image.  # noqa: E501

        :return: The initials_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._initials_image_uri

    @initials_image_uri.setter
    def initials_image_uri(self, initials_image_uri):
        """Sets the initials_image_uri of this UserSignature.

        Contains the URI for an endpoint that you can use to retrieve the initials image.  # noqa: E501

        :param initials_image_uri: The initials_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._initials_image_uri = initials_image_uri

    @property
    def is_default(self):
        """Gets the is_default of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The is_default of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this UserSignature.

          # noqa: E501

        :param is_default: The is_default of this UserSignature.  # noqa: E501
        :type: str
        """

        self._is_default = is_default

    @property
    def phonetic_name(self):
        """Gets the phonetic_name of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The phonetic_name of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._phonetic_name

    @phonetic_name.setter
    def phonetic_name(self, phonetic_name):
        """Sets the phonetic_name of this UserSignature.

          # noqa: E501

        :param phonetic_name: The phonetic_name of this UserSignature.  # noqa: E501
        :type: str
        """

        self._phonetic_name = phonetic_name

    @property
    def signature150_image_id(self):
        """Gets the signature150_image_id of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The signature150_image_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature150_image_id

    @signature150_image_id.setter
    def signature150_image_id(self, signature150_image_id):
        """Sets the signature150_image_id of this UserSignature.

          # noqa: E501

        :param signature150_image_id: The signature150_image_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature150_image_id = signature150_image_id

    @property
    def signature_font(self):
        """Gets the signature_font of this UserSignature.  # noqa: E501

        The font type for the signature, if the signature is not drawn. The supported font types are:  \"7_DocuSign\", \"1_DocuSign\", \"6_DocuSign\", \"8_DocuSign\", \"3_DocuSign\", \"Mistral\", \"4_DocuSign\", \"2_DocuSign\", \"5_DocuSign\", \"Rage Italic\"   # noqa: E501

        :return: The signature_font of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_font

    @signature_font.setter
    def signature_font(self, signature_font):
        """Sets the signature_font of this UserSignature.

        The font type for the signature, if the signature is not drawn. The supported font types are:  \"7_DocuSign\", \"1_DocuSign\", \"6_DocuSign\", \"8_DocuSign\", \"3_DocuSign\", \"Mistral\", \"4_DocuSign\", \"2_DocuSign\", \"5_DocuSign\", \"Rage Italic\"   # noqa: E501

        :param signature_font: The signature_font of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_font = signature_font

    @property
    def signature_id(self):
        """Gets the signature_id of this UserSignature.  # noqa: E501

        Specifies the signature ID associated with the signature name. You can use the signature ID in the URI in place of the signature name, and the value stored in the `signatureName` property in the body is used. This allows the use of special characters (such as \"&\", \"<\", \">\") in a the signature name. Note that with each update to signatures, the returned signature ID might change, so the caller will need to trigger off the signature name to get the new signature ID.  # noqa: E501

        :return: The signature_id of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """Sets the signature_id of this UserSignature.

        Specifies the signature ID associated with the signature name. You can use the signature ID in the URI in place of the signature name, and the value stored in the `signatureName` property in the body is used. This allows the use of special characters (such as \"&\", \"<\", \">\") in a the signature name. Note that with each update to signatures, the returned signature ID might change, so the caller will need to trigger off the signature name to get the new signature ID.  # noqa: E501

        :param signature_id: The signature_id of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_id = signature_id

    @property
    def signature_image_uri(self):
        """Gets the signature_image_uri of this UserSignature.  # noqa: E501

        Contains the URI for an endpoint that you can use to retrieve the signature image.  # noqa: E501

        :return: The signature_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_image_uri

    @signature_image_uri.setter
    def signature_image_uri(self, signature_image_uri):
        """Sets the signature_image_uri of this UserSignature.

        Contains the URI for an endpoint that you can use to retrieve the signature image.  # noqa: E501

        :param signature_image_uri: The signature_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_image_uri = signature_image_uri

    @property
    def signature_initials(self):
        """Gets the signature_initials of this UserSignature.  # noqa: E501

         The initials associated with the signature.  # noqa: E501

        :return: The signature_initials of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_initials

    @signature_initials.setter
    def signature_initials(self, signature_initials):
        """Sets the signature_initials of this UserSignature.

         The initials associated with the signature.  # noqa: E501

        :param signature_initials: The signature_initials of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_initials = signature_initials

    @property
    def signature_name(self):
        """Gets the signature_name of this UserSignature.  # noqa: E501

        Specifies the user signature name.  # noqa: E501

        :return: The signature_name of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this UserSignature.

        Specifies the user signature name.  # noqa: E501

        :param signature_name: The signature_name of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_name = signature_name

    @property
    def signature_type(self):
        """Gets the signature_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The signature_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this UserSignature.

          # noqa: E501

        :param signature_type: The signature_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._signature_type = signature_type

    @property
    def stamp_format(self):
        """Gets the stamp_format of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_format of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_format

    @stamp_format.setter
    def stamp_format(self, stamp_format):
        """Sets the stamp_format of this UserSignature.

          # noqa: E501

        :param stamp_format: The stamp_format of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_format = stamp_format

    @property
    def stamp_image_uri(self):
        """Gets the stamp_image_uri of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_image_uri of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_image_uri

    @stamp_image_uri.setter
    def stamp_image_uri(self, stamp_image_uri):
        """Sets the stamp_image_uri of this UserSignature.

          # noqa: E501

        :param stamp_image_uri: The stamp_image_uri of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_image_uri = stamp_image_uri

    @property
    def stamp_size_mm(self):
        """Gets the stamp_size_mm of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_size_mm of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_size_mm

    @stamp_size_mm.setter
    def stamp_size_mm(self, stamp_size_mm):
        """Sets the stamp_size_mm of this UserSignature.

          # noqa: E501

        :param stamp_size_mm: The stamp_size_mm of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_size_mm = stamp_size_mm

    @property
    def stamp_type(self):
        """Gets the stamp_type of this UserSignature.  # noqa: E501

          # noqa: E501

        :return: The stamp_type of this UserSignature.  # noqa: E501
        :rtype: str
        """
        return self._stamp_type

    @stamp_type.setter
    def stamp_type(self, stamp_type):
        """Sets the stamp_type of this UserSignature.

          # noqa: E501

        :param stamp_type: The stamp_type of this UserSignature.  # noqa: E501
        :type: str
        """

        self._stamp_type = stamp_type

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
        if issubclass(UserSignature, dict):
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
        if not isinstance(other, UserSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
