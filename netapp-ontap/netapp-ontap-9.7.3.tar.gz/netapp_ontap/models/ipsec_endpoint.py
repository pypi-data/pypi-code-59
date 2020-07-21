# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["IpsecEndpoint", "IpsecEndpointSchema"]
__pdoc__ = {
    "IpsecEndpointSchema.resource": False,
    "IpsecEndpoint": False,
}


class IpsecEndpointSchema(ResourceSchema):
    """The fields of the IpsecEndpoint object"""

    address = fields.Str(data_key="address")
    r""" The address field of the ipsec_endpoint. """

    family = fields.Str(data_key="family")
    r""" The family field of the ipsec_endpoint. """

    netmask = fields.Str(data_key="netmask")
    r""" The netmask field of the ipsec_endpoint. """

    port = fields.Str(data_key="port")
    r""" Application port to be covered by the IPsec policy

Example: 23 """

    @property
    def resource(self):
        return IpsecEndpoint

    @property
    def patchable_fields(self):
        return [
            "address",
            "family",
            "netmask",
            "port",
        ]

    @property
    def postable_fields(self):
        return [
            "address",
            "family",
            "netmask",
            "port",
        ]


class IpsecEndpoint(Resource):  # pylint: disable=missing-docstring

    _schema = IpsecEndpointSchema
