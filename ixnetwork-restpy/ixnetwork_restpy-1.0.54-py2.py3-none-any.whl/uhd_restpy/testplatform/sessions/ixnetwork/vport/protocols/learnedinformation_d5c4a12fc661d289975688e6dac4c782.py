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


class LearnedInformation(Base):
    """
    The LearnedInformation class encapsulates a list of learnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'
    _SDM_ATT_MAP = {
        'DestinationAddressIpv4': 'destinationAddressIpv4',
        'DownstreamAddressType': 'downstreamAddressType',
        'DownstreamInterfaceAddress': 'downstreamInterfaceAddress',
        'DownstreamIpAddress': 'downstreamIpAddress',
        'EchoResponseTimeoutMs': 'echoResponseTimeoutMs',
        'EnableAdvance': 'enableAdvance',
        'EnableDsiFlag': 'enableDsiFlag',
        'EnableDsnFlag': 'enableDsnFlag',
        'EnableFecValidation': 'enableFecValidation',
        'EnableIncludeDownstreamMappingTlv': 'enableIncludeDownstreamMappingTlv',
        'EnableIncludePadTlv': 'enableIncludePadTlv',
        'EnableIncludeVendorEnterpriseNumberTlv': 'enableIncludeVendorEnterpriseNumberTlv',
        'EnablePauseResumeBfdPduTrigger': 'enablePauseResumeBfdPduTrigger',
        'EnablePauseResumeReplyTrigger': 'enablePauseResumeReplyTrigger',
        'EnableSendTriggeredPing': 'enableSendTriggeredPing',
        'EnableSendTriggeredTraceroute': 'enableSendTriggeredTraceroute',
        'EnableSetResetEchoReplyCodeTrigger': 'enableSetResetEchoReplyCodeTrigger',
        'IsGeneralLearnedInformationRefreshed': 'isGeneralLearnedInformationRefreshed',
        'IsTriggeredPingLearnedInformationRefreshed': 'isTriggeredPingLearnedInformationRefreshed',
        'IsTriggeredTraceRouteLearnedInformationRefreshed': 'isTriggeredTraceRouteLearnedInformationRefreshed',
        'PadTlvFirstOctetOptions': 'padTlvFirstOctetOptions',
        'PadTlvLength': 'padTlvLength',
        'PauseResumeBfdPduTriggerOption': 'pauseResumeBfdPduTriggerOption',
        'PauseResumeReplyTriggerOption': 'pauseResumeReplyTriggerOption',
        'ReplyMode': 'replyMode',
        'ReturnCodeOption': 'returnCodeOption',
        'ReturnSubCode': 'returnSubCode',
        'TriggerOptions': 'triggerOptions',
        'TriggerType': 'triggerType',
        'TtlLimit': 'ttlLimit',
        'VendorEnterpriseNumber': 'vendorEnterpriseNumber',
    }

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def GeneralLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_8010b2dfe921ba6310a049b8b025a8ba.GeneralLearnedInfo): An instance of the GeneralLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_8010b2dfe921ba6310a049b8b025a8ba import GeneralLearnedInfo
        return GeneralLearnedInfo(self)

    @property
    def TriggeredPingLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_de0ed0012c4c1038986dd586f5dd63fc.TriggeredPingLearnedInfo): An instance of the TriggeredPingLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_de0ed0012c4c1038986dd586f5dd63fc import TriggeredPingLearnedInfo
        return TriggeredPingLearnedInfo(self)

    @property
    def TriggeredTracerouteLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_60610bdf03c18bf6050144c753fe5797.TriggeredTracerouteLearnedInfo): An instance of the TriggeredTracerouteLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_60610bdf03c18bf6050144c753fe5797 import TriggeredTracerouteLearnedInfo
        return TriggeredTracerouteLearnedInfo(self)

    @property
    def DestinationAddressIpv4(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationAddressIpv4'])
    @DestinationAddressIpv4.setter
    def DestinationAddressIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationAddressIpv4'], value)

    @property
    def DownstreamAddressType(self):
        """
        Returns
        -------
        - str(ipv4Numbered | ipv4UnNumbered): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamAddressType'])
    @DownstreamAddressType.setter
    def DownstreamAddressType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamAddressType'], value)

    @property
    def DownstreamInterfaceAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamInterfaceAddress'])
    @DownstreamInterfaceAddress.setter
    def DownstreamInterfaceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamInterfaceAddress'], value)

    @property
    def DownstreamIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamIpAddress'])
    @DownstreamIpAddress.setter
    def DownstreamIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamIpAddress'], value)

    @property
    def EchoResponseTimeoutMs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoResponseTimeoutMs'])
    @EchoResponseTimeoutMs.setter
    def EchoResponseTimeoutMs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoResponseTimeoutMs'], value)

    @property
    def EnableAdvance(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvance'])
    @EnableAdvance.setter
    def EnableAdvance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvance'], value)

    @property
    def EnableDsiFlag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDsiFlag'])
    @EnableDsiFlag.setter
    def EnableDsiFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDsiFlag'], value)

    @property
    def EnableDsnFlag(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDsnFlag'])
    @EnableDsnFlag.setter
    def EnableDsnFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDsnFlag'], value)

    @property
    def EnableFecValidation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFecValidation'])
    @EnableFecValidation.setter
    def EnableFecValidation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFecValidation'], value)

    @property
    def EnableIncludeDownstreamMappingTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeDownstreamMappingTlv'])
    @EnableIncludeDownstreamMappingTlv.setter
    def EnableIncludeDownstreamMappingTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeDownstreamMappingTlv'], value)

    @property
    def EnableIncludePadTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludePadTlv'])
    @EnableIncludePadTlv.setter
    def EnableIncludePadTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludePadTlv'], value)

    @property
    def EnableIncludeVendorEnterpriseNumberTlv(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeVendorEnterpriseNumberTlv'])
    @EnableIncludeVendorEnterpriseNumberTlv.setter
    def EnableIncludeVendorEnterpriseNumberTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeVendorEnterpriseNumberTlv'], value)

    @property
    def EnablePauseResumeBfdPduTrigger(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePauseResumeBfdPduTrigger'])
    @EnablePauseResumeBfdPduTrigger.setter
    def EnablePauseResumeBfdPduTrigger(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePauseResumeBfdPduTrigger'], value)

    @property
    def EnablePauseResumeReplyTrigger(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePauseResumeReplyTrigger'])
    @EnablePauseResumeReplyTrigger.setter
    def EnablePauseResumeReplyTrigger(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePauseResumeReplyTrigger'], value)

    @property
    def EnableSendTriggeredPing(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPing'])
    @EnableSendTriggeredPing.setter
    def EnableSendTriggeredPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPing'], value)

    @property
    def EnableSendTriggeredTraceroute(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredTraceroute'])
    @EnableSendTriggeredTraceroute.setter
    def EnableSendTriggeredTraceroute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredTraceroute'], value)

    @property
    def EnableSetResetEchoReplyCodeTrigger(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSetResetEchoReplyCodeTrigger'])
    @EnableSetResetEchoReplyCodeTrigger.setter
    def EnableSetResetEchoReplyCodeTrigger(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSetResetEchoReplyCodeTrigger'], value)

    @property
    def IsGeneralLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsGeneralLearnedInformationRefreshed'])

    @property
    def IsTriggeredPingLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsTriggeredPingLearnedInformationRefreshed'])

    @property
    def IsTriggeredTraceRouteLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsTriggeredTraceRouteLearnedInformationRefreshed'])

    @property
    def PadTlvFirstOctetOptions(self):
        """
        Returns
        -------
        - str(dropPadTlvFromReply | copyPadTlvToReply): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PadTlvFirstOctetOptions'])
    @PadTlvFirstOctetOptions.setter
    def PadTlvFirstOctetOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PadTlvFirstOctetOptions'], value)

    @property
    def PadTlvLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PadTlvLength'])
    @PadTlvLength.setter
    def PadTlvLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PadTlvLength'], value)

    @property
    def PauseResumeBfdPduTriggerOption(self):
        """
        Returns
        -------
        - str(pause | resume): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PauseResumeBfdPduTriggerOption'])
    @PauseResumeBfdPduTriggerOption.setter
    def PauseResumeBfdPduTriggerOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PauseResumeBfdPduTriggerOption'], value)

    @property
    def PauseResumeReplyTriggerOption(self):
        """
        Returns
        -------
        - str(pause | resume): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PauseResumeReplyTriggerOption'])
    @PauseResumeReplyTriggerOption.setter
    def PauseResumeReplyTriggerOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PauseResumeReplyTriggerOption'], value)

    @property
    def ReplyMode(self):
        """
        Returns
        -------
        - str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyMode'])
    @ReplyMode.setter
    def ReplyMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplyMode'], value)

    @property
    def ReturnCodeOption(self):
        """
        Returns
        -------
        - str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnCodeOption'])
    @ReturnCodeOption.setter
    def ReturnCodeOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReturnCodeOption'], value)

    @property
    def ReturnSubCode(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReturnSubCode'])
    @ReturnSubCode.setter
    def ReturnSubCode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReturnSubCode'], value)

    @property
    def TriggerOptions(self):
        """
        Returns
        -------
        - str(tx | rx | txRx): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerOptions'])
    @TriggerOptions.setter
    def TriggerOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerOptions'], value)

    @property
    def TriggerType(self):
        """
        Returns
        -------
        - str(resetToNormalReply | forceReplyCode): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggerType'])
    @TriggerType.setter
    def TriggerType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggerType'], value)

    @property
    def TtlLimit(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TtlLimit'])
    @TtlLimit.setter
    def TtlLimit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TtlLimit'], value)

    @property
    def VendorEnterpriseNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorEnterpriseNumber'])
    @VendorEnterpriseNumber.setter
    def VendorEnterpriseNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorEnterpriseNumber'], value)

    def update(self, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddress=None, DownstreamIpAddress=None, EchoResponseTimeoutMs=None, EnableAdvance=None, EnableDsiFlag=None, EnableDsnFlag=None, EnableFecValidation=None, EnableIncludeDownstreamMappingTlv=None, EnableIncludePadTlv=None, EnableIncludeVendorEnterpriseNumberTlv=None, EnablePauseResumeBfdPduTrigger=None, EnablePauseResumeReplyTrigger=None, EnableSendTriggeredPing=None, EnableSendTriggeredTraceroute=None, EnableSetResetEchoReplyCodeTrigger=None, PadTlvFirstOctetOptions=None, PadTlvLength=None, PauseResumeBfdPduTriggerOption=None, PauseResumeReplyTriggerOption=None, ReplyMode=None, ReturnCodeOption=None, ReturnSubCode=None, TriggerOptions=None, TriggerType=None, TtlLimit=None, VendorEnterpriseNumber=None):
        """Updates learnedInformation resource on the server.

        Args
        ----
        - DestinationAddressIpv4 (str): 
        - DownstreamAddressType (str(ipv4Numbered | ipv4UnNumbered)): 
        - DownstreamInterfaceAddress (str): 
        - DownstreamIpAddress (str): 
        - EchoResponseTimeoutMs (number): 
        - EnableAdvance (bool): 
        - EnableDsiFlag (bool): 
        - EnableDsnFlag (bool): 
        - EnableFecValidation (bool): 
        - EnableIncludeDownstreamMappingTlv (bool): 
        - EnableIncludePadTlv (bool): 
        - EnableIncludeVendorEnterpriseNumberTlv (bool): 
        - EnablePauseResumeBfdPduTrigger (bool): 
        - EnablePauseResumeReplyTrigger (bool): 
        - EnableSendTriggeredPing (bool): 
        - EnableSendTriggeredTraceroute (bool): 
        - EnableSetResetEchoReplyCodeTrigger (bool): 
        - PadTlvFirstOctetOptions (str(dropPadTlvFromReply | copyPadTlvToReply)): 
        - PadTlvLength (number): 
        - PauseResumeBfdPduTriggerOption (str(pause | resume)): 
        - PauseResumeReplyTriggerOption (str(pause | resume)): 
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): 
        - ReturnCodeOption (str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): 
        - ReturnSubCode (number): 
        - TriggerOptions (str(tx | rx | txRx)): 
        - TriggerType (str(resetToNormalReply | forceReplyCode)): 
        - TtlLimit (number): 
        - VendorEnterpriseNumber (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddress=None, DownstreamIpAddress=None, EchoResponseTimeoutMs=None, EnableAdvance=None, EnableDsiFlag=None, EnableDsnFlag=None, EnableFecValidation=None, EnableIncludeDownstreamMappingTlv=None, EnableIncludePadTlv=None, EnableIncludeVendorEnterpriseNumberTlv=None, EnablePauseResumeBfdPduTrigger=None, EnablePauseResumeReplyTrigger=None, EnableSendTriggeredPing=None, EnableSendTriggeredTraceroute=None, EnableSetResetEchoReplyCodeTrigger=None, IsGeneralLearnedInformationRefreshed=None, IsTriggeredPingLearnedInformationRefreshed=None, IsTriggeredTraceRouteLearnedInformationRefreshed=None, PadTlvFirstOctetOptions=None, PadTlvLength=None, PauseResumeBfdPduTriggerOption=None, PauseResumeReplyTriggerOption=None, ReplyMode=None, ReturnCodeOption=None, ReturnSubCode=None, TriggerOptions=None, TriggerType=None, TtlLimit=None, VendorEnterpriseNumber=None):
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Args
        ----
        - DestinationAddressIpv4 (str): 
        - DownstreamAddressType (str(ipv4Numbered | ipv4UnNumbered)): 
        - DownstreamInterfaceAddress (str): 
        - DownstreamIpAddress (str): 
        - EchoResponseTimeoutMs (number): 
        - EnableAdvance (bool): 
        - EnableDsiFlag (bool): 
        - EnableDsnFlag (bool): 
        - EnableFecValidation (bool): 
        - EnableIncludeDownstreamMappingTlv (bool): 
        - EnableIncludePadTlv (bool): 
        - EnableIncludeVendorEnterpriseNumberTlv (bool): 
        - EnablePauseResumeBfdPduTrigger (bool): 
        - EnablePauseResumeReplyTrigger (bool): 
        - EnableSendTriggeredPing (bool): 
        - EnableSendTriggeredTraceroute (bool): 
        - EnableSetResetEchoReplyCodeTrigger (bool): 
        - IsGeneralLearnedInformationRefreshed (bool): 
        - IsTriggeredPingLearnedInformationRefreshed (bool): 
        - IsTriggeredTraceRouteLearnedInformationRefreshed (bool): 
        - PadTlvFirstOctetOptions (str(dropPadTlvFromReply | copyPadTlvToReply)): 
        - PadTlvLength (number): 
        - PauseResumeBfdPduTriggerOption (str(pause | resume)): 
        - PauseResumeReplyTriggerOption (str(pause | resume)): 
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): 
        - ReturnCodeOption (str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): 
        - ReturnSubCode (number): 
        - TriggerOptions (str(tx | rx | txRx)): 
        - TriggerType (str(resetToNormalReply | forceReplyCode)): 
        - TtlLimit (number): 
        - VendorEnterpriseNumber (number): 

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearRecordsForTrigger(self):
        """Executes the clearRecordsForTrigger operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('clearRecordsForTrigger', payload=payload, response_object=None)

    def RefreshLearnedInformation(self):
        """Executes the refreshLearnedInformation operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInformation', payload=payload, response_object=None)

    def Trigger(self):
        """Executes the trigger operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('trigger', payload=payload, response_object=None)
