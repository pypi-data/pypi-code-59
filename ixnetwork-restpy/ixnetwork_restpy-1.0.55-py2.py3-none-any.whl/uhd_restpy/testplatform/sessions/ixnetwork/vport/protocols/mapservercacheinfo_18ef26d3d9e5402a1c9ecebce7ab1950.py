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


class MapServerCacheInfo(Base):
    """
    The MapServerCacheInfo class encapsulates a list of mapServerCacheInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the MapServerCacheInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'mapServerCacheInfo'
    _SDM_ATT_MAP = {
        'Action': 'action',
        'EidPrefix': 'eidPrefix',
        'EidPrefixAfi': 'eidPrefixAfi',
        'EidPrefixLength': 'eidPrefixLength',
        'EtrIp': 'etrIp',
        'ExpiresAfter': 'expiresAfter',
        'InstanceId': 'instanceId',
        'Ipv4ErrorMapRegisterRx': 'ipv4ErrorMapRegisterRx',
        'Ipv4MapNotifyTx': 'ipv4MapNotifyTx',
        'Ipv4MapRegisterRx': 'ipv4MapRegisterRx',
        'Ipv4MapRequestDropped': 'ipv4MapRequestDropped',
        'Ipv6ErrorMapRegisterRx': 'ipv6ErrorMapRegisterRx',
        'Ipv6MapNotifyTx': 'ipv6MapNotifyTx',
        'Ipv6MapRegisterRx': 'ipv6MapRegisterRx',
        'Ipv6MapRequestDropped': 'ipv6MapRequestDropped',
        'Key': 'key',
        'MapVersionNumber': 'mapVersionNumber',
        'ProxyMapReply': 'proxyMapReply',
        'WantMapNotify': 'wantMapNotify',
    }

    def __init__(self, parent):
        super(MapServerCacheInfo, self).__init__(parent)

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
    def EidPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefix'])

    @property
    def EidPrefixAfi(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefixAfi'])

    @property
    def EidPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EidPrefixLength'])

    @property
    def EtrIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EtrIp'])

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
    def Ipv4ErrorMapRegisterRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4ErrorMapRegisterRx'])

    @property
    def Ipv4MapNotifyTx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapNotifyTx'])

    @property
    def Ipv4MapRegisterRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRegisterRx'])

    @property
    def Ipv4MapRequestDropped(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MapRequestDropped'])

    @property
    def Ipv6ErrorMapRegisterRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6ErrorMapRegisterRx'])

    @property
    def Ipv6MapNotifyTx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapNotifyTx'])

    @property
    def Ipv6MapRegisterRx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRegisterRx'])

    @property
    def Ipv6MapRequestDropped(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MapRequestDropped'])

    @property
    def Key(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Key'])

    @property
    def MapVersionNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapVersionNumber'])

    @property
    def ProxyMapReply(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProxyMapReply'])

    @property
    def WantMapNotify(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['WantMapNotify'])

    def find(self, Action=None, EidPrefix=None, EidPrefixAfi=None, EidPrefixLength=None, EtrIp=None, ExpiresAfter=None, InstanceId=None, Ipv4ErrorMapRegisterRx=None, Ipv4MapNotifyTx=None, Ipv4MapRegisterRx=None, Ipv4MapRequestDropped=None, Ipv6ErrorMapRegisterRx=None, Ipv6MapNotifyTx=None, Ipv6MapRegisterRx=None, Ipv6MapRequestDropped=None, Key=None, MapVersionNumber=None, ProxyMapReply=None, WantMapNotify=None):
        """Finds and retrieves mapServerCacheInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mapServerCacheInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mapServerCacheInfo resources from the server.

        Args
        ----
        - Action (str): 
        - EidPrefix (str): 
        - EidPrefixAfi (str): 
        - EidPrefixLength (number): 
        - EtrIp (str): 
        - ExpiresAfter (str): 
        - InstanceId (number): 
        - Ipv4ErrorMapRegisterRx (number): 
        - Ipv4MapNotifyTx (number): 
        - Ipv4MapRegisterRx (number): 
        - Ipv4MapRequestDropped (number): 
        - Ipv6ErrorMapRegisterRx (number): 
        - Ipv6MapNotifyTx (number): 
        - Ipv6MapRegisterRx (number): 
        - Ipv6MapRequestDropped (number): 
        - Key (str): 
        - MapVersionNumber (number): 
        - ProxyMapReply (bool): 
        - WantMapNotify (bool): 

        Returns
        -------
        - self: This instance with matching mapServerCacheInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mapServerCacheInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mapServerCacheInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
