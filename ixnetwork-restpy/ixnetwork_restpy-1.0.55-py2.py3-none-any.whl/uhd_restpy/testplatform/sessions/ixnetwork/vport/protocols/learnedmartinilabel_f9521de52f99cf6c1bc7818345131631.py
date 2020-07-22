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


class LearnedMartiniLabel(Base):
    """
    The LearnedMartiniLabel class encapsulates a list of learnedMartiniLabel resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedMartiniLabel.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedMartiniLabel'
    _SDM_ATT_MAP = {
        'CBit': 'cBit',
        'Cas': 'cas',
        'CemOption': 'cemOption',
        'CemPayloadBytes': 'cemPayloadBytes',
        'Description': 'description',
        'DisCeAddress': 'disCeAddress',
        'Frequency': 'frequency',
        'GroupId': 'groupId',
        'IncludeRtpHeader': 'includeRtpHeader',
        'Label': 'label',
        'LabelSpaceId': 'labelSpaceId',
        'LocalPwSubStatus': 'localPwSubStatus',
        'MaxAtmCell': 'maxAtmCell',
        'Mtu': 'mtu',
        'PayloadSize': 'payloadSize',
        'PayloadType': 'payloadType',
        'Peer': 'peer',
        'PeerPwSubStatus': 'peerPwSubStatus',
        'PwState': 'pwState',
        'Sp': 'sp',
        'Ssrc': 'ssrc',
        'TdmBitrate': 'tdmBitrate',
        'TimestampMode': 'timestampMode',
        'VcId': 'vcId',
        'VcType': 'vcType',
    }

    def __init__(self, parent):
        super(LearnedMartiniLabel, self).__init__(parent)

    @property
    def CBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CBit'])

    @property
    def Cas(self):
        """
        Returns
        -------
        - str(e1Trunk | t1EsfTrunk | t1SfTrunk): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cas'])

    @property
    def CemOption(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemOption'])

    @property
    def CemPayloadBytes(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemPayloadBytes'])

    @property
    def Description(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def DisCeAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisCeAddress'])

    @property
    def Frequency(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Frequency'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def IncludeRtpHeader(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeRtpHeader'])

    @property
    def Label(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Label'])

    @property
    def LabelSpaceId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelSpaceId'])

    @property
    def LocalPwSubStatus(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPwSubStatus'])

    @property
    def MaxAtmCell(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxAtmCell'])

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])

    @property
    def PayloadSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadSize'])

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadType'])

    @property
    def Peer(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peer'])

    @property
    def PeerPwSubStatus(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerPwSubStatus'])

    @property
    def PwState(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PwState'])

    @property
    def Sp(self):
        """
        Returns
        -------
        - str(hexVal1 | hexVal2 | hexVal3 | hexVal4): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sp'])

    @property
    def Ssrc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ssrc'])

    @property
    def TdmBitrate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TdmBitrate'])

    @property
    def TimestampMode(self):
        """
        Returns
        -------
        - str(absolute | differential): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampMode'])

    @property
    def VcId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcId'])

    @property
    def VcType(self):
        """
        Returns
        -------
        - str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcType'])

    def find(self, CBit=None, Cas=None, CemOption=None, CemPayloadBytes=None, Description=None, DisCeAddress=None, Frequency=None, GroupId=None, IncludeRtpHeader=None, Label=None, LabelSpaceId=None, LocalPwSubStatus=None, MaxAtmCell=None, Mtu=None, PayloadSize=None, PayloadType=None, Peer=None, PeerPwSubStatus=None, PwState=None, Sp=None, Ssrc=None, TdmBitrate=None, TimestampMode=None, VcId=None, VcType=None):
        """Finds and retrieves learnedMartiniLabel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedMartiniLabel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedMartiniLabel resources from the server.

        Args
        ----
        - CBit (bool): 
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): 
        - CemOption (number): 
        - CemPayloadBytes (number): 
        - Description (str): 
        - DisCeAddress (str): 
        - Frequency (number): 
        - GroupId (number): 
        - IncludeRtpHeader (bool): 
        - Label (number): 
        - LabelSpaceId (number): 
        - LocalPwSubStatus (number): 
        - MaxAtmCell (number): 
        - Mtu (number): 
        - PayloadSize (number): 
        - PayloadType (number): 
        - Peer (str): 
        - PeerPwSubStatus (number): 
        - PwState (bool): 
        - Sp (str(hexVal1 | hexVal2 | hexVal3 | hexVal4)): 
        - Ssrc (number): 
        - TdmBitrate (number): 
        - TimestampMode (str(absolute | differential)): 
        - VcId (number): 
        - VcType (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619)): 

        Returns
        -------
        - self: This instance with matching learnedMartiniLabel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedMartiniLabel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedMartiniLabel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
