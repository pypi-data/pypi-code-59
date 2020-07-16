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
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'
    _SDM_ATT_MAP = {
        'AsyncConfStatResponseTimeOut': 'asyncConfStatResponseTimeOut',
        'DescriptionStatResponseTimeOut': 'descriptionStatResponseTimeOut',
        'EnableAsyncConfMasterFlowRemovedFlowDelete': 'enableAsyncConfMasterFlowRemovedFlowDelete',
        'EnableAsyncConfMasterFlowRemovedGroupDelete': 'enableAsyncConfMasterFlowRemovedGroupDelete',
        'EnableAsyncConfMasterFlowRemovedHardTimeOut': 'enableAsyncConfMasterFlowRemovedHardTimeOut',
        'EnableAsyncConfMasterFlowRemovedIdleTimeOut': 'enableAsyncConfMasterFlowRemovedIdleTimeOut',
        'EnableAsyncConfMasterPacketInActionOutputToController': 'enableAsyncConfMasterPacketInActionOutputToController',
        'EnableAsyncConfMasterPacketInInvalidTtl': 'enableAsyncConfMasterPacketInInvalidTtl',
        'EnableAsyncConfMasterPacketInNoMatching': 'enableAsyncConfMasterPacketInNoMatching',
        'EnableAsyncConfMasterPortStatusAdd': 'enableAsyncConfMasterPortStatusAdd',
        'EnableAsyncConfMasterPortStatusDelete': 'enableAsyncConfMasterPortStatusDelete',
        'EnableAsyncConfMasterPortStatusModify': 'enableAsyncConfMasterPortStatusModify',
        'EnableAsyncConfSlaveFlowRemovedFlowDelete': 'enableAsyncConfSlaveFlowRemovedFlowDelete',
        'EnableAsyncConfSlaveFlowRemovedGroupDelete': 'enableAsyncConfSlaveFlowRemovedGroupDelete',
        'EnableAsyncConfSlaveFlowRemovedHardTimeOut': 'enableAsyncConfSlaveFlowRemovedHardTimeOut',
        'EnableAsyncConfSlaveFlowRemovedIdleTimeOut': 'enableAsyncConfSlaveFlowRemovedIdleTimeOut',
        'EnableAsyncConfSlavePacketInActionOutputToController': 'enableAsyncConfSlavePacketInActionOutputToController',
        'EnableAsyncConfSlavePacketInInvalidTtl': 'enableAsyncConfSlavePacketInInvalidTtl',
        'EnableAsyncConfSlavePacketInNoMatching': 'enableAsyncConfSlavePacketInNoMatching',
        'EnableAsyncConfSlavePortStatusAdd': 'enableAsyncConfSlavePortStatusAdd',
        'EnableAsyncConfSlavePortStatusDelete': 'enableAsyncConfSlavePortStatusDelete',
        'EnableAsyncConfSlavePortStatusModify': 'enableAsyncConfSlavePortStatusModify',
        'EnableFlowAggregatedStatMatchCapability': 'enableFlowAggregatedStatMatchCapability',
        'EnableFlowStatMatchCapability': 'enableFlowStatMatchCapability',
        'EnableGroupStatMatchCapability': 'enableGroupStatMatchCapability',
        'EnablePortStatMatchCapability': 'enablePortStatMatchCapability',
        'EnableQueueStatMatchCapability': 'enableQueueStatMatchCapability',
        'EnableSendTableFeaturesTrigger': 'enableSendTableFeaturesTrigger',
        'EnableSendTriggerPortFeaturesLearnedInformation': 'enableSendTriggerPortFeaturesLearnedInformation',
        'EnableSendTriggeredAsyncConfStatLearnedInformation': 'enableSendTriggeredAsyncConfStatLearnedInformation',
        'EnableSendTriggeredBarrierRequestMessage': 'enableSendTriggeredBarrierRequestMessage',
        'EnableSendTriggeredDescriptionStatLearnedInformation': 'enableSendTriggeredDescriptionStatLearnedInformation',
        'EnableSendTriggeredFlowAggregatedStatLearnedInformation': 'enableSendTriggeredFlowAggregatedStatLearnedInformation',
        'EnableSendTriggeredFlowStatLearnedInformation': 'enableSendTriggeredFlowStatLearnedInformation',
        'EnableSendTriggeredGroupDescriptionStatLearnedInformation': 'enableSendTriggeredGroupDescriptionStatLearnedInformation',
        'EnableSendTriggeredGroupFeatureStatLearnedInformation': 'enableSendTriggeredGroupFeatureStatLearnedInformation',
        'EnableSendTriggeredGroupStatLearnedInformation': 'enableSendTriggeredGroupStatLearnedInformation',
        'EnableSendTriggeredPacketOutMessage': 'enableSendTriggeredPacketOutMessage',
        'EnableSendTriggeredPortModificationMessage': 'enableSendTriggeredPortModificationMessage',
        'EnableSendTriggeredPortStatLearnedInformation': 'enableSendTriggeredPortStatLearnedInformation',
        'EnableSendTriggeredQueueConfigLearnedInformation': 'enableSendTriggeredQueueConfigLearnedInformation',
        'EnableSendTriggeredQueueStatLearnedInformation': 'enableSendTriggeredQueueStatLearnedInformation',
        'EnableSendTriggeredRoleRequestMessage': 'enableSendTriggeredRoleRequestMessage',
        'EnableSendTriggeredSwitchConfigLearnedInformation': 'enableSendTriggeredSwitchConfigLearnedInformation',
        'EnableSendTriggeredTableStatLearnedInformation': 'enableSendTriggeredTableStatLearnedInformation',
        'EnableSendTriggeredVendorStatLearnedInformation': 'enableSendTriggeredVendorStatLearnedInformation',
        'EnableSetAsyncConfig': 'enableSetAsyncConfig',
        'EnableSetSwitchConfig': 'enableSetSwitchConfig',
        'EnableSetTableFeatures': 'enableSetTableFeatures',
        'EnableTableStatMatchCapability': 'enableTableStatMatchCapability',
        'EnableTriggeredVendorMessage': 'enableTriggeredVendorMessage',
        'FlowAggregatedStatEthernetDestination': 'flowAggregatedStatEthernetDestination',
        'FlowAggregatedStatEthernetSource': 'flowAggregatedStatEthernetSource',
        'FlowAggregatedStatEthernetType': 'flowAggregatedStatEthernetType',
        'FlowAggregatedStatInPort': 'flowAggregatedStatInPort',
        'FlowAggregatedStatIpDscp': 'flowAggregatedStatIpDscp',
        'FlowAggregatedStatIpProtocol': 'flowAggregatedStatIpProtocol',
        'FlowAggregatedStatIpv4Destination': 'flowAggregatedStatIpv4Destination',
        'FlowAggregatedStatIpv4Source': 'flowAggregatedStatIpv4Source',
        'FlowAggregatedStatOutPortInputMode': 'flowAggregatedStatOutPortInputMode',
        'FlowAggregatedStatResponseTimeOut': 'flowAggregatedStatResponseTimeOut',
        'FlowAggregatedStatTableIdInputMode': 'flowAggregatedStatTableIdInputMode',
        'FlowAggregatedStatTableIdInputModeNumber': 'flowAggregatedStatTableIdInputModeNumber',
        'FlowAggregatedStatTransportDestination': 'flowAggregatedStatTransportDestination',
        'FlowAggregatedStatTransportSource': 'flowAggregatedStatTransportSource',
        'FlowAggregatedStatVlanId': 'flowAggregatedStatVlanId',
        'FlowAggregatedStatVlanPriority': 'flowAggregatedStatVlanPriority',
        'FlowStatEthernetDestination': 'flowStatEthernetDestination',
        'FlowStatEthernetSource': 'flowStatEthernetSource',
        'FlowStatEthernetType': 'flowStatEthernetType',
        'FlowStatInPort': 'flowStatInPort',
        'FlowStatIpDscp': 'flowStatIpDscp',
        'FlowStatIpProtocol': 'flowStatIpProtocol',
        'FlowStatIpv4Destination': 'flowStatIpv4Destination',
        'FlowStatIpv4Source': 'flowStatIpv4Source',
        'FlowStatOutPortInputMode': 'flowStatOutPortInputMode',
        'FlowStatResponseTimeOut': 'flowStatResponseTimeOut',
        'FlowStatTableIdInputMode': 'flowStatTableIdInputMode',
        'FlowStatTableIdInputModeNumber': 'flowStatTableIdInputModeNumber',
        'FlowStatTransportDestination': 'flowStatTransportDestination',
        'FlowStatTransportSource': 'flowStatTransportSource',
        'FlowStatVlanId': 'flowStatVlanId',
        'FlowStatVlanPriority': 'flowStatVlanPriority',
        'GroupDescriptionStatResponseTimeOut': 'groupDescriptionStatResponseTimeOut',
        'GroupFeatureStatResponseTimeOut': 'groupFeatureStatResponseTimeOut',
        'GroupId': 'groupId',
        'GroupIdType': 'groupIdType',
        'GroupStatResponseTimeOut': 'groupStatResponseTimeOut',
        'IsAsyncConfStatLearnedInformationRefreshed': 'isAsyncConfStatLearnedInformationRefreshed',
        'IsDescriptionStatLearnedInformationRefreshed': 'isDescriptionStatLearnedInformationRefreshed',
        'IsFlowAggregatedStatLearnedInformationRefreshed': 'isFlowAggregatedStatLearnedInformationRefreshed',
        'IsFlowStatLearnedInformationRefreshed': 'isFlowStatLearnedInformationRefreshed',
        'IsGroupDescriptionStatLearnedInformationRefreshed': 'isGroupDescriptionStatLearnedInformationRefreshed',
        'IsGroupFeatureStatLearnedInformationRefreshed': 'isGroupFeatureStatLearnedInformationRefreshed',
        'IsGroupStatLearnedInformationRefreshed': 'isGroupStatLearnedInformationRefreshed',
        'IsOfChannelLearnedInformationRefreshed': 'isOfChannelLearnedInformationRefreshed',
        'IsPortFeaturesLearnedInformationRefreshed': 'isPortFeaturesLearnedInformationRefreshed',
        'IsPortStatLearnedInformationRefreshed': 'isPortStatLearnedInformationRefreshed',
        'IsQueueConfigLearnedInformationRefreshed': 'isQueueConfigLearnedInformationRefreshed',
        'IsQueueStatLearnedInformationRefreshed': 'isQueueStatLearnedInformationRefreshed',
        'IsTableStatLearnedInformationRefreshed': 'isTableStatLearnedInformationRefreshed',
        'IsVendorStatLearnedInformationRefreshed': 'isVendorStatLearnedInformationRefreshed',
        'PacketOutAuxiliaryId': 'packetOutAuxiliaryId',
        'PacketOutBufferId': 'packetOutBufferId',
        'PacketOutBufferIdInputMode': 'packetOutBufferIdInputMode',
        'PacketOutData': 'packetOutData',
        'PacketOutDataLength': 'packetOutDataLength',
        'PacketOutInPortInputMode': 'packetOutInPortInputMode',
        'PacketOutInPortNumber': 'packetOutInPortNumber',
        'PortFeaturesResponseTimeOut': 'portFeaturesResponseTimeOut',
        'PortNumber': 'portNumber',
        'PortNumberInputMode': 'portNumberInputMode',
        'PortStatResponseTimeOut': 'portStatResponseTimeOut',
        'QueueConfigPortNumber': 'queueConfigPortNumber',
        'QueueConfigResponseTimeOut': 'queueConfigResponseTimeOut',
        'QueueId': 'queueId',
        'QueueIdInputMode': 'queueIdInputMode',
        'QueueStatPortNumber': 'queueStatPortNumber',
        'QueueStatPortNumberInputMode': 'queueStatPortNumberInputMode',
        'QueueStatResponseTimeOut': 'queueStatResponseTimeOut',
        'RoleRequestGenerationId': 'roleRequestGenerationId',
        'RoleRequestType': 'roleRequestType',
        'SwitchConfigDropFragments': 'switchConfigDropFragments',
        'SwitchConfigMissSendLength': 'switchConfigMissSendLength',
        'SwitchConfigReassembleFragments': 'switchConfigReassembleFragments',
        'SwitchConfigResponseTimeOut': 'switchConfigResponseTimeOut',
        'TableFeatureConfig': 'tableFeatureConfig',
        'TableFeatureMaxEntries': 'tableFeatureMaxEntries',
        'TableFeatureMetadataMatch': 'tableFeatureMetadataMatch',
        'TableFeatureMetadataWrite': 'tableFeatureMetadataWrite',
        'TableFeatureName': 'tableFeatureName',
        'TableFeatureResponseTimeOut': 'tableFeatureResponseTimeOut',
        'TableFeatureTableId': 'tableFeatureTableId',
        'TableStatResponseTimeOut': 'tableStatResponseTimeOut',
        'TriggeredVendorMessage': 'triggeredVendorMessage',
        'TriggeredVendorMessageId': 'triggeredVendorMessageId',
        'TriggeredVendorMessageLength': 'triggeredVendorMessageLength',
        'VendorId': 'vendorId',
        'VendorMessage': 'vendorMessage',
        'VendorMessageLength': 'vendorMessageLength',
        'VendorStateResponseTimeOut': 'vendorStateResponseTimeOut',
    }

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def AsyncConfStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_55a6bd209526972244efc9f3d4661ec1.AsyncConfStatLearnedInformation): An instance of the AsyncConfStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_55a6bd209526972244efc9f3d4661ec1 import AsyncConfStatLearnedInformation
        return AsyncConfStatLearnedInformation(self)

    @property
    def Controller131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_232ca5028d5ea1215ace5aeba2962aea.Controller131TriggerAttributes): An instance of the Controller131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_232ca5028d5ea1215ace5aeba2962aea import Controller131TriggerAttributes
        return Controller131TriggerAttributes(self)._select()

    @property
    def DescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_1cfc66b0b9bce6c9662a87e26565e532.DescriptionStatLearnedInformation): An instance of the DescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_1cfc66b0b9bce6c9662a87e26565e532 import DescriptionStatLearnedInformation
        return DescriptionStatLearnedInformation(self)

    @property
    def FlowAggregatedStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_4c7ab774f7d7c4e18b23b05a43dc0027.FlowAggregatedStatLearnedInformation): An instance of the FlowAggregatedStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_4c7ab774f7d7c4e18b23b05a43dc0027 import FlowAggregatedStatLearnedInformation
        return FlowAggregatedStatLearnedInformation(self)

    @property
    def FlowAggregatedStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_8ac885c07bf1d6cf7c59365972b356be.FlowAggregatedStatMatchCriteria131TriggerAttributes): An instance of the FlowAggregatedStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_8ac885c07bf1d6cf7c59365972b356be import FlowAggregatedStatMatchCriteria131TriggerAttributes
        return FlowAggregatedStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def FlowStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_002eabd5fa0889c68e7235a9bb9ad5e9.FlowStatLearnedInformation): An instance of the FlowStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_002eabd5fa0889c68e7235a9bb9ad5e9 import FlowStatLearnedInformation
        return FlowStatLearnedInformation(self)

    @property
    def FlowStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_b27e5ddde40e31d2de302bf536951c5d.FlowStatMatchCriteria131TriggerAttributes): An instance of the FlowStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_b27e5ddde40e31d2de302bf536951c5d import FlowStatMatchCriteria131TriggerAttributes
        return FlowStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def GroupDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_bb5c295d0dd2098afdc53add531f47ac.GroupDescriptionStatLearnedInformation): An instance of the GroupDescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_bb5c295d0dd2098afdc53add531f47ac import GroupDescriptionStatLearnedInformation
        return GroupDescriptionStatLearnedInformation(self)

    @property
    def GroupFeatureStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_632280eccf78483b8e26aff2c0535531.GroupFeatureStatLearnedInformation): An instance of the GroupFeatureStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_632280eccf78483b8e26aff2c0535531 import GroupFeatureStatLearnedInformation
        return GroupFeatureStatLearnedInformation(self)

    @property
    def GroupStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_f7fdb75ad6f8b605208c6756821bc8dd.GroupStatLearnedInformation): An instance of the GroupStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_f7fdb75ad6f8b605208c6756821bc8dd import GroupStatLearnedInformation
        return GroupStatLearnedInformation(self)

    @property
    def MeterConfigStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_c404f0f7aa6709be1e0bc4e360c26a77.MeterConfigStatsLearnedInformation): An instance of the MeterConfigStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_c404f0f7aa6709be1e0bc4e360c26a77 import MeterConfigStatsLearnedInformation
        return MeterConfigStatsLearnedInformation(self)

    @property
    def MeterFeatureStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_1c74658b5cfaf7cf07e18ab8b210037a.MeterFeatureStatsLearnedInformation): An instance of the MeterFeatureStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_1c74658b5cfaf7cf07e18ab8b210037a import MeterFeatureStatsLearnedInformation
        return MeterFeatureStatsLearnedInformation(self)

    @property
    def MeterStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_4c77d8d9d16967a4ae392a348abd22b4.MeterStatsLearnedInformation): An instance of the MeterStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_4c77d8d9d16967a4ae392a348abd22b4 import MeterStatsLearnedInformation
        return MeterStatsLearnedInformation(self)

    @property
    def OfChannelLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_a03889c4dddf5a4a960b59e5877e27e7.OfChannelLearnedInformation): An instance of the OfChannelLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_a03889c4dddf5a4a960b59e5877e27e7 import OfChannelLearnedInformation
        return OfChannelLearnedInformation(self)

    @property
    def PacketOutTriggerActions(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_7bb1bdd5560775fd276ee2edb4edc6bd.PacketOutTriggerActions): An instance of the PacketOutTriggerActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_7bb1bdd5560775fd276ee2edb4edc6bd import PacketOutTriggerActions
        return PacketOutTriggerActions(self)

    @property
    def PortFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_0889eed53126145fbd585737900ec1c3.PortFeaturesLearnedInformation): An instance of the PortFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_0889eed53126145fbd585737900ec1c3 import PortFeaturesLearnedInformation
        return PortFeaturesLearnedInformation(self)

    @property
    def PortModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_015954c805480d254b896509d1f9cf19.PortModificationTriggerAttributes): An instance of the PortModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_015954c805480d254b896509d1f9cf19 import PortModificationTriggerAttributes
        return PortModificationTriggerAttributes(self)._select()

    @property
    def PortStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_df08cb6d6559c441ecb18e842c4373c9.PortStatLearnedInformation): An instance of the PortStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_df08cb6d6559c441ecb18e842c4373c9 import PortStatLearnedInformation
        return PortStatLearnedInformation(self)

    @property
    def QueueConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_7ee9e47cec80aa1c9cd1b2b3de6ccb5c.QueueConfigLearnedInformation): An instance of the QueueConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_7ee9e47cec80aa1c9cd1b2b3de6ccb5c import QueueConfigLearnedInformation
        return QueueConfigLearnedInformation(self)

    @property
    def QueueStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_153b6f38157622bbfcd373d2e0ef5a3b.QueueStatLearnedInformation): An instance of the QueueStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_153b6f38157622bbfcd373d2e0ef5a3b import QueueStatLearnedInformation
        return QueueStatLearnedInformation(self)

    @property
    def SwitchConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_e983ca5da0eadbba93d1ce1d2903a5b7.SwitchConfigLearnedInformation): An instance of the SwitchConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_e983ca5da0eadbba93d1ce1d2903a5b7 import SwitchConfigLearnedInformation
        return SwitchConfigLearnedInformation(self)

    @property
    def TableFeaturePropertiesTrigger(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_06c9316866ce5e30145a1ef9dd4c0ab3.TableFeaturePropertiesTrigger): An instance of the TableFeaturePropertiesTrigger class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_06c9316866ce5e30145a1ef9dd4c0ab3 import TableFeaturePropertiesTrigger
        return TableFeaturePropertiesTrigger(self)

    @property
    def TableFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_d8111e2d2a95a96300ef4ebcbf872951.TableFeaturesLearnedInformation): An instance of the TableFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_d8111e2d2a95a96300ef4ebcbf872951 import TableFeaturesLearnedInformation
        return TableFeaturesLearnedInformation(self)

    @property
    def TableStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_9488b714c99c38ed6e9b5f637e107bcb.TableStatLearnedInformation): An instance of the TableStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_9488b714c99c38ed6e9b5f637e107bcb import TableStatLearnedInformation
        return TableStatLearnedInformation(self)

    @property
    def VendorStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_72c9018540f96fd911126c55520168d7.VendorStatLearnedInformation): An instance of the VendorStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_72c9018540f96fd911126c55520168d7 import VendorStatLearnedInformation
        return VendorStatLearnedInformation(self)

    @property
    def AsyncConfStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsyncConfStatResponseTimeOut'])
    @AsyncConfStatResponseTimeOut.setter
    def AsyncConfStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsyncConfStatResponseTimeOut'], value)

    @property
    def DescriptionStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptionStatResponseTimeOut'])
    @DescriptionStatResponseTimeOut.setter
    def DescriptionStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DescriptionStatResponseTimeOut'], value)

    @property
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedFlowDelete'])
    @EnableAsyncConfMasterFlowRemovedFlowDelete.setter
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedFlowDelete'], value)

    @property
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedGroupDelete'])
    @EnableAsyncConfMasterFlowRemovedGroupDelete.setter
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedGroupDelete'], value)

    @property
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedHardTimeOut'])
    @EnableAsyncConfMasterFlowRemovedHardTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedHardTimeOut'], value)

    @property
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedIdleTimeOut'])
    @EnableAsyncConfMasterFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterFlowRemovedIdleTimeOut'], value)

    @property
    def EnableAsyncConfMasterPacketInActionOutputToController(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInActionOutputToController'])
    @EnableAsyncConfMasterPacketInActionOutputToController.setter
    def EnableAsyncConfMasterPacketInActionOutputToController(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInActionOutputToController'], value)

    @property
    def EnableAsyncConfMasterPacketInInvalidTtl(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInInvalidTtl'])
    @EnableAsyncConfMasterPacketInInvalidTtl.setter
    def EnableAsyncConfMasterPacketInInvalidTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInInvalidTtl'], value)

    @property
    def EnableAsyncConfMasterPacketInNoMatching(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInNoMatching'])
    @EnableAsyncConfMasterPacketInNoMatching.setter
    def EnableAsyncConfMasterPacketInNoMatching(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPacketInNoMatching'], value)

    @property
    def EnableAsyncConfMasterPortStatusAdd(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusAdd'])
    @EnableAsyncConfMasterPortStatusAdd.setter
    def EnableAsyncConfMasterPortStatusAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusAdd'], value)

    @property
    def EnableAsyncConfMasterPortStatusDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusDelete'])
    @EnableAsyncConfMasterPortStatusDelete.setter
    def EnableAsyncConfMasterPortStatusDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusDelete'], value)

    @property
    def EnableAsyncConfMasterPortStatusModify(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusModify'])
    @EnableAsyncConfMasterPortStatusModify.setter
    def EnableAsyncConfMasterPortStatusModify(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfMasterPortStatusModify'], value)

    @property
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedFlowDelete'])
    @EnableAsyncConfSlaveFlowRemovedFlowDelete.setter
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedFlowDelete'], value)

    @property
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedGroupDelete'])
    @EnableAsyncConfSlaveFlowRemovedGroupDelete.setter
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedGroupDelete'], value)

    @property
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedHardTimeOut'])
    @EnableAsyncConfSlaveFlowRemovedHardTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedHardTimeOut'], value)

    @property
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedIdleTimeOut'])
    @EnableAsyncConfSlaveFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlaveFlowRemovedIdleTimeOut'], value)

    @property
    def EnableAsyncConfSlavePacketInActionOutputToController(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInActionOutputToController'])
    @EnableAsyncConfSlavePacketInActionOutputToController.setter
    def EnableAsyncConfSlavePacketInActionOutputToController(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInActionOutputToController'], value)

    @property
    def EnableAsyncConfSlavePacketInInvalidTtl(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInInvalidTtl'])
    @EnableAsyncConfSlavePacketInInvalidTtl.setter
    def EnableAsyncConfSlavePacketInInvalidTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInInvalidTtl'], value)

    @property
    def EnableAsyncConfSlavePacketInNoMatching(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInNoMatching'])
    @EnableAsyncConfSlavePacketInNoMatching.setter
    def EnableAsyncConfSlavePacketInNoMatching(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePacketInNoMatching'], value)

    @property
    def EnableAsyncConfSlavePortStatusAdd(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusAdd'])
    @EnableAsyncConfSlavePortStatusAdd.setter
    def EnableAsyncConfSlavePortStatusAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusAdd'], value)

    @property
    def EnableAsyncConfSlavePortStatusDelete(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusDelete'])
    @EnableAsyncConfSlavePortStatusDelete.setter
    def EnableAsyncConfSlavePortStatusDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusDelete'], value)

    @property
    def EnableAsyncConfSlavePortStatusModify(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusModify'])
    @EnableAsyncConfSlavePortStatusModify.setter
    def EnableAsyncConfSlavePortStatusModify(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsyncConfSlavePortStatusModify'], value)

    @property
    def EnableFlowAggregatedStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFlowAggregatedStatMatchCapability'])
    @EnableFlowAggregatedStatMatchCapability.setter
    def EnableFlowAggregatedStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFlowAggregatedStatMatchCapability'], value)

    @property
    def EnableFlowStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFlowStatMatchCapability'])
    @EnableFlowStatMatchCapability.setter
    def EnableFlowStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFlowStatMatchCapability'], value)

    @property
    def EnableGroupStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGroupStatMatchCapability'])
    @EnableGroupStatMatchCapability.setter
    def EnableGroupStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGroupStatMatchCapability'], value)

    @property
    def EnablePortStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePortStatMatchCapability'])
    @EnablePortStatMatchCapability.setter
    def EnablePortStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePortStatMatchCapability'], value)

    @property
    def EnableQueueStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableQueueStatMatchCapability'])
    @EnableQueueStatMatchCapability.setter
    def EnableQueueStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableQueueStatMatchCapability'], value)

    @property
    def EnableSendTableFeaturesTrigger(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTableFeaturesTrigger'])
    @EnableSendTableFeaturesTrigger.setter
    def EnableSendTableFeaturesTrigger(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTableFeaturesTrigger'], value)

    @property
    def EnableSendTriggerPortFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggerPortFeaturesLearnedInformation'])
    @EnableSendTriggerPortFeaturesLearnedInformation.setter
    def EnableSendTriggerPortFeaturesLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggerPortFeaturesLearnedInformation'], value)

    @property
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredAsyncConfStatLearnedInformation'])
    @EnableSendTriggeredAsyncConfStatLearnedInformation.setter
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredAsyncConfStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredBarrierRequestMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredBarrierRequestMessage'])
    @EnableSendTriggeredBarrierRequestMessage.setter
    def EnableSendTriggeredBarrierRequestMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredBarrierRequestMessage'], value)

    @property
    def EnableSendTriggeredDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredDescriptionStatLearnedInformation'])
    @EnableSendTriggeredDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredDescriptionStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredDescriptionStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredFlowAggregatedStatLearnedInformation'])
    @EnableSendTriggeredFlowAggregatedStatLearnedInformation.setter
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredFlowAggregatedStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredFlowStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredFlowStatLearnedInformation'])
    @EnableSendTriggeredFlowStatLearnedInformation.setter
    def EnableSendTriggeredFlowStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredFlowStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupDescriptionStatLearnedInformation'])
    @EnableSendTriggeredGroupDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupDescriptionStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupFeatureStatLearnedInformation'])
    @EnableSendTriggeredGroupFeatureStatLearnedInformation.setter
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupFeatureStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredGroupStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupStatLearnedInformation'])
    @EnableSendTriggeredGroupStatLearnedInformation.setter
    def EnableSendTriggeredGroupStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredGroupStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredPacketOutMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPacketOutMessage'])
    @EnableSendTriggeredPacketOutMessage.setter
    def EnableSendTriggeredPacketOutMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPacketOutMessage'], value)

    @property
    def EnableSendTriggeredPortModificationMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPortModificationMessage'])
    @EnableSendTriggeredPortModificationMessage.setter
    def EnableSendTriggeredPortModificationMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPortModificationMessage'], value)

    @property
    def EnableSendTriggeredPortStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPortStatLearnedInformation'])
    @EnableSendTriggeredPortStatLearnedInformation.setter
    def EnableSendTriggeredPortStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredPortStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredQueueConfigLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredQueueConfigLearnedInformation'])
    @EnableSendTriggeredQueueConfigLearnedInformation.setter
    def EnableSendTriggeredQueueConfigLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredQueueConfigLearnedInformation'], value)

    @property
    def EnableSendTriggeredQueueStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredQueueStatLearnedInformation'])
    @EnableSendTriggeredQueueStatLearnedInformation.setter
    def EnableSendTriggeredQueueStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredQueueStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredRoleRequestMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredRoleRequestMessage'])
    @EnableSendTriggeredRoleRequestMessage.setter
    def EnableSendTriggeredRoleRequestMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredRoleRequestMessage'], value)

    @property
    def EnableSendTriggeredSwitchConfigLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredSwitchConfigLearnedInformation'])
    @EnableSendTriggeredSwitchConfigLearnedInformation.setter
    def EnableSendTriggeredSwitchConfigLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredSwitchConfigLearnedInformation'], value)

    @property
    def EnableSendTriggeredTableStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredTableStatLearnedInformation'])
    @EnableSendTriggeredTableStatLearnedInformation.setter
    def EnableSendTriggeredTableStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredTableStatLearnedInformation'], value)

    @property
    def EnableSendTriggeredVendorStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggeredVendorStatLearnedInformation'])
    @EnableSendTriggeredVendorStatLearnedInformation.setter
    def EnableSendTriggeredVendorStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggeredVendorStatLearnedInformation'], value)

    @property
    def EnableSetAsyncConfig(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSetAsyncConfig'])
    @EnableSetAsyncConfig.setter
    def EnableSetAsyncConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSetAsyncConfig'], value)

    @property
    def EnableSetSwitchConfig(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSetSwitchConfig'])
    @EnableSetSwitchConfig.setter
    def EnableSetSwitchConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSetSwitchConfig'], value)

    @property
    def EnableSetTableFeatures(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSetTableFeatures'])
    @EnableSetTableFeatures.setter
    def EnableSetTableFeatures(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSetTableFeatures'], value)

    @property
    def EnableTableStatMatchCapability(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTableStatMatchCapability'])
    @EnableTableStatMatchCapability.setter
    def EnableTableStatMatchCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTableStatMatchCapability'], value)

    @property
    def EnableTriggeredVendorMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTriggeredVendorMessage'])
    @EnableTriggeredVendorMessage.setter
    def EnableTriggeredVendorMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTriggeredVendorMessage'], value)

    @property
    def FlowAggregatedStatEthernetDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetDestination'])
    @FlowAggregatedStatEthernetDestination.setter
    def FlowAggregatedStatEthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetDestination'], value)

    @property
    def FlowAggregatedStatEthernetSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetSource'])
    @FlowAggregatedStatEthernetSource.setter
    def FlowAggregatedStatEthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetSource'], value)

    @property
    def FlowAggregatedStatEthernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetType'])
    @FlowAggregatedStatEthernetType.setter
    def FlowAggregatedStatEthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatEthernetType'], value)

    @property
    def FlowAggregatedStatInPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatInPort'])
    @FlowAggregatedStatInPort.setter
    def FlowAggregatedStatInPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatInPort'], value)

    @property
    def FlowAggregatedStatIpDscp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpDscp'])
    @FlowAggregatedStatIpDscp.setter
    def FlowAggregatedStatIpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpDscp'], value)

    @property
    def FlowAggregatedStatIpProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpProtocol'])
    @FlowAggregatedStatIpProtocol.setter
    def FlowAggregatedStatIpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpProtocol'], value)

    @property
    def FlowAggregatedStatIpv4Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpv4Destination'])
    @FlowAggregatedStatIpv4Destination.setter
    def FlowAggregatedStatIpv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpv4Destination'], value)

    @property
    def FlowAggregatedStatIpv4Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpv4Source'])
    @FlowAggregatedStatIpv4Source.setter
    def FlowAggregatedStatIpv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatIpv4Source'], value)

    @property
    def FlowAggregatedStatOutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatOutPortInputMode'])
    @FlowAggregatedStatOutPortInputMode.setter
    def FlowAggregatedStatOutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatOutPortInputMode'], value)

    @property
    def FlowAggregatedStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatResponseTimeOut'])
    @FlowAggregatedStatResponseTimeOut.setter
    def FlowAggregatedStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatResponseTimeOut'], value)

    @property
    def FlowAggregatedStatTableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTableIdInputMode'])
    @FlowAggregatedStatTableIdInputMode.setter
    def FlowAggregatedStatTableIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTableIdInputMode'], value)

    @property
    def FlowAggregatedStatTableIdInputModeNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTableIdInputModeNumber'])
    @FlowAggregatedStatTableIdInputModeNumber.setter
    def FlowAggregatedStatTableIdInputModeNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTableIdInputModeNumber'], value)

    @property
    def FlowAggregatedStatTransportDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTransportDestination'])
    @FlowAggregatedStatTransportDestination.setter
    def FlowAggregatedStatTransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTransportDestination'], value)

    @property
    def FlowAggregatedStatTransportSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTransportSource'])
    @FlowAggregatedStatTransportSource.setter
    def FlowAggregatedStatTransportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatTransportSource'], value)

    @property
    def FlowAggregatedStatVlanId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatVlanId'])
    @FlowAggregatedStatVlanId.setter
    def FlowAggregatedStatVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatVlanId'], value)

    @property
    def FlowAggregatedStatVlanPriority(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowAggregatedStatVlanPriority'])
    @FlowAggregatedStatVlanPriority.setter
    def FlowAggregatedStatVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowAggregatedStatVlanPriority'], value)

    @property
    def FlowStatEthernetDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatEthernetDestination'])
    @FlowStatEthernetDestination.setter
    def FlowStatEthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatEthernetDestination'], value)

    @property
    def FlowStatEthernetSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatEthernetSource'])
    @FlowStatEthernetSource.setter
    def FlowStatEthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatEthernetSource'], value)

    @property
    def FlowStatEthernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatEthernetType'])
    @FlowStatEthernetType.setter
    def FlowStatEthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatEthernetType'], value)

    @property
    def FlowStatInPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatInPort'])
    @FlowStatInPort.setter
    def FlowStatInPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatInPort'], value)

    @property
    def FlowStatIpDscp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatIpDscp'])
    @FlowStatIpDscp.setter
    def FlowStatIpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatIpDscp'], value)

    @property
    def FlowStatIpProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatIpProtocol'])
    @FlowStatIpProtocol.setter
    def FlowStatIpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatIpProtocol'], value)

    @property
    def FlowStatIpv4Destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatIpv4Destination'])
    @FlowStatIpv4Destination.setter
    def FlowStatIpv4Destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatIpv4Destination'], value)

    @property
    def FlowStatIpv4Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatIpv4Source'])
    @FlowStatIpv4Source.setter
    def FlowStatIpv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatIpv4Source'], value)

    @property
    def FlowStatOutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutPortInputMode'])
    @FlowStatOutPortInputMode.setter
    def FlowStatOutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutPortInputMode'], value)

    @property
    def FlowStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatResponseTimeOut'])
    @FlowStatResponseTimeOut.setter
    def FlowStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatResponseTimeOut'], value)

    @property
    def FlowStatTableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTableIdInputMode'])
    @FlowStatTableIdInputMode.setter
    def FlowStatTableIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTableIdInputMode'], value)

    @property
    def FlowStatTableIdInputModeNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTableIdInputModeNumber'])
    @FlowStatTableIdInputModeNumber.setter
    def FlowStatTableIdInputModeNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTableIdInputModeNumber'], value)

    @property
    def FlowStatTransportDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTransportDestination'])
    @FlowStatTransportDestination.setter
    def FlowStatTransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTransportDestination'], value)

    @property
    def FlowStatTransportSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTransportSource'])
    @FlowStatTransportSource.setter
    def FlowStatTransportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTransportSource'], value)

    @property
    def FlowStatVlanId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatVlanId'])
    @FlowStatVlanId.setter
    def FlowStatVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatVlanId'], value)

    @property
    def FlowStatVlanPriority(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatVlanPriority'])
    @FlowStatVlanPriority.setter
    def FlowStatVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatVlanPriority'], value)

    @property
    def GroupDescriptionStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupDescriptionStatResponseTimeOut'])
    @GroupDescriptionStatResponseTimeOut.setter
    def GroupDescriptionStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupDescriptionStatResponseTimeOut'], value)

    @property
    def GroupFeatureStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupFeatureStatResponseTimeOut'])
    @GroupFeatureStatResponseTimeOut.setter
    def GroupFeatureStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupFeatureStatResponseTimeOut'], value)

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])
    @GroupId.setter
    def GroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupId'], value)

    @property
    def GroupIdType(self):
        """
        Returns
        -------
        - str(ofpgAll | ofpgAny | manual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupIdType'])
    @GroupIdType.setter
    def GroupIdType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupIdType'], value)

    @property
    def GroupStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupStatResponseTimeOut'])
    @GroupStatResponseTimeOut.setter
    def GroupStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupStatResponseTimeOut'], value)

    @property
    def IsAsyncConfStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAsyncConfStatLearnedInformationRefreshed'])

    @property
    def IsDescriptionStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDescriptionStatLearnedInformationRefreshed'])

    @property
    def IsFlowAggregatedStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsFlowAggregatedStatLearnedInformationRefreshed'])

    @property
    def IsFlowStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsFlowStatLearnedInformationRefreshed'])

    @property
    def IsGroupDescriptionStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsGroupDescriptionStatLearnedInformationRefreshed'])

    @property
    def IsGroupFeatureStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsGroupFeatureStatLearnedInformationRefreshed'])

    @property
    def IsGroupStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsGroupStatLearnedInformationRefreshed'])

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfChannelLearnedInformationRefreshed'])

    @property
    def IsPortFeaturesLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPortFeaturesLearnedInformationRefreshed'])

    @property
    def IsPortStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPortStatLearnedInformationRefreshed'])

    @property
    def IsQueueConfigLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsQueueConfigLearnedInformationRefreshed'])

    @property
    def IsQueueStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsQueueStatLearnedInformationRefreshed'])

    @property
    def IsTableStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsTableStatLearnedInformationRefreshed'])

    @property
    def IsVendorStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsVendorStatLearnedInformationRefreshed'])

    @property
    def PacketOutAuxiliaryId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutAuxiliaryId'])
    @PacketOutAuxiliaryId.setter
    def PacketOutAuxiliaryId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutAuxiliaryId'], value)

    @property
    def PacketOutBufferId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutBufferId'])
    @PacketOutBufferId.setter
    def PacketOutBufferId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutBufferId'], value)

    @property
    def PacketOutBufferIdInputMode(self):
        """
        Returns
        -------
        - str(opfNoBuffer | manual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutBufferIdInputMode'])
    @PacketOutBufferIdInputMode.setter
    def PacketOutBufferIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutBufferIdInputMode'], value)

    @property
    def PacketOutData(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutData'])
    @PacketOutData.setter
    def PacketOutData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutData'], value)

    @property
    def PacketOutDataLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutDataLength'])
    @PacketOutDataLength.setter
    def PacketOutDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutDataLength'], value)

    @property
    def PacketOutInPortInputMode(self):
        """
        Returns
        -------
        - str(ofppController | ofppLocal | manual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutInPortInputMode'])
    @PacketOutInPortInputMode.setter
    def PacketOutInPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutInPortInputMode'], value)

    @property
    def PacketOutInPortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketOutInPortNumber'])
    @PacketOutInPortNumber.setter
    def PacketOutInPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketOutInPortNumber'], value)

    @property
    def PortFeaturesResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortFeaturesResponseTimeOut'])
    @PortFeaturesResponseTimeOut.setter
    def PortFeaturesResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortFeaturesResponseTimeOut'], value)

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNumber'], value)

    @property
    def PortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppNone | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumberInputMode'])
    @PortNumberInputMode.setter
    def PortNumberInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNumberInputMode'], value)

    @property
    def PortStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortStatResponseTimeOut'])
    @PortStatResponseTimeOut.setter
    def PortStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortStatResponseTimeOut'], value)

    @property
    def QueueConfigPortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueConfigPortNumber'])
    @QueueConfigPortNumber.setter
    def QueueConfigPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueConfigPortNumber'], value)

    @property
    def QueueConfigResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueConfigResponseTimeOut'])
    @QueueConfigResponseTimeOut.setter
    def QueueConfigResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueConfigResponseTimeOut'], value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueId'], value)

    @property
    def QueueIdInputMode(self):
        """
        Returns
        -------
        - str(ofpqAll | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueIdInputMode'])
    @QueueIdInputMode.setter
    def QueueIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueIdInputMode'], value)

    @property
    def QueueStatPortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueStatPortNumber'])
    @QueueStatPortNumber.setter
    def QueueStatPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueStatPortNumber'], value)

    @property
    def QueueStatPortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppAll | custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueStatPortNumberInputMode'])
    @QueueStatPortNumberInputMode.setter
    def QueueStatPortNumberInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueStatPortNumberInputMode'], value)

    @property
    def QueueStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueStatResponseTimeOut'])
    @QueueStatResponseTimeOut.setter
    def QueueStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueStatResponseTimeOut'], value)

    @property
    def RoleRequestGenerationId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoleRequestGenerationId'])
    @RoleRequestGenerationId.setter
    def RoleRequestGenerationId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoleRequestGenerationId'], value)

    @property
    def RoleRequestType(self):
        """
        Returns
        -------
        - str(equal | master | slave | noChange): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoleRequestType'])
    @RoleRequestType.setter
    def RoleRequestType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoleRequestType'], value)

    @property
    def SwitchConfigDropFragments(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchConfigDropFragments'])
    @SwitchConfigDropFragments.setter
    def SwitchConfigDropFragments(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchConfigDropFragments'], value)

    @property
    def SwitchConfigMissSendLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchConfigMissSendLength'])
    @SwitchConfigMissSendLength.setter
    def SwitchConfigMissSendLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchConfigMissSendLength'], value)

    @property
    def SwitchConfigReassembleFragments(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchConfigReassembleFragments'])
    @SwitchConfigReassembleFragments.setter
    def SwitchConfigReassembleFragments(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchConfigReassembleFragments'], value)

    @property
    def SwitchConfigResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchConfigResponseTimeOut'])
    @SwitchConfigResponseTimeOut.setter
    def SwitchConfigResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SwitchConfigResponseTimeOut'], value)

    @property
    def TableFeatureConfig(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureConfig'])
    @TableFeatureConfig.setter
    def TableFeatureConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureConfig'], value)

    @property
    def TableFeatureMaxEntries(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureMaxEntries'])
    @TableFeatureMaxEntries.setter
    def TableFeatureMaxEntries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureMaxEntries'], value)

    @property
    def TableFeatureMetadataMatch(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureMetadataMatch'])
    @TableFeatureMetadataMatch.setter
    def TableFeatureMetadataMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureMetadataMatch'], value)

    @property
    def TableFeatureMetadataWrite(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureMetadataWrite'])
    @TableFeatureMetadataWrite.setter
    def TableFeatureMetadataWrite(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureMetadataWrite'], value)

    @property
    def TableFeatureName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureName'])
    @TableFeatureName.setter
    def TableFeatureName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureName'], value)

    @property
    def TableFeatureResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureResponseTimeOut'])
    @TableFeatureResponseTimeOut.setter
    def TableFeatureResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureResponseTimeOut'], value)

    @property
    def TableFeatureTableId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableFeatureTableId'])
    @TableFeatureTableId.setter
    def TableFeatureTableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableFeatureTableId'], value)

    @property
    def TableStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableStatResponseTimeOut'])
    @TableStatResponseTimeOut.setter
    def TableStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableStatResponseTimeOut'], value)

    @property
    def TriggeredVendorMessage(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggeredVendorMessage'])
    @TriggeredVendorMessage.setter
    def TriggeredVendorMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggeredVendorMessage'], value)

    @property
    def TriggeredVendorMessageId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggeredVendorMessageId'])
    @TriggeredVendorMessageId.setter
    def TriggeredVendorMessageId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggeredVendorMessageId'], value)

    @property
    def TriggeredVendorMessageLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TriggeredVendorMessageLength'])
    @TriggeredVendorMessageLength.setter
    def TriggeredVendorMessageLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TriggeredVendorMessageLength'], value)

    @property
    def VendorId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorId'])
    @VendorId.setter
    def VendorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorId'], value)

    @property
    def VendorMessage(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessage'])
    @VendorMessage.setter
    def VendorMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorMessage'], value)

    @property
    def VendorMessageLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessageLength'])
    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorMessageLength'], value)

    @property
    def VendorStateResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorStateResponseTimeOut'])
    @VendorStateResponseTimeOut.setter
    def VendorStateResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorStateResponseTimeOut'], value)

    def update(self, AsyncConfStatResponseTimeOut=None, DescriptionStatResponseTimeOut=None, EnableAsyncConfMasterFlowRemovedFlowDelete=None, EnableAsyncConfMasterFlowRemovedGroupDelete=None, EnableAsyncConfMasterFlowRemovedHardTimeOut=None, EnableAsyncConfMasterFlowRemovedIdleTimeOut=None, EnableAsyncConfMasterPacketInActionOutputToController=None, EnableAsyncConfMasterPacketInInvalidTtl=None, EnableAsyncConfMasterPacketInNoMatching=None, EnableAsyncConfMasterPortStatusAdd=None, EnableAsyncConfMasterPortStatusDelete=None, EnableAsyncConfMasterPortStatusModify=None, EnableAsyncConfSlaveFlowRemovedFlowDelete=None, EnableAsyncConfSlaveFlowRemovedGroupDelete=None, EnableAsyncConfSlaveFlowRemovedHardTimeOut=None, EnableAsyncConfSlaveFlowRemovedIdleTimeOut=None, EnableAsyncConfSlavePacketInActionOutputToController=None, EnableAsyncConfSlavePacketInInvalidTtl=None, EnableAsyncConfSlavePacketInNoMatching=None, EnableAsyncConfSlavePortStatusAdd=None, EnableAsyncConfSlavePortStatusDelete=None, EnableAsyncConfSlavePortStatusModify=None, EnableFlowAggregatedStatMatchCapability=None, EnableFlowStatMatchCapability=None, EnableGroupStatMatchCapability=None, EnablePortStatMatchCapability=None, EnableQueueStatMatchCapability=None, EnableSendTableFeaturesTrigger=None, EnableSendTriggerPortFeaturesLearnedInformation=None, EnableSendTriggeredAsyncConfStatLearnedInformation=None, EnableSendTriggeredBarrierRequestMessage=None, EnableSendTriggeredDescriptionStatLearnedInformation=None, EnableSendTriggeredFlowAggregatedStatLearnedInformation=None, EnableSendTriggeredFlowStatLearnedInformation=None, EnableSendTriggeredGroupDescriptionStatLearnedInformation=None, EnableSendTriggeredGroupFeatureStatLearnedInformation=None, EnableSendTriggeredGroupStatLearnedInformation=None, EnableSendTriggeredPacketOutMessage=None, EnableSendTriggeredPortModificationMessage=None, EnableSendTriggeredPortStatLearnedInformation=None, EnableSendTriggeredQueueConfigLearnedInformation=None, EnableSendTriggeredQueueStatLearnedInformation=None, EnableSendTriggeredRoleRequestMessage=None, EnableSendTriggeredSwitchConfigLearnedInformation=None, EnableSendTriggeredTableStatLearnedInformation=None, EnableSendTriggeredVendorStatLearnedInformation=None, EnableSetAsyncConfig=None, EnableSetSwitchConfig=None, EnableSetTableFeatures=None, EnableTableStatMatchCapability=None, EnableTriggeredVendorMessage=None, FlowAggregatedStatEthernetDestination=None, FlowAggregatedStatEthernetSource=None, FlowAggregatedStatEthernetType=None, FlowAggregatedStatInPort=None, FlowAggregatedStatIpDscp=None, FlowAggregatedStatIpProtocol=None, FlowAggregatedStatIpv4Destination=None, FlowAggregatedStatIpv4Source=None, FlowAggregatedStatOutPortInputMode=None, FlowAggregatedStatResponseTimeOut=None, FlowAggregatedStatTableIdInputMode=None, FlowAggregatedStatTableIdInputModeNumber=None, FlowAggregatedStatTransportDestination=None, FlowAggregatedStatTransportSource=None, FlowAggregatedStatVlanId=None, FlowAggregatedStatVlanPriority=None, FlowStatEthernetDestination=None, FlowStatEthernetSource=None, FlowStatEthernetType=None, FlowStatInPort=None, FlowStatIpDscp=None, FlowStatIpProtocol=None, FlowStatIpv4Destination=None, FlowStatIpv4Source=None, FlowStatOutPortInputMode=None, FlowStatResponseTimeOut=None, FlowStatTableIdInputMode=None, FlowStatTableIdInputModeNumber=None, FlowStatTransportDestination=None, FlowStatTransportSource=None, FlowStatVlanId=None, FlowStatVlanPriority=None, GroupDescriptionStatResponseTimeOut=None, GroupFeatureStatResponseTimeOut=None, GroupId=None, GroupIdType=None, GroupStatResponseTimeOut=None, PacketOutAuxiliaryId=None, PacketOutBufferId=None, PacketOutBufferIdInputMode=None, PacketOutData=None, PacketOutDataLength=None, PacketOutInPortInputMode=None, PacketOutInPortNumber=None, PortFeaturesResponseTimeOut=None, PortNumber=None, PortNumberInputMode=None, PortStatResponseTimeOut=None, QueueConfigPortNumber=None, QueueConfigResponseTimeOut=None, QueueId=None, QueueIdInputMode=None, QueueStatPortNumber=None, QueueStatPortNumberInputMode=None, QueueStatResponseTimeOut=None, RoleRequestGenerationId=None, RoleRequestType=None, SwitchConfigDropFragments=None, SwitchConfigMissSendLength=None, SwitchConfigReassembleFragments=None, SwitchConfigResponseTimeOut=None, TableFeatureConfig=None, TableFeatureMaxEntries=None, TableFeatureMetadataMatch=None, TableFeatureMetadataWrite=None, TableFeatureName=None, TableFeatureResponseTimeOut=None, TableFeatureTableId=None, TableStatResponseTimeOut=None, TriggeredVendorMessage=None, TriggeredVendorMessageId=None, TriggeredVendorMessageLength=None, VendorId=None, VendorMessage=None, VendorMessageLength=None, VendorStateResponseTimeOut=None):
        """Updates learnedInformation resource on the server.

        Args
        ----
        - AsyncConfStatResponseTimeOut (number): 
        - DescriptionStatResponseTimeOut (number): 
        - EnableAsyncConfMasterFlowRemovedFlowDelete (bool): 
        - EnableAsyncConfMasterFlowRemovedGroupDelete (bool): 
        - EnableAsyncConfMasterFlowRemovedHardTimeOut (bool): 
        - EnableAsyncConfMasterFlowRemovedIdleTimeOut (bool): 
        - EnableAsyncConfMasterPacketInActionOutputToController (bool): 
        - EnableAsyncConfMasterPacketInInvalidTtl (bool): 
        - EnableAsyncConfMasterPacketInNoMatching (bool): 
        - EnableAsyncConfMasterPortStatusAdd (bool): 
        - EnableAsyncConfMasterPortStatusDelete (bool): 
        - EnableAsyncConfMasterPortStatusModify (bool): 
        - EnableAsyncConfSlaveFlowRemovedFlowDelete (bool): 
        - EnableAsyncConfSlaveFlowRemovedGroupDelete (bool): 
        - EnableAsyncConfSlaveFlowRemovedHardTimeOut (bool): 
        - EnableAsyncConfSlaveFlowRemovedIdleTimeOut (bool): 
        - EnableAsyncConfSlavePacketInActionOutputToController (bool): 
        - EnableAsyncConfSlavePacketInInvalidTtl (bool): 
        - EnableAsyncConfSlavePacketInNoMatching (bool): 
        - EnableAsyncConfSlavePortStatusAdd (bool): 
        - EnableAsyncConfSlavePortStatusDelete (bool): 
        - EnableAsyncConfSlavePortStatusModify (bool): 
        - EnableFlowAggregatedStatMatchCapability (bool): 
        - EnableFlowStatMatchCapability (bool): 
        - EnableGroupStatMatchCapability (bool): 
        - EnablePortStatMatchCapability (bool): 
        - EnableQueueStatMatchCapability (bool): 
        - EnableSendTableFeaturesTrigger (bool): 
        - EnableSendTriggerPortFeaturesLearnedInformation (bool): 
        - EnableSendTriggeredAsyncConfStatLearnedInformation (bool): 
        - EnableSendTriggeredBarrierRequestMessage (bool): 
        - EnableSendTriggeredDescriptionStatLearnedInformation (bool): 
        - EnableSendTriggeredFlowAggregatedStatLearnedInformation (bool): 
        - EnableSendTriggeredFlowStatLearnedInformation (bool): 
        - EnableSendTriggeredGroupDescriptionStatLearnedInformation (bool): 
        - EnableSendTriggeredGroupFeatureStatLearnedInformation (bool): 
        - EnableSendTriggeredGroupStatLearnedInformation (bool): 
        - EnableSendTriggeredPacketOutMessage (bool): 
        - EnableSendTriggeredPortModificationMessage (bool): 
        - EnableSendTriggeredPortStatLearnedInformation (bool): 
        - EnableSendTriggeredQueueConfigLearnedInformation (bool): 
        - EnableSendTriggeredQueueStatLearnedInformation (bool): 
        - EnableSendTriggeredRoleRequestMessage (bool): 
        - EnableSendTriggeredSwitchConfigLearnedInformation (bool): 
        - EnableSendTriggeredTableStatLearnedInformation (bool): 
        - EnableSendTriggeredVendorStatLearnedInformation (bool): 
        - EnableSetAsyncConfig (bool): 
        - EnableSetSwitchConfig (bool): 
        - EnableSetTableFeatures (bool): 
        - EnableTableStatMatchCapability (bool): 
        - EnableTriggeredVendorMessage (bool): 
        - FlowAggregatedStatEthernetDestination (str): 
        - FlowAggregatedStatEthernetSource (str): 
        - FlowAggregatedStatEthernetType (str): 
        - FlowAggregatedStatInPort (str): 
        - FlowAggregatedStatIpDscp (str): 
        - FlowAggregatedStatIpProtocol (str): 
        - FlowAggregatedStatIpv4Destination (str): 
        - FlowAggregatedStatIpv4Source (str): 
        - FlowAggregatedStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): 
        - FlowAggregatedStatResponseTimeOut (number): 
        - FlowAggregatedStatTableIdInputMode (str(allTables | emergency | custom)): 
        - FlowAggregatedStatTableIdInputModeNumber (number): 
        - FlowAggregatedStatTransportDestination (str): 
        - FlowAggregatedStatTransportSource (str): 
        - FlowAggregatedStatVlanId (str): 
        - FlowAggregatedStatVlanPriority (str): 
        - FlowStatEthernetDestination (str): 
        - FlowStatEthernetSource (str): 
        - FlowStatEthernetType (str): 
        - FlowStatInPort (str): 
        - FlowStatIpDscp (str): 
        - FlowStatIpProtocol (str): 
        - FlowStatIpv4Destination (str): 
        - FlowStatIpv4Source (str): 
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): 
        - FlowStatResponseTimeOut (number): 
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): 
        - FlowStatTableIdInputModeNumber (number): 
        - FlowStatTransportDestination (str): 
        - FlowStatTransportSource (str): 
        - FlowStatVlanId (str): 
        - FlowStatVlanPriority (str): 
        - GroupDescriptionStatResponseTimeOut (number): 
        - GroupFeatureStatResponseTimeOut (number): 
        - GroupId (number): 
        - GroupIdType (str(ofpgAll | ofpgAny | manual)): 
        - GroupStatResponseTimeOut (number): 
        - PacketOutAuxiliaryId (number): 
        - PacketOutBufferId (number): 
        - PacketOutBufferIdInputMode (str(opfNoBuffer | manual)): 
        - PacketOutData (str): 
        - PacketOutDataLength (number): 
        - PacketOutInPortInputMode (str(ofppController | ofppLocal | manual)): 
        - PacketOutInPortNumber (number): 
        - PortFeaturesResponseTimeOut (number): 
        - PortNumber (number): 
        - PortNumberInputMode (str(ofppNone | custom)): 
        - PortStatResponseTimeOut (number): 
        - QueueConfigPortNumber (number): 
        - QueueConfigResponseTimeOut (number): 
        - QueueId (number): 
        - QueueIdInputMode (str(ofpqAll | custom)): 
        - QueueStatPortNumber (number): 
        - QueueStatPortNumberInputMode (str(ofppAll | custom)): 
        - QueueStatResponseTimeOut (number): 
        - RoleRequestGenerationId (str): 
        - RoleRequestType (str(equal | master | slave | noChange)): 
        - SwitchConfigDropFragments (bool): 
        - SwitchConfigMissSendLength (number): 
        - SwitchConfigReassembleFragments (bool): 
        - SwitchConfigResponseTimeOut (number): 
        - TableFeatureConfig (number): 
        - TableFeatureMaxEntries (number): 
        - TableFeatureMetadataMatch (str): 
        - TableFeatureMetadataWrite (str): 
        - TableFeatureName (str): 
        - TableFeatureResponseTimeOut (number): 
        - TableFeatureTableId (number): 
        - TableStatResponseTimeOut (number): 
        - TriggeredVendorMessage (str): 
        - TriggeredVendorMessageId (number): 
        - TriggeredVendorMessageLength (number): 
        - VendorId (number): 
        - VendorMessage (str): 
        - VendorMessageLength (number): 
        - VendorStateResponseTimeOut (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
