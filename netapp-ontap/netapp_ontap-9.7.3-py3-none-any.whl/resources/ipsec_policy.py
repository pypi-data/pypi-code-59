# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.

## Overview
The following operations are supported:

* Collection Get: GET security/ipsec/policies
* Creation Post: POST security/ipsec/policies
* Instance Get: GET security/ipsec/policies/uuid
* Instance Patch: PATCH security/ipsec/policies/uuid
* Instance Delete: DELETE security/ipsec/policies/uuid
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["IpsecPolicy", "IpsecPolicySchema"]
__pdoc__ = {
    "IpsecPolicySchema.resource": False,
    "IpsecPolicySchema.patchable_fields": False,
    "IpsecPolicySchema.postable_fields": False,
}


class IpsecPolicySchema(ResourceSchema):
    """The fields of the IpsecPolicy object"""

    action = fields.Str(
        data_key="action",
        validate=enum_validation(['bypass', 'discard', 'esp_transport']),
    )
    r""" Action for the IPsec policy.

Valid choices:

* bypass
* discard
* esp_transport """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Indicates whether or not the policy is enabled. """

    local_endpoint = fields.Nested("netapp_ontap.models.ipsec_endpoint.IpsecEndpointSchema", data_key="local_endpoint", unknown=EXCLUDE)
    r""" The local_endpoint field of the ipsec_policy. """

    name = fields.Str(
        data_key="name",
    )
    r""" IPsec policy name. """

    protocol = fields.Str(
        data_key="protocol",
    )
    r""" Lower layer protocol to be covered by the IPsec policy.

Example: 17 """

    remote_endpoint = fields.Nested("netapp_ontap.models.ipsec_endpoint.IpsecEndpointSchema", data_key="remote_endpoint", unknown=EXCLUDE)
    r""" The remote_endpoint field of the ipsec_policy. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for interfaces owned by an SVM. Otherwise, set to "cluster".

Valid choices:

* svm
* cluster """

    secret_key = fields.Str(
        data_key="secret_key",
        validate=len_validation(minimum=18, maximum=128),
    )
    r""" Pre-shared key for IKE negotiation. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the ipsec_policy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique identifier of the IPsec policy.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return IpsecPolicy

    @property
    def patchable_fields(self):
        return [
            "enabled",
            "name",
            "protocol",
            "svm.name",
            "svm.uuid",
        ]

    @property
    def postable_fields(self):
        return [
            "action",
            "enabled",
            "name",
            "protocol",
            "secret_key",
            "svm.name",
            "svm.uuid",
        ]

class IpsecPolicy(Resource):
    r""" IPsec policy object. """

    _schema = IpsecPolicySchema
    _path = "/api/security/ipsec/policies"
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
        r"""Retrieves the collection of IPsec policies.
### Related ONTAP commands
* `security ipsec policy show`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
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
        r"""Retrieves the collection of IPsec policies.
### Related ONTAP commands
* `security ipsec policy show`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a specific IPsec policy.
### Related ONTAP commands
* `security ipsec policy modify`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._patch_collection(body, *args, connection=connection, **kwargs)

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a specific IPsec policy.
### Related ONTAP commands
* `security ipsec policy delete`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the collection of IPsec policies.
### Related ONTAP commands
* `security ipsec policy show`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific IPsec policy.
### Related ONTAP commands
* `security ipsec policy show`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates an IPsec policy.
### Related ONTAP commands
* `security ipsec policy create`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a specific IPsec policy.
### Related ONTAP commands
* `security ipsec policy modify`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    # pylint: disable=bad-continuation
    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a specific IPsec policy.
### Related ONTAP commands
* `security ipsec policy delete`

### Learn more
* [`DOC /security/ipsec/policies`](#docs-security-security_ipsec_policies)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)  # pylint: disable=no-member


