# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview

* Collection Get: GET security/ipsec/security-associatios
* Instance Get: GET security/ipsec/security-associations/uuid
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SecurityAssociation", "SecurityAssociationSchema"]
__pdoc__ = {
    "SecurityAssociationSchema.resource": False,
    "SecurityAssociationSchema.patchable_fields": False,
    "SecurityAssociationSchema.postable_fields": False,
}


class SecurityAssociationSchema(ResourceSchema):
    """The fields of the SecurityAssociation object"""

    cipher_suite = fields.Str(
        data_key="cipher_suite",
        validate=enum_validation(['aescbc', 'gcm256', 'gmac256']),
    )
    r""" Cipher suite for the security association.

Valid choices:

* aescbc
* gcm256
* gmac256 """

    ike = fields.Nested("netapp_ontap.models.security_association_ike.SecurityAssociationIkeSchema", data_key="ike", unknown=EXCLUDE)
    r""" The ike field of the security_association. """

    ipsec = fields.Nested("netapp_ontap.models.security_association_ipsec.SecurityAssociationIpsecSchema", data_key="ipsec", unknown=EXCLUDE)
    r""" The ipsec field of the security_association. """

    lifetime = fields.Integer(
        data_key="lifetime",
    )
    r""" Lifetime for the security association in seconds. """

    local_address = fields.Str(
        data_key="local_address",
    )
    r""" Local address of the security association. """

    name = fields.Str(
        data_key="name",
    )
    r""" Policy name for the security association. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the security_association. """

    remote_address = fields.Str(
        data_key="remote_address",
    )
    r""" Remote address of the security association. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the security_association. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['ipsec', 'ike']),
    )
    r""" Type of security association, it can be IPsec or IKE (Internet Key Exchange).

Valid choices:

* ipsec
* ike """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique identifier of the security association. """

    @property
    def resource(self):
        return SecurityAssociation

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
        ]

class SecurityAssociation(Resource):
    r""" Security association object for IPsec security association and IKE (Internet Key Exchange) security association. """

    _schema = SecurityAssociationSchema
    _path = "/api/security/ipsec/security-associations"
    @property
    def _keys(self):
        return ["uuid"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the IPsec and IKE (Internet Key Exchange) security associations.
### Related ONTAP commands
* `security ipsec show-ipsecsa`
* `security ipsec show-ikesa`

### Learn more
* [`DOC /security/ipsec/security-associations`](#docs-security-security_ipsec_security-associations)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        r"""Retrieves the IPsec and IKE (Internet Key Exchange) security associations.
### Related ONTAP commands
* `security ipsec show-ipsecsa`
* `security ipsec show-ikesa`

### Learn more
* [`DOC /security/ipsec/security-associations`](#docs-security-security_ipsec_security-associations)"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the IPsec and IKE (Internet Key Exchange) security associations.
### Related ONTAP commands
* `security ipsec show-ipsecsa`
* `security ipsec show-ikesa`

### Learn more
* [`DOC /security/ipsec/security-associations`](#docs-security-security_ipsec_security-associations)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific IPsec or IKE (Internet Key Exchange) security association.
### Related ONTAP commands
* `security ipsec show-ipsecsa`
* `security ipsec show-ikesa`

### Learn more
* [`DOC /security/ipsec/security-associations`](#docs-security-security_ipsec_security-associations)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





