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


class L2VcRange(Base):
    """
    The L2VcRange class encapsulates a list of l2VcRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2VcRange.find() method.
    The list can be managed by using the L2VcRange.add() and L2VcRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2VcRange'
    _SDM_ATT_MAP = {
        'CapableOfReassembly': 'capableOfReassembly',
        'Cas': 'cas',
        'CeIpAddress': 'ceIpAddress',
        'CemOption': 'cemOption',
        'CemPayload': 'cemPayload',
        'Count': 'count',
        'Description': 'description',
        'DoNotExpandIntoVcs': 'doNotExpandIntoVcs',
        'DownInterval': 'downInterval',
        'DownStartInterval': 'downStartInterval',
        'EnableBfdIpUdpCv': 'enableBfdIpUdpCv',
        'EnableBfdPwAchCv': 'enableBfdPwAchCv',
        'EnableCBit': 'enableCBit',
        'EnableCccvNegotiation': 'enableCccvNegotiation',
        'EnableCemOption': 'enableCemOption',
        'EnableCemPayload': 'enableCemPayload',
        'EnableDescriptionPresent': 'enableDescriptionPresent',
        'EnableLspPingCv': 'enableLspPingCv',
        'EnableMaxAtmPresent': 'enableMaxAtmPresent',
        'EnableMtuPresent': 'enableMtuPresent',
        'EnablePacking': 'enablePacking',
        'EnablePwAchCc': 'enablePwAchCc',
        'EnablePwStatusTlv': 'enablePwStatusTlv',
        'EnableRouterAlertCc': 'enableRouterAlertCc',
        'Enabled': 'enabled',
        'FecType': 'fecType',
        'Frequency': 'frequency',
        'IncludeRtpHeader': 'includeRtpHeader',
        'IncludeSsrc': 'includeSsrc',
        'IncludeTdmBitrate': 'includeTdmBitrate',
        'IncludeTdmOption': 'includeTdmOption',
        'IncludeTdmPayload': 'includeTdmPayload',
        'IpType': 'ipType',
        'LabelMode': 'labelMode',
        'LabelStart': 'labelStart',
        'MaxNumberOfAtmCells': 'maxNumberOfAtmCells',
        'Mtu': 'mtu',
        'PayloadType': 'payloadType',
        'PeerAddress': 'peerAddress',
        'ProvisioningModel': 'provisioningModel',
        'PwStatusCode': 'pwStatusCode',
        'RepeatCount': 'repeatCount',
        'SendPwStatus': 'sendPwStatus',
        'SourceAiiAsIp': 'sourceAiiAsIp',
        'SourceAiiAsNumber': 'sourceAiiAsNumber',
        'SourceAiiType': 'sourceAiiType',
        'Sp': 'sp',
        'Ssrc': 'ssrc',
        'Step': 'step',
        'TargetAiiAsIp': 'targetAiiAsIp',
        'TargetAiiAsNumber': 'targetAiiAsNumber',
        'TargetAiiType': 'targetAiiType',
        'TdmBitrate': 'tdmBitrate',
        'TdmDataSize': 'tdmDataSize',
        'TimestampMode': 'timestampMode',
        'UpInterval': 'upInterval',
        'VcId': 'vcId',
        'VcIdStep': 'vcIdStep',
        'VplsIdAsNumber': 'vplsIdAsNumber',
        'VplsIdAsNumberStep': 'vplsIdAsNumberStep',
        'VplsIdAssignedNumber': 'vplsIdAssignedNumber',
        'VplsIdAssignedNumberStep': 'vplsIdAssignedNumberStep',
        'VplsIdCount': 'vplsIdCount',
        'VplsIdIpAddress': 'vplsIdIpAddress',
        'VplsIdIpAddressStep': 'vplsIdIpAddressStep',
        'VplsIdType': 'vplsIdType',
    }

    def __init__(self, parent):
        super(L2VcRange, self).__init__(parent)

    @property
    def L2MacVlanRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2macvlanrange_36baa7785cd8b38a46986e297ae96a88.L2MacVlanRange): An instance of the L2MacVlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2macvlanrange_36baa7785cd8b38a46986e297ae96a88 import L2MacVlanRange
        return L2MacVlanRange(self)._select()

    @property
    def L2VcIpRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vciprange_b16a8fc51e54b59051680c68da42d9ab.L2VcIpRange): An instance of the L2VcIpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vciprange_b16a8fc51e54b59051680c68da42d9ab import L2VcIpRange
        return L2VcIpRange(self)._select()

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficgroupid_dbbea754aa76dde537237a1dd3913088.TrafficGroupId): An instance of the TrafficGroupId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.trafficgroupid_dbbea754aa76dde537237a1dd3913088 import TrafficGroupId
        return TrafficGroupId(self)

    @property
    def CapableOfReassembly(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CapableOfReassembly'])
    @CapableOfReassembly.setter
    def CapableOfReassembly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CapableOfReassembly'], value)

    @property
    def Cas(self):
        """
        Returns
        -------
        - str(e1Trunk | t1EsfTrunk | t1SfTrunk): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cas'])
    @Cas.setter
    def Cas(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cas'], value)

    @property
    def CeIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CeIpAddress'])
    @CeIpAddress.setter
    def CeIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CeIpAddress'], value)

    @property
    def CemOption(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemOption'])
    @CemOption.setter
    def CemOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CemOption'], value)

    @property
    def CemPayload(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemPayload'])
    @CemPayload.setter
    def CemPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CemPayload'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def DoNotExpandIntoVcs(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DoNotExpandIntoVcs'])
    @DoNotExpandIntoVcs.setter
    def DoNotExpandIntoVcs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DoNotExpandIntoVcs'], value)

    @property
    def DownInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownInterval'])
    @DownInterval.setter
    def DownInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownInterval'], value)

    @property
    def DownStartInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownStartInterval'])
    @DownStartInterval.setter
    def DownStartInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownStartInterval'], value)

    @property
    def EnableBfdIpUdpCv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdIpUdpCv'])
    @EnableBfdIpUdpCv.setter
    def EnableBfdIpUdpCv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdIpUdpCv'], value)

    @property
    def EnableBfdPwAchCv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdPwAchCv'])
    @EnableBfdPwAchCv.setter
    def EnableBfdPwAchCv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdPwAchCv'], value)

    @property
    def EnableCBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCBit'])
    @EnableCBit.setter
    def EnableCBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCBit'], value)

    @property
    def EnableCccvNegotiation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCccvNegotiation'])
    @EnableCccvNegotiation.setter
    def EnableCccvNegotiation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCccvNegotiation'], value)

    @property
    def EnableCemOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCemOption'])
    @EnableCemOption.setter
    def EnableCemOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCemOption'], value)

    @property
    def EnableCemPayload(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCemPayload'])
    @EnableCemPayload.setter
    def EnableCemPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCemPayload'], value)

    @property
    def EnableDescriptionPresent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDescriptionPresent'])
    @EnableDescriptionPresent.setter
    def EnableDescriptionPresent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDescriptionPresent'], value)

    @property
    def EnableLspPingCv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLspPingCv'])
    @EnableLspPingCv.setter
    def EnableLspPingCv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLspPingCv'], value)

    @property
    def EnableMaxAtmPresent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMaxAtmPresent'])
    @EnableMaxAtmPresent.setter
    def EnableMaxAtmPresent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMaxAtmPresent'], value)

    @property
    def EnableMtuPresent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMtuPresent'])
    @EnableMtuPresent.setter
    def EnableMtuPresent(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMtuPresent'], value)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePacking'])
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePacking'], value)

    @property
    def EnablePwAchCc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePwAchCc'])
    @EnablePwAchCc.setter
    def EnablePwAchCc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePwAchCc'], value)

    @property
    def EnablePwStatusTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePwStatusTlv'])
    @EnablePwStatusTlv.setter
    def EnablePwStatusTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePwStatusTlv'], value)

    @property
    def EnableRouterAlertCc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRouterAlertCc'])
    @EnableRouterAlertCc.setter
    def EnableRouterAlertCc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRouterAlertCc'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FecType(self):
        """
        Returns
        -------
        - str(pwIdFec | generalizedIdFecVpls): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FecType'])
    @FecType.setter
    def FecType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FecType'], value)

    @property
    def Frequency(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Frequency'])
    @Frequency.setter
    def Frequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Frequency'], value)

    @property
    def IncludeRtpHeader(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeRtpHeader'])
    @IncludeRtpHeader.setter
    def IncludeRtpHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeRtpHeader'], value)

    @property
    def IncludeSsrc(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeSsrc'])
    @IncludeSsrc.setter
    def IncludeSsrc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeSsrc'], value)

    @property
    def IncludeTdmBitrate(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTdmBitrate'])
    @IncludeTdmBitrate.setter
    def IncludeTdmBitrate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTdmBitrate'], value)

    @property
    def IncludeTdmOption(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTdmOption'])
    @IncludeTdmOption.setter
    def IncludeTdmOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTdmOption'], value)

    @property
    def IncludeTdmPayload(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeTdmPayload'])
    @IncludeTdmPayload.setter
    def IncludeTdmPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeTdmPayload'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - str(none | increment): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelMode'])
    @LabelMode.setter
    def LabelMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelMode'], value)

    @property
    def LabelStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelStart'])
    @LabelStart.setter
    def LabelStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelStart'], value)

    @property
    def MaxNumberOfAtmCells(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfAtmCells'])
    @MaxNumberOfAtmCells.setter
    def MaxNumberOfAtmCells(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNumberOfAtmCells'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadType'])
    @PayloadType.setter
    def PayloadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PayloadType'], value)

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerAddress'])
    @PeerAddress.setter
    def PeerAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeerAddress'], value)

    @property
    def ProvisioningModel(self):
        """
        Returns
        -------
        - str(manualConfiguration | bgpAutoDiscovery): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProvisioningModel'])
    @ProvisioningModel.setter
    def ProvisioningModel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProvisioningModel'], value)

    @property
    def PwStatusCode(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PwStatusCode'])
    @PwStatusCode.setter
    def PwStatusCode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PwStatusCode'], value)

    @property
    def RepeatCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RepeatCount'])
    @RepeatCount.setter
    def RepeatCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RepeatCount'], value)

    @property
    def SendPwStatus(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendPwStatus'])
    @SendPwStatus.setter
    def SendPwStatus(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendPwStatus'], value)

    @property
    def SourceAiiAsIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAiiAsIp'])
    @SourceAiiAsIp.setter
    def SourceAiiAsIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAiiAsIp'], value)

    @property
    def SourceAiiAsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAiiAsNumber'])
    @SourceAiiAsNumber.setter
    def SourceAiiAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAiiAsNumber'], value)

    @property
    def SourceAiiType(self):
        """
        Returns
        -------
        - str(number | ipAddress): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAiiType'])
    @SourceAiiType.setter
    def SourceAiiType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAiiType'], value)

    @property
    def Sp(self):
        """
        Returns
        -------
        - str(hexVal0 | hexVal1 | hexVal2 | hexVal3): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sp'])
    @Sp.setter
    def Sp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Sp'], value)

    @property
    def Ssrc(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ssrc'])
    @Ssrc.setter
    def Ssrc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ssrc'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    @property
    def TargetAiiAsIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetAiiAsIp'])
    @TargetAiiAsIp.setter
    def TargetAiiAsIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetAiiAsIp'], value)

    @property
    def TargetAiiAsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetAiiAsNumber'])
    @TargetAiiAsNumber.setter
    def TargetAiiAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetAiiAsNumber'], value)

    @property
    def TargetAiiType(self):
        """
        Returns
        -------
        - str(number | ipAddress): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetAiiType'])
    @TargetAiiType.setter
    def TargetAiiType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TargetAiiType'], value)

    @property
    def TdmBitrate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TdmBitrate'])
    @TdmBitrate.setter
    def TdmBitrate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TdmBitrate'], value)

    @property
    def TdmDataSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TdmDataSize'])
    @TdmDataSize.setter
    def TdmDataSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TdmDataSize'], value)

    @property
    def TimestampMode(self):
        """
        Returns
        -------
        - str(absolute | differential): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampMode'])
    @TimestampMode.setter
    def TimestampMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimestampMode'], value)

    @property
    def UpInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpInterval'])
    @UpInterval.setter
    def UpInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpInterval'], value)

    @property
    def VcId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcId'])
    @VcId.setter
    def VcId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VcId'], value)

    @property
    def VcIdStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcIdStep'])
    @VcIdStep.setter
    def VcIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VcIdStep'], value)

    @property
    def VplsIdAsNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdAsNumber'])
    @VplsIdAsNumber.setter
    def VplsIdAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdAsNumber'], value)

    @property
    def VplsIdAsNumberStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdAsNumberStep'])
    @VplsIdAsNumberStep.setter
    def VplsIdAsNumberStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdAsNumberStep'], value)

    @property
    def VplsIdAssignedNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdAssignedNumber'])
    @VplsIdAssignedNumber.setter
    def VplsIdAssignedNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdAssignedNumber'], value)

    @property
    def VplsIdAssignedNumberStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdAssignedNumberStep'])
    @VplsIdAssignedNumberStep.setter
    def VplsIdAssignedNumberStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdAssignedNumberStep'], value)

    @property
    def VplsIdCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdCount'])
    @VplsIdCount.setter
    def VplsIdCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdCount'], value)

    @property
    def VplsIdIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdIpAddress'])
    @VplsIdIpAddress.setter
    def VplsIdIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdIpAddress'], value)

    @property
    def VplsIdIpAddressStep(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdIpAddressStep'])
    @VplsIdIpAddressStep.setter
    def VplsIdIpAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdIpAddressStep'], value)

    @property
    def VplsIdType(self):
        """
        Returns
        -------
        - str(asNumber | ipAddress): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsIdType'])
    @VplsIdType.setter
    def VplsIdType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VplsIdType'], value)

    def update(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Updates l2VcRange resource on the server.

        Args
        ----
        - CapableOfReassembly (bool): 
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): 
        - CeIpAddress (str): 
        - CemOption (number): 
        - CemPayload (number): 
        - Count (number): 
        - Description (str): 
        - DoNotExpandIntoVcs (bool): 
        - DownInterval (number): 
        - DownStartInterval (number): 
        - EnableBfdIpUdpCv (bool): 
        - EnableBfdPwAchCv (bool): 
        - EnableCBit (bool): 
        - EnableCccvNegotiation (bool): 
        - EnableCemOption (bool): 
        - EnableCemPayload (bool): 
        - EnableDescriptionPresent (bool): 
        - EnableLspPingCv (bool): 
        - EnableMaxAtmPresent (bool): 
        - EnableMtuPresent (bool): 
        - EnablePacking (bool): 
        - EnablePwAchCc (bool): 
        - EnablePwStatusTlv (bool): 
        - EnableRouterAlertCc (bool): 
        - Enabled (bool): 
        - FecType (str(pwIdFec | generalizedIdFecVpls)): 
        - Frequency (number): 
        - IncludeRtpHeader (bool): 
        - IncludeSsrc (bool): 
        - IncludeTdmBitrate (bool): 
        - IncludeTdmOption (bool): 
        - IncludeTdmPayload (bool): 
        - IpType (number): 
        - LabelMode (str(none | increment)): 
        - LabelStart (number): 
        - MaxNumberOfAtmCells (number): 
        - Mtu (number): 
        - PayloadType (number): 
        - PeerAddress (str): 
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): 
        - PwStatusCode (number): 
        - RepeatCount (number): 
        - SendPwStatus (bool): 
        - SourceAiiAsIp (str): 
        - SourceAiiAsNumber (number): 
        - SourceAiiType (str(number | ipAddress)): 
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): 
        - Ssrc (number): 
        - Step (number): 
        - TargetAiiAsIp (str): 
        - TargetAiiAsNumber (number): 
        - TargetAiiType (str(number | ipAddress)): 
        - TdmBitrate (number): 
        - TdmDataSize (number): 
        - TimestampMode (str(absolute | differential)): 
        - UpInterval (number): 
        - VcId (number): 
        - VcIdStep (number): 
        - VplsIdAsNumber (number): 
        - VplsIdAsNumberStep (number): 
        - VplsIdAssignedNumber (number): 
        - VplsIdAssignedNumberStep (number): 
        - VplsIdCount (number): 
        - VplsIdIpAddress (str): 
        - VplsIdIpAddressStep (str): 
        - VplsIdType (str(asNumber | ipAddress)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Adds a new l2VcRange resource on the server and adds it to the container.

        Args
        ----
        - CapableOfReassembly (bool): 
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): 
        - CeIpAddress (str): 
        - CemOption (number): 
        - CemPayload (number): 
        - Count (number): 
        - Description (str): 
        - DoNotExpandIntoVcs (bool): 
        - DownInterval (number): 
        - DownStartInterval (number): 
        - EnableBfdIpUdpCv (bool): 
        - EnableBfdPwAchCv (bool): 
        - EnableCBit (bool): 
        - EnableCccvNegotiation (bool): 
        - EnableCemOption (bool): 
        - EnableCemPayload (bool): 
        - EnableDescriptionPresent (bool): 
        - EnableLspPingCv (bool): 
        - EnableMaxAtmPresent (bool): 
        - EnableMtuPresent (bool): 
        - EnablePacking (bool): 
        - EnablePwAchCc (bool): 
        - EnablePwStatusTlv (bool): 
        - EnableRouterAlertCc (bool): 
        - Enabled (bool): 
        - FecType (str(pwIdFec | generalizedIdFecVpls)): 
        - Frequency (number): 
        - IncludeRtpHeader (bool): 
        - IncludeSsrc (bool): 
        - IncludeTdmBitrate (bool): 
        - IncludeTdmOption (bool): 
        - IncludeTdmPayload (bool): 
        - IpType (number): 
        - LabelMode (str(none | increment)): 
        - LabelStart (number): 
        - MaxNumberOfAtmCells (number): 
        - Mtu (number): 
        - PayloadType (number): 
        - PeerAddress (str): 
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): 
        - PwStatusCode (number): 
        - RepeatCount (number): 
        - SendPwStatus (bool): 
        - SourceAiiAsIp (str): 
        - SourceAiiAsNumber (number): 
        - SourceAiiType (str(number | ipAddress)): 
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): 
        - Ssrc (number): 
        - Step (number): 
        - TargetAiiAsIp (str): 
        - TargetAiiAsNumber (number): 
        - TargetAiiType (str(number | ipAddress)): 
        - TdmBitrate (number): 
        - TdmDataSize (number): 
        - TimestampMode (str(absolute | differential)): 
        - UpInterval (number): 
        - VcId (number): 
        - VcIdStep (number): 
        - VplsIdAsNumber (number): 
        - VplsIdAsNumberStep (number): 
        - VplsIdAssignedNumber (number): 
        - VplsIdAssignedNumberStep (number): 
        - VplsIdCount (number): 
        - VplsIdIpAddress (str): 
        - VplsIdIpAddressStep (str): 
        - VplsIdType (str(asNumber | ipAddress)): 

        Returns
        -------
        - self: This instance with all currently retrieved l2VcRange resources using find and the newly added l2VcRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2VcRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CapableOfReassembly=None, Cas=None, CeIpAddress=None, CemOption=None, CemPayload=None, Count=None, Description=None, DoNotExpandIntoVcs=None, DownInterval=None, DownStartInterval=None, EnableBfdIpUdpCv=None, EnableBfdPwAchCv=None, EnableCBit=None, EnableCccvNegotiation=None, EnableCemOption=None, EnableCemPayload=None, EnableDescriptionPresent=None, EnableLspPingCv=None, EnableMaxAtmPresent=None, EnableMtuPresent=None, EnablePacking=None, EnablePwAchCc=None, EnablePwStatusTlv=None, EnableRouterAlertCc=None, Enabled=None, FecType=None, Frequency=None, IncludeRtpHeader=None, IncludeSsrc=None, IncludeTdmBitrate=None, IncludeTdmOption=None, IncludeTdmPayload=None, IpType=None, LabelMode=None, LabelStart=None, MaxNumberOfAtmCells=None, Mtu=None, PayloadType=None, PeerAddress=None, ProvisioningModel=None, PwStatusCode=None, RepeatCount=None, SendPwStatus=None, SourceAiiAsIp=None, SourceAiiAsNumber=None, SourceAiiType=None, Sp=None, Ssrc=None, Step=None, TargetAiiAsIp=None, TargetAiiAsNumber=None, TargetAiiType=None, TdmBitrate=None, TdmDataSize=None, TimestampMode=None, UpInterval=None, VcId=None, VcIdStep=None, VplsIdAsNumber=None, VplsIdAsNumberStep=None, VplsIdAssignedNumber=None, VplsIdAssignedNumberStep=None, VplsIdCount=None, VplsIdIpAddress=None, VplsIdIpAddressStep=None, VplsIdType=None):
        """Finds and retrieves l2VcRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2VcRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2VcRange resources from the server.

        Args
        ----
        - CapableOfReassembly (bool): 
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): 
        - CeIpAddress (str): 
        - CemOption (number): 
        - CemPayload (number): 
        - Count (number): 
        - Description (str): 
        - DoNotExpandIntoVcs (bool): 
        - DownInterval (number): 
        - DownStartInterval (number): 
        - EnableBfdIpUdpCv (bool): 
        - EnableBfdPwAchCv (bool): 
        - EnableCBit (bool): 
        - EnableCccvNegotiation (bool): 
        - EnableCemOption (bool): 
        - EnableCemPayload (bool): 
        - EnableDescriptionPresent (bool): 
        - EnableLspPingCv (bool): 
        - EnableMaxAtmPresent (bool): 
        - EnableMtuPresent (bool): 
        - EnablePacking (bool): 
        - EnablePwAchCc (bool): 
        - EnablePwStatusTlv (bool): 
        - EnableRouterAlertCc (bool): 
        - Enabled (bool): 
        - FecType (str(pwIdFec | generalizedIdFecVpls)): 
        - Frequency (number): 
        - IncludeRtpHeader (bool): 
        - IncludeSsrc (bool): 
        - IncludeTdmBitrate (bool): 
        - IncludeTdmOption (bool): 
        - IncludeTdmPayload (bool): 
        - IpType (number): 
        - LabelMode (str(none | increment)): 
        - LabelStart (number): 
        - MaxNumberOfAtmCells (number): 
        - Mtu (number): 
        - PayloadType (number): 
        - PeerAddress (str): 
        - ProvisioningModel (str(manualConfiguration | bgpAutoDiscovery)): 
        - PwStatusCode (number): 
        - RepeatCount (number): 
        - SendPwStatus (bool): 
        - SourceAiiAsIp (str): 
        - SourceAiiAsNumber (number): 
        - SourceAiiType (str(number | ipAddress)): 
        - Sp (str(hexVal0 | hexVal1 | hexVal2 | hexVal3)): 
        - Ssrc (number): 
        - Step (number): 
        - TargetAiiAsIp (str): 
        - TargetAiiAsNumber (number): 
        - TargetAiiType (str(number | ipAddress)): 
        - TdmBitrate (number): 
        - TdmDataSize (number): 
        - TimestampMode (str(absolute | differential)): 
        - UpInterval (number): 
        - VcId (number): 
        - VcIdStep (number): 
        - VplsIdAsNumber (number): 
        - VplsIdAsNumberStep (number): 
        - VplsIdAssignedNumber (number): 
        - VplsIdAssignedNumberStep (number): 
        - VplsIdCount (number): 
        - VplsIdIpAddress (str): 
        - VplsIdIpAddressStep (str): 
        - VplsIdType (str(asNumber | ipAddress)): 

        Returns
        -------
        - self: This instance with matching l2VcRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2VcRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2VcRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
