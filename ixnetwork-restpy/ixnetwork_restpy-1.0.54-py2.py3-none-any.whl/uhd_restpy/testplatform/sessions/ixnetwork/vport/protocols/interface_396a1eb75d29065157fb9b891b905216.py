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


class Interface(Base):
    """
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'AcceptUnconfiguredChannel': 'acceptUnconfiguredChannel',
        'AllFlowsDelOnStart': 'allFlowsDelOnStart',
        'AuxiliaryConnectionTimeout': 'auxiliaryConnectionTimeout',
        'BadVersionErrorAction': 'badVersionErrorAction',
        'EchoInterval': 'echoInterval',
        'EchoMultiplier': 'echoMultiplier',
        'EchoTimeout': 'echoTimeout',
        'EnableEchoTimeOut': 'enableEchoTimeOut',
        'EnableMultipleLogicalSwitch': 'enableMultipleLogicalSwitch',
        'EnablePeriodicEcho': 'enablePeriodicEcho',
        'EnablePeriodicLldp': 'enablePeriodicLldp',
        'Enabled': 'enabled',
        'FeatureRequestTimeout': 'featureRequestTimeout',
        'FeatureRequestTimeoutAction': 'featureRequestTimeoutAction',
        'InstallFlowForLldp': 'installFlowForLldp',
        'LldpDestinationMacAddress': 'lldpDestinationMacAddress',
        'ModeOfConnection': 'modeOfConnection',
        'NonHelloMessageStartupAction': 'nonHelloMessageStartupAction',
        'PeriodicLldpInterval': 'periodicLldpInterval',
        'ProtocolInterfaces': 'protocolInterfaces',
        'SendPortFeatureAtStartup': 'sendPortFeatureAtStartup',
        'TcpPort': 'tcpPort',
        'TimeOutOption': 'timeOutOption',
        'TypeOfConnection': 'typeOfConnection',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def OfChannel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannel_9036477cbe231f174fe46ed935c71138.OfChannel): An instance of the OfChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannel_9036477cbe231f174fe46ed935c71138 import OfChannel
        return OfChannel(self)

    @property
    def Switch(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switch_e05bb508bd425f6e97cddf103067b461.Switch): An instance of the Switch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.switch_e05bb508bd425f6e97cddf103067b461 import Switch
        return Switch(self)

    @property
    def AcceptUnconfiguredChannel(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcceptUnconfiguredChannel'])
    @AcceptUnconfiguredChannel.setter
    def AcceptUnconfiguredChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcceptUnconfiguredChannel'], value)

    @property
    def AllFlowsDelOnStart(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllFlowsDelOnStart'])
    @AllFlowsDelOnStart.setter
    def AllFlowsDelOnStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllFlowsDelOnStart'], value)

    @property
    def AuxiliaryConnectionTimeout(self):
        """
        Returns
        -------
        - str(auxReSendFeatureRequest | auxFeatureRequestTerminateConnection): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuxiliaryConnectionTimeout'])
    @AuxiliaryConnectionTimeout.setter
    def AuxiliaryConnectionTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuxiliaryConnectionTimeout'], value)

    @property
    def BadVersionErrorAction(self):
        """
        Returns
        -------
        - str(auxReSendHello | auxTerminateConnection): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BadVersionErrorAction'])
    @BadVersionErrorAction.setter
    def BadVersionErrorAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BadVersionErrorAction'], value)

    @property
    def EchoInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoInterval'])
    @EchoInterval.setter
    def EchoInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoInterval'], value)

    @property
    def EchoMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoMultiplier'])
    @EchoMultiplier.setter
    def EchoMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoMultiplier'], value)

    @property
    def EchoTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoTimeout'])
    @EchoTimeout.setter
    def EchoTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoTimeout'], value)

    @property
    def EnableEchoTimeOut(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEchoTimeOut'])
    @EnableEchoTimeOut.setter
    def EnableEchoTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEchoTimeOut'], value)

    @property
    def EnableMultipleLogicalSwitch(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMultipleLogicalSwitch'])
    @EnableMultipleLogicalSwitch.setter
    def EnableMultipleLogicalSwitch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMultipleLogicalSwitch'], value)

    @property
    def EnablePeriodicEcho(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicEcho'])
    @EnablePeriodicEcho.setter
    def EnablePeriodicEcho(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeriodicEcho'], value)

    @property
    def EnablePeriodicLldp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicLldp'])
    @EnablePeriodicLldp.setter
    def EnablePeriodicLldp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeriodicLldp'], value)

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
    def FeatureRequestTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FeatureRequestTimeout'])
    @FeatureRequestTimeout.setter
    def FeatureRequestTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FeatureRequestTimeout'], value)

    @property
    def FeatureRequestTimeoutAction(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FeatureRequestTimeoutAction'])
    @FeatureRequestTimeoutAction.setter
    def FeatureRequestTimeoutAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FeatureRequestTimeoutAction'], value)

    @property
    def InstallFlowForLldp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstallFlowForLldp'])
    @InstallFlowForLldp.setter
    def InstallFlowForLldp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstallFlowForLldp'], value)

    @property
    def LldpDestinationMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LldpDestinationMacAddress'])
    @LldpDestinationMacAddress.setter
    def LldpDestinationMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LldpDestinationMacAddress'], value)

    @property
    def ModeOfConnection(self):
        """
        Returns
        -------
        - str(passive | active | mixed): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ModeOfConnection'])
    @ModeOfConnection.setter
    def ModeOfConnection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ModeOfConnection'], value)

    @property
    def NonHelloMessageStartupAction(self):
        """
        Returns
        -------
        - str(auxAcceptConnection | auxSendError): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NonHelloMessageStartupAction'])
    @NonHelloMessageStartupAction.setter
    def NonHelloMessageStartupAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NonHelloMessageStartupAction'], value)

    @property
    def PeriodicLldpInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicLldpInterval'])
    @PeriodicLldpInterval.setter
    def PeriodicLldpInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicLldpInterval'], value)

    @property
    def ProtocolInterfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterfaces'])
    @ProtocolInterfaces.setter
    def ProtocolInterfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterfaces'], value)

    @property
    def SendPortFeatureAtStartup(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendPortFeatureAtStartup'])
    @SendPortFeatureAtStartup.setter
    def SendPortFeatureAtStartup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendPortFeatureAtStartup'], value)

    @property
    def TcpPort(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TcpPort'])
    @TcpPort.setter
    def TcpPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TcpPort'], value)

    @property
    def TimeOutOption(self):
        """
        Returns
        -------
        - str(multiplier | timeOutValue): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeOutOption'])
    @TimeOutOption.setter
    def TimeOutOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeOutOption'], value)

    @property
    def TypeOfConnection(self):
        """
        Returns
        -------
        - str(tcp | tls): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeOfConnection'])
    @TypeOfConnection.setter
    def TypeOfConnection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeOfConnection'], value)

    def update(self, AcceptUnconfiguredChannel=None, AllFlowsDelOnStart=None, AuxiliaryConnectionTimeout=None, BadVersionErrorAction=None, EchoInterval=None, EchoMultiplier=None, EchoTimeout=None, EnableEchoTimeOut=None, EnableMultipleLogicalSwitch=None, EnablePeriodicEcho=None, EnablePeriodicLldp=None, Enabled=None, FeatureRequestTimeout=None, FeatureRequestTimeoutAction=None, InstallFlowForLldp=None, LldpDestinationMacAddress=None, ModeOfConnection=None, NonHelloMessageStartupAction=None, PeriodicLldpInterval=None, ProtocolInterfaces=None, SendPortFeatureAtStartup=None, TcpPort=None, TimeOutOption=None, TypeOfConnection=None):
        """Updates interface resource on the server.

        Args
        ----
        - AcceptUnconfiguredChannel (bool): 
        - AllFlowsDelOnStart (bool): 
        - AuxiliaryConnectionTimeout (str(auxReSendFeatureRequest | auxFeatureRequestTerminateConnection)): 
        - BadVersionErrorAction (str(auxReSendHello | auxTerminateConnection)): 
        - EchoInterval (number): 
        - EchoMultiplier (number): 
        - EchoTimeout (number): 
        - EnableEchoTimeOut (bool): 
        - EnableMultipleLogicalSwitch (bool): 
        - EnablePeriodicEcho (bool): 
        - EnablePeriodicLldp (bool): 
        - Enabled (bool): 
        - FeatureRequestTimeout (number): 
        - FeatureRequestTimeoutAction (number): 
        - InstallFlowForLldp (bool): 
        - LldpDestinationMacAddress (str): 
        - ModeOfConnection (str(passive | active | mixed)): 
        - NonHelloMessageStartupAction (str(auxAcceptConnection | auxSendError)): 
        - PeriodicLldpInterval (number): 
        - ProtocolInterfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - SendPortFeatureAtStartup (bool): 
        - TcpPort (number): 
        - TimeOutOption (str(multiplier | timeOutValue)): 
        - TypeOfConnection (str(tcp | tls)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptUnconfiguredChannel=None, AllFlowsDelOnStart=None, AuxiliaryConnectionTimeout=None, BadVersionErrorAction=None, EchoInterval=None, EchoMultiplier=None, EchoTimeout=None, EnableEchoTimeOut=None, EnableMultipleLogicalSwitch=None, EnablePeriodicEcho=None, EnablePeriodicLldp=None, Enabled=None, FeatureRequestTimeout=None, FeatureRequestTimeoutAction=None, InstallFlowForLldp=None, LldpDestinationMacAddress=None, ModeOfConnection=None, NonHelloMessageStartupAction=None, PeriodicLldpInterval=None, ProtocolInterfaces=None, SendPortFeatureAtStartup=None, TcpPort=None, TimeOutOption=None, TypeOfConnection=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AcceptUnconfiguredChannel (bool): 
        - AllFlowsDelOnStart (bool): 
        - AuxiliaryConnectionTimeout (str(auxReSendFeatureRequest | auxFeatureRequestTerminateConnection)): 
        - BadVersionErrorAction (str(auxReSendHello | auxTerminateConnection)): 
        - EchoInterval (number): 
        - EchoMultiplier (number): 
        - EchoTimeout (number): 
        - EnableEchoTimeOut (bool): 
        - EnableMultipleLogicalSwitch (bool): 
        - EnablePeriodicEcho (bool): 
        - EnablePeriodicLldp (bool): 
        - Enabled (bool): 
        - FeatureRequestTimeout (number): 
        - FeatureRequestTimeoutAction (number): 
        - InstallFlowForLldp (bool): 
        - LldpDestinationMacAddress (str): 
        - ModeOfConnection (str(passive | active | mixed)): 
        - NonHelloMessageStartupAction (str(auxAcceptConnection | auxSendError)): 
        - PeriodicLldpInterval (number): 
        - ProtocolInterfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - SendPortFeatureAtStartup (bool): 
        - TcpPort (number): 
        - TimeOutOption (str(multiplier | timeOutValue)): 
        - TypeOfConnection (str(tcp | tls)): 

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptUnconfiguredChannel=None, AllFlowsDelOnStart=None, AuxiliaryConnectionTimeout=None, BadVersionErrorAction=None, EchoInterval=None, EchoMultiplier=None, EchoTimeout=None, EnableEchoTimeOut=None, EnableMultipleLogicalSwitch=None, EnablePeriodicEcho=None, EnablePeriodicLldp=None, Enabled=None, FeatureRequestTimeout=None, FeatureRequestTimeoutAction=None, InstallFlowForLldp=None, LldpDestinationMacAddress=None, ModeOfConnection=None, NonHelloMessageStartupAction=None, PeriodicLldpInterval=None, ProtocolInterfaces=None, SendPortFeatureAtStartup=None, TcpPort=None, TimeOutOption=None, TypeOfConnection=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AcceptUnconfiguredChannel (bool): 
        - AllFlowsDelOnStart (bool): 
        - AuxiliaryConnectionTimeout (str(auxReSendFeatureRequest | auxFeatureRequestTerminateConnection)): 
        - BadVersionErrorAction (str(auxReSendHello | auxTerminateConnection)): 
        - EchoInterval (number): 
        - EchoMultiplier (number): 
        - EchoTimeout (number): 
        - EnableEchoTimeOut (bool): 
        - EnableMultipleLogicalSwitch (bool): 
        - EnablePeriodicEcho (bool): 
        - EnablePeriodicLldp (bool): 
        - Enabled (bool): 
        - FeatureRequestTimeout (number): 
        - FeatureRequestTimeoutAction (number): 
        - InstallFlowForLldp (bool): 
        - LldpDestinationMacAddress (str): 
        - ModeOfConnection (str(passive | active | mixed)): 
        - NonHelloMessageStartupAction (str(auxAcceptConnection | auxSendError)): 
        - PeriodicLldpInterval (number): 
        - ProtocolInterfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): 
        - SendPortFeatureAtStartup (bool): 
        - TcpPort (number): 
        - TimeOutOption (str(multiplier | timeOutValue)): 
        - TypeOfConnection (str(tcp | tls)): 

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
