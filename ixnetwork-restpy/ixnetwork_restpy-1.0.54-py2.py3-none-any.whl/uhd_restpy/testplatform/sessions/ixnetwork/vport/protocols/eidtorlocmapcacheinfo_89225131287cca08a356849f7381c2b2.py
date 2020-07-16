# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class EidToRlocMapCacheInfo(Base):
    """
    The EidToRlocMapCacheInfo class encapsulates a list of eidToRlocMapCacheInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the EidToRlocMapCacheInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'eidToRlocMapCacheInfo'
    _SDM_ATT_MAP = {
        'Action': 'action',
        'ExpiresAfter': 'expiresAfter',
        'InstanceId': 'instanceId',
        'MapReplyRx': 'mapReplyRx',
        'MapRequestTx': 'mapRequestTx',
        'MapVersionNumber': 'mapVersionNumber',
        'NegativeMapReplyRx': 'negativeMapReplyRx',
        'RemoteEidMappingStatus': 'remoteEidMappingStatus',
        'RemoteEidPrefix': 'remoteEidPrefix',
        'RemoteEidPrefixAfi': 'remoteEidPrefixAfi',
        'RemoteEidPrefixLength': 'remoteEidPrefixLength',
        'ResponderIp': 'responderIp',
        'RlocProbeReplyRx': 'rlocProbeReplyRx',
        'RlocProbeRequestTx': 'rlocProbeRequestTx',
    }

    def __init__(self, parent):
        super(EidToRlocMapCacheInfo, self).__init__(parent)

    @property
    def RemoteLocators(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_96410d05b977962f780a8f3077813cee.RemoteLocators): An instance of the RemoteLocators class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_96410d05b977962f780a8f3077813cee import RemoteLocators
        return RemoteLocators(self)

    @property
    def Action(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Action'])

    @property
    def ExpiresAfter(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpiresAfter'])

    @property
    def InstanceId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstanceId'])

    @property
    def MapReplyRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapReplyRx'])

    @property
    def MapRequestTx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapRequestTx'])

    @property
    def MapVersionNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapVersionNumber'])

    @property
    def NegativeMapReplyRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegativeMapReplyRx'])

    @property
    def RemoteEidMappingStatus(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteEidMappingStatus'])

    @property
    def RemoteEidPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteEidPrefix'])

    @property
    def RemoteEidPrefixAfi(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteEidPrefixAfi'])

    @property
    def RemoteEidPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteEidPrefixLength'])

    @property
    def ResponderIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponderIp'])

    @property
    def RlocProbeReplyRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RlocProbeReplyRx'])

    @property
    def RlocProbeRequestTx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RlocProbeRequestTx'])

    def find(self, Action=None, ExpiresAfter=None, InstanceId=None, MapReplyRx=None, MapRequestTx=None, MapVersionNumber=None, NegativeMapReplyRx=None, RemoteEidMappingStatus=None, RemoteEidPrefix=None, RemoteEidPrefixAfi=None, RemoteEidPrefixLength=None, ResponderIp=None, RlocProbeReplyRx=None, RlocProbeRequestTx=None):
        """Finds and retrieves eidToRlocMapCacheInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eidToRlocMapCacheInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eidToRlocMapCacheInfo resources from the server.

        Args
        ----
        - Action (str): 
        - ExpiresAfter (str): 
        - InstanceId (number): 
        - MapReplyRx (number): 
        - MapRequestTx (number): 
        - MapVersionNumber (number): 
        - NegativeMapReplyRx (number): 
        - RemoteEidMappingStatus (str): 
        - RemoteEidPrefix (str): 
        - RemoteEidPrefixAfi (str): 
        - RemoteEidPrefixLength (number): 
        - ResponderIp (str): 
        - RlocProbeReplyRx (number): 
        - RlocProbeRequestTx (number): 

        Returns
        -------
        - self: This instance with matching eidToRlocMapCacheInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eidToRlocMapCacheInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eidToRlocMapCacheInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
