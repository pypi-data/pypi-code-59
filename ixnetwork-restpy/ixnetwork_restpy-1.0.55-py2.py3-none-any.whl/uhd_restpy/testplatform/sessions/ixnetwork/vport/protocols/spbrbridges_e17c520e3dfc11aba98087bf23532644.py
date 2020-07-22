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


class SpbRbridges(Base):
    """
    The SpbRbridges class encapsulates a list of spbRbridges resources that are managed by the system.
    A list of resources can be retrieved from the server using the SpbRbridges.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'spbRbridges'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'AuxillaryMcidConfigName': 'auxillaryMcidConfigName',
        'BaseVid': 'baseVid',
        'BridgeMacAddress': 'bridgeMacAddress',
        'BridgePriority': 'bridgePriority',
        'EctAlgorithm': 'ectAlgorithm',
        'HostName': 'hostName',
        'IsId': 'isId',
        'LinkMetric': 'linkMetric',
        'MBit': 'mBit',
        'McidConfigName': 'mcidConfigName',
        'RBit': 'rBit',
        'SequenceNumber': 'sequenceNumber',
        'SystemId': 'systemId',
        'TBit': 'tBit',
        'UseFlagBit': 'useFlagBit',
    }

    def __init__(self, parent):
        super(SpbRbridges, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def AuxillaryMcidConfigName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuxillaryMcidConfigName'])

    @property
    def BaseVid(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseVid'])

    @property
    def BridgeMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeMacAddress'])

    @property
    def BridgePriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgePriority'])

    @property
    def EctAlgorithm(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EctAlgorithm'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def IsId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsId'])

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])

    @property
    def MBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MBit'])

    @property
    def McidConfigName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['McidConfigName'])

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RBit'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def SystemId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemId'])

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])

    @property
    def UseFlagBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseFlagBit'])

    def find(self, Age=None, AuxillaryMcidConfigName=None, BaseVid=None, BridgeMacAddress=None, BridgePriority=None, EctAlgorithm=None, HostName=None, IsId=None, LinkMetric=None, MBit=None, McidConfigName=None, RBit=None, SequenceNumber=None, SystemId=None, TBit=None, UseFlagBit=None):
        """Finds and retrieves spbRbridges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbRbridges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbRbridges resources from the server.

        Args
        ----
        - Age (number): 
        - AuxillaryMcidConfigName (str): 
        - BaseVid (number): 
        - BridgeMacAddress (str): 
        - BridgePriority (number): 
        - EctAlgorithm (number): 
        - HostName (str): 
        - IsId (number): 
        - LinkMetric (number): 
        - MBit (bool): 
        - McidConfigName (str): 
        - RBit (bool): 
        - SequenceNumber (number): 
        - SystemId (str): 
        - TBit (bool): 
        - UseFlagBit (bool): 

        Returns
        -------
        - self: This instance with matching spbRbridges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbRbridges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbRbridges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
