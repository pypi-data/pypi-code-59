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


__all__ = ["SecurityAssociationIpsecInbound", "SecurityAssociationIpsecInboundSchema"]
__pdoc__ = {
    "SecurityAssociationIpsecInboundSchema.resource": False,
    "SecurityAssociationIpsecInbound": False,
}


class SecurityAssociationIpsecInboundSchema(ResourceSchema):
    """The fields of the SecurityAssociationIpsecInbound object"""

    bytes = fields.Integer(data_key="bytes")
    r""" Number of inbound bytes for the IPsec security association. """

    packets = fields.Integer(data_key="packets")
    r""" Number of inbound packets for the IPsec security association. """

    security_parameter_index = fields.Integer(data_key="security_parameter_index")
    r""" Inbound security parameter index for the IPSec security association. """

    @property
    def resource(self):
        return SecurityAssociationIpsecInbound

    @property
    def patchable_fields(self):
        return [
            "bytes",
            "packets",
            "security_parameter_index",
        ]

    @property
    def postable_fields(self):
        return [
            "bytes",
            "packets",
            "security_parameter_index",
        ]


class SecurityAssociationIpsecInbound(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityAssociationIpsecInboundSchema
