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


__all__ = ["SecurityAssociationIpsecOutbound", "SecurityAssociationIpsecOutboundSchema"]
__pdoc__ = {
    "SecurityAssociationIpsecOutboundSchema.resource": False,
    "SecurityAssociationIpsecOutbound": False,
}


class SecurityAssociationIpsecOutboundSchema(ResourceSchema):
    """The fields of the SecurityAssociationIpsecOutbound object"""

    bytes = fields.Integer(data_key="bytes")
    r""" Number of outbound bytes for the IPsec security association. """

    packets = fields.Integer(data_key="packets")
    r""" Number of outbound packets for the IPsec security association. """

    security_parameter_index = fields.Integer(data_key="security_parameter_index")
    r""" Outbound security parameter index for the IPSec security association. """

    @property
    def resource(self):
        return SecurityAssociationIpsecOutbound

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


class SecurityAssociationIpsecOutbound(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityAssociationIpsecOutboundSchema
