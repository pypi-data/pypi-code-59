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


class SwitchLearnedInformation(Base):
    """
    The SwitchLearnedInformation class encapsulates a required switchLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'switchLearnedInformation'
    _SDM_ATT_MAP = {
        'EnableVendorExperimenterMessage': 'enableVendorExperimenterMessage',
        'EthernetDestination': 'ethernetDestination',
        'EthernetSource': 'ethernetSource',
        'EthernetType': 'ethernetType',
        'InPort': 'inPort',
        'IpDscp': 'ipDscp',
        'IpProtocol': 'ipProtocol',
        'Ipv4Source': 'ipv4Source',
        'Ipv4destination': 'ipv4destination',
        'IsOfChannelLearnedInformationRefreshed': 'isOfChannelLearnedInformationRefreshed',
        'IsOfFlowsLearnedInformationRefreshed': 'isOfFlowsLearnedInformationRefreshed',
        'OutPort': 'outPort',
        'OutPortInputMode': 'outPortInputMode',
        'TableId': 'tableId',
        'TableIdInputMode': 'tableIdInputMode',
        'TansportSource': 'tansportSource',
        'TransportDestination': 'transportDestination',
        'VendorExperimenterId': 'vendorExperimenterId',
        'VendorExperimenterType': 'vendorExperimenterType',
        'VendorMessage': 'vendorMessage',
        'VendorMessageLength': 'vendorMessageLength',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(SwitchLearnedInformation, self).__init__(parent)

    @property
    def OfChannelSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_8014ef79f44d2c63a73d35dd12599267.OfChannelSwitchLearnedInfo): An instance of the OfChannelSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_8014ef79f44d2c63a73d35dd12599267 import OfChannelSwitchLearnedInfo
        return OfChannelSwitchLearnedInfo(self)

    @property
    def SwitchFlow131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_f684d69a421575142ffb1973005001bd.SwitchFlow131TriggerAttributes): An instance of the SwitchFlow131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_f684d69a421575142ffb1973005001bd import SwitchFlow131TriggerAttributes
        return SwitchFlow131TriggerAttributes(self)._select()

    @property
    def SwitchFlowLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_ca1989680f648fe88b21f62ddc39567b.SwitchFlowLearnedInfo): An instance of the SwitchFlowLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_ca1989680f648fe88b21f62ddc39567b import SwitchFlowLearnedInfo
        return SwitchFlowLearnedInfo(self)

    @property
    def SwitchFlowMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_3aa835176420a29823aa2b0d3e4805b2.SwitchFlowMatchCriteria131TriggerAttributes): An instance of the SwitchFlowMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_3aa835176420a29823aa2b0d3e4805b2 import SwitchFlowMatchCriteria131TriggerAttributes
        return SwitchFlowMatchCriteria131TriggerAttributes(self)._select()

    @property
    def SwitchGroupLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_aafd044030635b13c0db790095a88328.SwitchGroupLearnedInfo): An instance of the SwitchGroupLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_aafd044030635b13c0db790095a88328 import SwitchGroupLearnedInfo
        return SwitchGroupLearnedInfo(self)

    @property
    def SwitchMeterLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_99f3b816edb76e0b23f8211b94b0b8c7.SwitchMeterLearnedInfo): An instance of the SwitchMeterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_99f3b816edb76e0b23f8211b94b0b8c7 import SwitchMeterLearnedInfo
        return SwitchMeterLearnedInfo(self)

    @property
    def SwitchTableFeaturesStatLearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_bb49dadbbed3b7e099461fbcb8d8e518.SwitchTableFeaturesStatLearnedInfo): An instance of the SwitchTableFeaturesStatLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_bb49dadbbed3b7e099461fbcb8d8e518 import SwitchTableFeaturesStatLearnedInfo
        return SwitchTableFeaturesStatLearnedInfo(self)

    @property
    def EnableVendorExperimenterMessage(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVendorExperimenterMessage'])
    @EnableVendorExperimenterMessage.setter
    def EnableVendorExperimenterMessage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVendorExperimenterMessage'], value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetDestination'])
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetDestination'], value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetSource'])
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetSource'], value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetType'])
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EthernetType'], value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPort'])
    @InPort.setter
    def InPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InPort'], value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpDscp'])
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpDscp'], value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpProtocol'])
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpProtocol'], value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4Source'])
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4Source'], value)

    @property
    def Ipv4destination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4destination'])
    @Ipv4destination.setter
    def Ipv4destination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4destination'], value)

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfChannelLearnedInformationRefreshed'])

    @property
    def IsOfFlowsLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfFlowsLearnedInformationRefreshed'])

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPort'])
    @OutPort.setter
    def OutPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPort'], value)

    @property
    def OutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortInputMode'])
    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OutPortInputMode'], value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableId'])
    @TableId.setter
    def TableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableId'], value)

    @property
    def TableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | tableIdCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableIdInputMode'])
    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableIdInputMode'], value)

    @property
    def TansportSource(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TansportSource'])
    @TansportSource.setter
    def TansportSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TansportSource'], value)

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransportDestination'])
    @TransportDestination.setter
    def TransportDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransportDestination'], value)

    @property
    def VendorExperimenterId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorExperimenterId'])
    @VendorExperimenterId.setter
    def VendorExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorExperimenterId'], value)

    @property
    def VendorExperimenterType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorExperimenterType'])
    @VendorExperimenterType.setter
    def VendorExperimenterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorExperimenterType'], value)

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
    def VlanId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, EnableVendorExperimenterMessage=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Source=None, Ipv4destination=None, OutPort=None, OutPortInputMode=None, TableId=None, TableIdInputMode=None, TansportSource=None, TransportDestination=None, VendorExperimenterId=None, VendorExperimenterType=None, VendorMessage=None, VendorMessageLength=None, VlanId=None, VlanPriority=None):
        """Updates switchLearnedInformation resource on the server.

        Args
        ----
        - EnableVendorExperimenterMessage (bool): 
        - EthernetDestination (str): 
        - EthernetSource (str): 
        - EthernetType (str): 
        - InPort (str): 
        - IpDscp (str): 
        - IpProtocol (str): 
        - Ipv4Source (str): 
        - Ipv4destination (str): 
        - OutPort (number): 
        - OutPortInputMode (str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom)): 
        - TableId (number): 
        - TableIdInputMode (str(allTables | emergency | tableIdCustom)): 
        - TansportSource (str): 
        - TransportDestination (str): 
        - VendorExperimenterId (number): 
        - VendorExperimenterType (number): 
        - VendorMessage (str): 
        - VendorMessageLength (number): 
        - VlanId (str): 
        - VlanPriority (str): 

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

    def RefreshFlows(self):
        """Executes the refreshFlows operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshFlows', payload=payload, response_object=None)

    def RefreshGroupLearnedInformation(self):
        """Executes the refreshGroupLearnedInformation operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshGroupLearnedInformation', payload=payload, response_object=None)

    def RefreshMeterLearnedInformation(self):
        """Executes the refreshMeterLearnedInformation operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshMeterLearnedInformation', payload=payload, response_object=None)

    def RefreshOfChannelLearnedInformation(self):
        """Executes the refreshOfChannelLearnedInformation operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshOfChannelLearnedInformation', payload=payload, response_object=None)

    def RefreshTableFeature(self):
        """Executes the refreshTableFeature operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshTableFeature', payload=payload, response_object=None)

    def Trigger(self):
        """Executes the trigger operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('trigger', payload=payload, response_object=None)
