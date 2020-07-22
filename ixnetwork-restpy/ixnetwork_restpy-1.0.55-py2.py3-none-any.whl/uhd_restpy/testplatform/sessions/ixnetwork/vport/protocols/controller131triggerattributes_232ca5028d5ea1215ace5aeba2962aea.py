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


class Controller131TriggerAttributes(Base):
    """
    The Controller131TriggerAttributes class encapsulates a required controller131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'controller131TriggerAttributes'
    _SDM_ATT_MAP = {
        'EnableSendTriggerMeterConfigStatsLearnedInformation': 'enableSendTriggerMeterConfigStatsLearnedInformation',
        'EnableSendTriggerMeterFeatureStatsLearnedInformation': 'enableSendTriggerMeterFeatureStatsLearnedInformation',
        'EnableSendTriggerMeterStatLearnedInformation': 'enableSendTriggerMeterStatLearnedInformation',
        'FlowStatOutGroup': 'flowStatOutGroup',
        'FlowStatOutGroupInputMode': 'flowStatOutGroupInputMode',
        'FlowStatOutPort': 'flowStatOutPort',
        'FlowStatOutPortInputMode': 'flowStatOutPortInputMode',
        'FlowStatTableId': 'flowStatTableId',
        'FlowStatTableIdInputMode': 'flowStatTableIdInputMode',
        'IsMeterConfigStatLearnedInformationRefreshed': 'isMeterConfigStatLearnedInformationRefreshed',
        'IsMeterFeatureStatLearnedInformationRefreshed': 'isMeterFeatureStatLearnedInformationRefreshed',
        'IsMeterStatLearnedInformationRefreshed': 'isMeterStatLearnedInformationRefreshed',
        'MeterConfigStatMeterId': 'meterConfigStatMeterId',
        'MeterConfigStatMeterNumber': 'meterConfigStatMeterNumber',
        'MeterConfigStatResponseTimeOut': 'meterConfigStatResponseTimeOut',
        'MeterFeatureStatResponseTimeOut': 'meterFeatureStatResponseTimeOut',
        'MeterStatMeterId': 'meterStatMeterId',
        'MeterStatMeterNumber': 'meterStatMeterNumber',
        'MeterStatResponseTimeOut': 'meterStatResponseTimeOut',
        'PortStatPortNumber': 'portStatPortNumber',
        'PortStatPortNumberInputMode': 'portStatPortNumberInputMode',
        'QueueConfigPortNumber': 'queueConfigPortNumber',
        'QueueConfigPortNumberInputMode': 'queueConfigPortNumberInputMode',
        'QueueStatPortNumber': 'queueStatPortNumber',
        'QueueStatPortNumberInputMode': 'queueStatPortNumberInputMode',
        'VendorMessageExperimenterType': 'vendorMessageExperimenterType',
        'VendorStatExperimenterType': 'vendorStatExperimenterType',
    }

    def __init__(self, parent):
        super(Controller131TriggerAttributes, self).__init__(parent)

    @property
    def EnableSendTriggerMeterConfigStatsLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterConfigStatsLearnedInformation'])
    @EnableSendTriggerMeterConfigStatsLearnedInformation.setter
    def EnableSendTriggerMeterConfigStatsLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterConfigStatsLearnedInformation'], value)

    @property
    def EnableSendTriggerMeterFeatureStatsLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterFeatureStatsLearnedInformation'])
    @EnableSendTriggerMeterFeatureStatsLearnedInformation.setter
    def EnableSendTriggerMeterFeatureStatsLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterFeatureStatsLearnedInformation'], value)

    @property
    def EnableSendTriggerMeterStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterStatLearnedInformation'])
    @EnableSendTriggerMeterStatLearnedInformation.setter
    def EnableSendTriggerMeterStatLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSendTriggerMeterStatLearnedInformation'], value)

    @property
    def FlowStatOutGroup(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutGroup'])
    @FlowStatOutGroup.setter
    def FlowStatOutGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutGroup'], value)

    @property
    def FlowStatOutGroupInputMode(self):
        """
        Returns
        -------
        - str(allGroups | anyGroup | outGroupCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutGroupInputMode'])
    @FlowStatOutGroupInputMode.setter
    def FlowStatOutGroupInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutGroupInputMode'], value)

    @property
    def FlowStatOutPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutPort'])
    @FlowStatOutPort.setter
    def FlowStatOutPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutPort'], value)

    @property
    def FlowStatOutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatOutPortInputMode'])
    @FlowStatOutPortInputMode.setter
    def FlowStatOutPortInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatOutPortInputMode'], value)

    @property
    def FlowStatTableId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatTableId'])
    @FlowStatTableId.setter
    def FlowStatTableId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatTableId'], value)

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
    def IsMeterConfigStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMeterConfigStatLearnedInformationRefreshed'])

    @property
    def IsMeterFeatureStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMeterFeatureStatLearnedInformationRefreshed'])

    @property
    def IsMeterStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMeterStatLearnedInformationRefreshed'])

    @property
    def MeterConfigStatMeterId(self):
        """
        Returns
        -------
        - str(ofpmController | ofpmSlowPath | ofpmAll | manual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterConfigStatMeterId'])
    @MeterConfigStatMeterId.setter
    def MeterConfigStatMeterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterConfigStatMeterId'], value)

    @property
    def MeterConfigStatMeterNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterConfigStatMeterNumber'])
    @MeterConfigStatMeterNumber.setter
    def MeterConfigStatMeterNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterConfigStatMeterNumber'], value)

    @property
    def MeterConfigStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterConfigStatResponseTimeOut'])
    @MeterConfigStatResponseTimeOut.setter
    def MeterConfigStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterConfigStatResponseTimeOut'], value)

    @property
    def MeterFeatureStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterFeatureStatResponseTimeOut'])
    @MeterFeatureStatResponseTimeOut.setter
    def MeterFeatureStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterFeatureStatResponseTimeOut'], value)

    @property
    def MeterStatMeterId(self):
        """
        Returns
        -------
        - str(ofpmController | ofpmSlowPath | ofpmAll | manual): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterStatMeterId'])
    @MeterStatMeterId.setter
    def MeterStatMeterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterStatMeterId'], value)

    @property
    def MeterStatMeterNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterStatMeterNumber'])
    @MeterStatMeterNumber.setter
    def MeterStatMeterNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterStatMeterNumber'], value)

    @property
    def MeterStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterStatResponseTimeOut'])
    @MeterStatResponseTimeOut.setter
    def MeterStatResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterStatResponseTimeOut'], value)

    @property
    def PortStatPortNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortStatPortNumber'])
    @PortStatPortNumber.setter
    def PortStatPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortStatPortNumber'], value)

    @property
    def PortStatPortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppAny | portNumberCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortStatPortNumberInputMode'])
    @PortStatPortNumberInputMode.setter
    def PortStatPortNumberInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortStatPortNumberInputMode'], value)

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
    def QueueConfigPortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppAny | portNumberCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueConfigPortNumberInputMode'])
    @QueueConfigPortNumberInputMode.setter
    def QueueConfigPortNumberInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueConfigPortNumberInputMode'], value)

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
        - str(ofppAll | ofppAny | portNumberCustom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueStatPortNumberInputMode'])
    @QueueStatPortNumberInputMode.setter
    def QueueStatPortNumberInputMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueStatPortNumberInputMode'], value)

    @property
    def VendorMessageExperimenterType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessageExperimenterType'])
    @VendorMessageExperimenterType.setter
    def VendorMessageExperimenterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorMessageExperimenterType'], value)

    @property
    def VendorStatExperimenterType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorStatExperimenterType'])
    @VendorStatExperimenterType.setter
    def VendorStatExperimenterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorStatExperimenterType'], value)

    def update(self, EnableSendTriggerMeterConfigStatsLearnedInformation=None, EnableSendTriggerMeterFeatureStatsLearnedInformation=None, EnableSendTriggerMeterStatLearnedInformation=None, FlowStatOutGroup=None, FlowStatOutGroupInputMode=None, FlowStatOutPort=None, FlowStatOutPortInputMode=None, FlowStatTableId=None, FlowStatTableIdInputMode=None, MeterConfigStatMeterId=None, MeterConfigStatMeterNumber=None, MeterConfigStatResponseTimeOut=None, MeterFeatureStatResponseTimeOut=None, MeterStatMeterId=None, MeterStatMeterNumber=None, MeterStatResponseTimeOut=None, PortStatPortNumber=None, PortStatPortNumberInputMode=None, QueueConfigPortNumber=None, QueueConfigPortNumberInputMode=None, QueueStatPortNumber=None, QueueStatPortNumberInputMode=None, VendorMessageExperimenterType=None, VendorStatExperimenterType=None):
        """Updates controller131TriggerAttributes resource on the server.

        Args
        ----
        - EnableSendTriggerMeterConfigStatsLearnedInformation (bool): 
        - EnableSendTriggerMeterFeatureStatsLearnedInformation (bool): 
        - EnableSendTriggerMeterStatLearnedInformation (bool): 
        - FlowStatOutGroup (number): 
        - FlowStatOutGroupInputMode (str(allGroups | anyGroup | outGroupCustom)): 
        - FlowStatOutPort (number): 
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppAny | outPortCustom)): 
        - FlowStatTableId (number): 
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): 
        - MeterConfigStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): 
        - MeterConfigStatMeterNumber (number): 
        - MeterConfigStatResponseTimeOut (number): 
        - MeterFeatureStatResponseTimeOut (number): 
        - MeterStatMeterId (str(ofpmController | ofpmSlowPath | ofpmAll | manual)): 
        - MeterStatMeterNumber (number): 
        - MeterStatResponseTimeOut (number): 
        - PortStatPortNumber (number): 
        - PortStatPortNumberInputMode (str(ofppAny | portNumberCustom)): 
        - QueueConfigPortNumber (number): 
        - QueueConfigPortNumberInputMode (str(ofppAny | portNumberCustom)): 
        - QueueStatPortNumber (number): 
        - QueueStatPortNumberInputMode (str(ofppAll | ofppAny | portNumberCustom)): 
        - VendorMessageExperimenterType (number): 
        - VendorStatExperimenterType (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
