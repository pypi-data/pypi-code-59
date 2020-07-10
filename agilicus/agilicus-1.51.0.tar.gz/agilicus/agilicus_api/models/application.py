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


class Application(object):
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
        'created': 'datetime',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'category': 'str',
        'image': 'str',
        'image_username': 'str',
        'image_password': 'str',
        'image_credentials_type': 'str',
        'environments': 'list[Environment]',
        'org_id': 'str',
        'contact_email': 'str',
        'port': 'int',
        'healthcheck_uri': 'str',
        'roles': 'RoleList',
        'definitions': 'list[Definition]',
        'assignments': 'list[ApplicationAssignment]',
        'owned': 'bool',
        'maintained': 'bool',
        'assigned': 'bool',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'category': 'category',
        'image': 'image',
        'image_username': 'image_username',
        'image_password': 'image_password',
        'image_credentials_type': 'image_credentials_type',
        'environments': 'environments',
        'org_id': 'org_id',
        'contact_email': 'contact_email',
        'port': 'port',
        'healthcheck_uri': 'healthcheck_uri',
        'roles': 'roles',
        'definitions': 'definitions',
        'assignments': 'assignments',
        'owned': 'owned',
        'maintained': 'maintained',
        'assigned': 'assigned',
        'updated': 'updated'
    }

    def __init__(self, created=None, id=None, name=None, description=None, category=None, image=None, image_username=None, image_password=None, image_credentials_type=None, environments=None, org_id=None, contact_email=None, port=5000, healthcheck_uri=None, roles=None, definitions=None, assignments=None, owned=None, maintained=None, assigned=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """Application - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._id = None
        self._name = None
        self._description = None
        self._category = None
        self._image = None
        self._image_username = None
        self._image_password = None
        self._image_credentials_type = None
        self._environments = None
        self._org_id = None
        self._contact_email = None
        self._port = None
        self._healthcheck_uri = None
        self._roles = None
        self._definitions = None
        self._assignments = None
        self._owned = None
        self._maintained = None
        self._assigned = None
        self._updated = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.category = category
        if image is not None:
            self.image = image
        if image_username is not None:
            self.image_username = image_username
        if image_password is not None:
            self.image_password = image_password
        if image_credentials_type is not None:
            self.image_credentials_type = image_credentials_type
        if environments is not None:
            self.environments = environments
        self.org_id = org_id
        if contact_email is not None:
            self.contact_email = contact_email
        if port is not None:
            self.port = port
        if healthcheck_uri is not None:
            self.healthcheck_uri = healthcheck_uri
        if roles is not None:
            self.roles = roles
        if definitions is not None:
            self.definitions = definitions
        if assignments is not None:
            self.assignments = assignments
        if owned is not None:
            self.owned = owned
        if maintained is not None:
            self.maintained = maintained
        if assigned is not None:
            self.assigned = assigned
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this Application.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Application.

        Creation time  # noqa: E501

        :param created: The created of this Application.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        application service id  # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        application service id  # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501

        application name  # noqa: E501

        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        application name  # noqa: E501

        :param name: The name of this Application.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 63):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9-:]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9-:]+$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Application.  # noqa: E501

        Application description text  # noqa: E501

        :return: The description of this Application.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.

        Application description text  # noqa: E501

        :param description: The description of this Application.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this Application.  # noqa: E501

        application category  # noqa: E501

        :return: The category of this Application.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Application.

        application category  # noqa: E501

        :param category: The category of this Application.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 100):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 1):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501

        self._category = category

    @property
    def image(self):
        """Gets the image of this Application.  # noqa: E501

        image registry path and name  # noqa: E501

        :return: The image of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Application.

        image registry path and name  # noqa: E501

        :param image: The image of this Application.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_username(self):
        """Gets the image_username of this Application.  # noqa: E501

        registry username  # noqa: E501

        :return: The image_username of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image_username

    @image_username.setter
    def image_username(self, image_username):
        """Sets the image_username of this Application.

        registry username  # noqa: E501

        :param image_username: The image_username of this Application.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_username is not None and len(image_username) > 100):
            raise ValueError("Invalid value for `image_username`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_username is not None and len(image_username) < 1):
            raise ValueError("Invalid value for `image_username`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_username = image_username

    @property
    def image_password(self):
        """Gets the image_password of this Application.  # noqa: E501

        registry password  # noqa: E501

        :return: The image_password of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image_password

    @image_password.setter
    def image_password(self, image_password):
        """Sets the image_password of this Application.

        registry password  # noqa: E501

        :param image_password: The image_password of this Application.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_password is not None and len(image_password) > 100):
            raise ValueError("Invalid value for `image_password`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_password is not None and len(image_password) < 1):
            raise ValueError("Invalid value for `image_password`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_password = image_password

    @property
    def image_credentials_type(self):
        """Gets the image_credentials_type of this Application.  # noqa: E501

        type of credentials for image  # noqa: E501

        :return: The image_credentials_type of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image_credentials_type

    @image_credentials_type.setter
    def image_credentials_type(self, image_credentials_type):
        """Sets the image_credentials_type of this Application.

        type of credentials for image  # noqa: E501

        :param image_credentials_type: The image_credentials_type of this Application.  # noqa: E501
        :type: str
        """
        allowed_values = ["basic_auth", "token"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and image_credentials_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `image_credentials_type` ({0}), must be one of {1}"  # noqa: E501
                .format(image_credentials_type, allowed_values)
            )

        self._image_credentials_type = image_credentials_type

    @property
    def environments(self):
        """Gets the environments of this Application.  # noqa: E501

        List of environments  # noqa: E501

        :return: The environments of this Application.  # noqa: E501
        :rtype: list[Environment]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this Application.

        List of environments  # noqa: E501

        :param environments: The environments of this Application.  # noqa: E501
        :type: list[Environment]
        """

        self._environments = environments

    @property
    def org_id(self):
        """Gets the org_id of this Application.  # noqa: E501

        organisation id  # noqa: E501

        :return: The org_id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Application.

        organisation id  # noqa: E501

        :param org_id: The org_id of this Application.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) > 40):
            raise ValueError("Invalid value for `org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) < 1):
            raise ValueError("Invalid value for `org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._org_id = org_id

    @property
    def contact_email(self):
        """Gets the contact_email of this Application.  # noqa: E501

        Administrator contact email  # noqa: E501

        :return: The contact_email of this Application.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Application.

        Administrator contact email  # noqa: E501

        :param contact_email: The contact_email of this Application.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                contact_email is not None and len(contact_email) > 100):
            raise ValueError("Invalid value for `contact_email`, length must be less than or equal to `100`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def port(self):
        """Gets the port of this Application.  # noqa: E501

        The transport layer port the application listens on for requests. E.g. if the application listens for HTTP requests on the standard port, port 80, set this to 80.   # noqa: E501

        :return: The port of this Application.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Application.

        The transport layer port the application listens on for requests. E.g. if the application listens for HTTP requests on the standard port, port 80, set this to 80.   # noqa: E501

        :param port: The port of this Application.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def healthcheck_uri(self):
        """Gets the healthcheck_uri of this Application.  # noqa: E501

        health check URI  # noqa: E501

        :return: The healthcheck_uri of this Application.  # noqa: E501
        :rtype: str
        """
        return self._healthcheck_uri

    @healthcheck_uri.setter
    def healthcheck_uri(self, healthcheck_uri):
        """Sets the healthcheck_uri of this Application.

        health check URI  # noqa: E501

        :param healthcheck_uri: The healthcheck_uri of this Application.  # noqa: E501
        :type: str
        """

        self._healthcheck_uri = healthcheck_uri

    @property
    def roles(self):
        """Gets the roles of this Application.  # noqa: E501


        :return: The roles of this Application.  # noqa: E501
        :rtype: RoleList
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Application.


        :param roles: The roles of this Application.  # noqa: E501
        :type: RoleList
        """

        self._roles = roles

    @property
    def definitions(self):
        """Gets the definitions of this Application.  # noqa: E501

        List of definitions  # noqa: E501

        :return: The definitions of this Application.  # noqa: E501
        :rtype: list[Definition]
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """Sets the definitions of this Application.

        List of definitions  # noqa: E501

        :param definitions: The definitions of this Application.  # noqa: E501
        :type: list[Definition]
        """

        self._definitions = definitions

    @property
    def assignments(self):
        """Gets the assignments of this Application.  # noqa: E501

        Controls the Organisations which have access to Environments of this Application.   # noqa: E501

        :return: The assignments of this Application.  # noqa: E501
        :rtype: list[ApplicationAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this Application.

        Controls the Organisations which have access to Environments of this Application.   # noqa: E501

        :param assignments: The assignments of this Application.  # noqa: E501
        :type: list[ApplicationAssignment]
        """

        self._assignments = assignments

    @property
    def owned(self):
        """Gets the owned of this Application.  # noqa: E501

        Whether this Application is owned by the provided organisation.   # noqa: E501

        :return: The owned of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._owned

    @owned.setter
    def owned(self, owned):
        """Sets the owned of this Application.

        Whether this Application is owned by the provided organisation.   # noqa: E501

        :param owned: The owned of this Application.  # noqa: E501
        :type: bool
        """

        self._owned = owned

    @property
    def maintained(self):
        """Gets the maintained of this Application.  # noqa: E501

        Whether this Application has an Environment maintained by the provided organisation.   # noqa: E501

        :return: The maintained of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._maintained

    @maintained.setter
    def maintained(self, maintained):
        """Sets the maintained of this Application.

        Whether this Application has an Environment maintained by the provided organisation.   # noqa: E501

        :param maintained: The maintained of this Application.  # noqa: E501
        :type: bool
        """

        self._maintained = maintained

    @property
    def assigned(self):
        """Gets the assigned of this Application.  # noqa: E501

        Whether an Environment is assigned to this Application.   # noqa: E501

        :return: The assigned of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """Sets the assigned of this Application.

        Whether an Environment is assigned to this Application.   # noqa: E501

        :param assigned: The assigned of this Application.  # noqa: E501
        :type: bool
        """

        self._assigned = assigned

    @property
    def updated(self):
        """Gets the updated of this Application.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Application.

        Update time  # noqa: E501

        :param updated: The updated of this Application.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, Application):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Application):
            return True

        return self.to_dict() != other.to_dict()
