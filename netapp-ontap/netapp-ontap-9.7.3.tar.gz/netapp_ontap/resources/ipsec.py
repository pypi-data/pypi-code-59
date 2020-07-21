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

* GET to retrieve the IPsec status: GET security/ipsec
* Patch to update IPsec status: PATCH security/ipsec
"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Ipsec", "IpsecSchema"]
__pdoc__ = {
    "IpsecSchema.resource": False,
    "IpsecSchema.patchable_fields": False,
    "IpsecSchema.postable_fields": False,
}


class IpsecSchema(ResourceSchema):
    """The fields of the Ipsec object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the ipsec. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Indicates whether or not IPsec is enabled. """

    @property
    def resource(self):
        return Ipsec

    @property
    def patchable_fields(self):
        return [
            "links",
            "enabled",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
            "enabled",
        ]

class Ipsec(Resource):
    r""" Manages IPsec configuration via REST APIs. """

    _schema = IpsecSchema
    _path = "/api/security/ipsec"






    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves IPsec configuration via REST APIs.
### Related ONTAP commands
* 'security ipsec config show'

### Learn more
* [`DOC /security/ipsec`](#docs-security-security_ipsec)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member


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
        r"""Updates IPsec configuration via REST APIs.
### Related ONTAP commands
* 'security ipsec config modify'

### Learn more
* [`DOC /security/ipsec`](#docs-security-security_ipsec)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)  # pylint: disable=no-member



