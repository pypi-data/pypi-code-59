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


__all__ = ["SecurityAssociationIke", "SecurityAssociationIkeSchema"]
__pdoc__ = {
    "SecurityAssociationIkeSchema.resource": False,
    "SecurityAssociationIke": False,
}


class SecurityAssociationIkeSchema(ResourceSchema):
    """The fields of the SecurityAssociationIke object"""

    authentication = fields.Str(data_key="authentication")
    r""" Authentication method for internet key exchange protocol.

Valid choices:

* none
* psk
* cert """

    initiator_security_parameter_index = fields.Integer(data_key="initiator_security_parameter_index")
    r""" Initiator's security parameter index for the IKE security association. """

    responder_security_parameter_index = fields.Integer(data_key="responder_security_parameter_index")
    r""" Responder's security parameter index for the IKE security association. """

    state = fields.Str(data_key="state")
    r""" State of the IKE connection.

Valid choices:

* none
* connecting
* established
* dead_peer_probe """

    version = fields.Str(data_key="version")
    r""" Internet key exchange protocol version. """

    @property
    def resource(self):
        return SecurityAssociationIke

    @property
    def patchable_fields(self):
        return [
            "authentication",
            "initiator_security_parameter_index",
            "responder_security_parameter_index",
            "state",
            "version",
        ]

    @property
    def postable_fields(self):
        return [
            "authentication",
            "initiator_security_parameter_index",
            "responder_security_parameter_index",
            "state",
            "version",
        ]


class SecurityAssociationIke(Resource):  # pylint: disable=missing-docstring

    _schema = SecurityAssociationIkeSchema
