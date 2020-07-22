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


class RBridges(Base):
    """
    The RBridges class encapsulates a list of rBridges resources that are managed by the system.
    A list of resources can be retrieved from the server using the RBridges.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rBridges'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'EnableCommonMtId': 'enableCommonMtId',
        'ExtendedCircuitId': 'extendedCircuitId',
        'GraphId': 'graphId',
        'HostName': 'hostName',
        'LinkMetric': 'linkMetric',
        'MtId': 'mtId',
        'PrimaryFtag': 'primaryFtag',
        'Priority': 'priority',
        'Role': 'role',
        'SecondaryFtag': 'secondaryFtag',
        'SequenceNumber': 'sequenceNumber',
        'SwitchId': 'switchId',
        'SystemId': 'systemId',
    }

    def __init__(self, parent):
        super(RBridges, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def EnableCommonMtId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCommonMtId'])

    @property
    def ExtendedCircuitId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCircuitId'])

    @property
    def GraphId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GraphId'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])

    @property
    def MtId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MtId'])

    @property
    def PrimaryFtag(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrimaryFtag'])

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])

    @property
    def Role(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])

    @property
    def SecondaryFtag(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SecondaryFtag'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def SwitchId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchId'])

    @property
    def SystemId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemId'])

    def find(self, Age=None, EnableCommonMtId=None, ExtendedCircuitId=None, GraphId=None, HostName=None, LinkMetric=None, MtId=None, PrimaryFtag=None, Priority=None, Role=None, SecondaryFtag=None, SequenceNumber=None, SwitchId=None, SystemId=None):
        """Finds and retrieves rBridges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rBridges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rBridges resources from the server.

        Args
        ----
        - Age (number): 
        - EnableCommonMtId (bool): 
        - ExtendedCircuitId (number): 
        - GraphId (number): 
        - HostName (str): 
        - LinkMetric (number): 
        - MtId (number): 
        - PrimaryFtag (number): 
        - Priority (number): 
        - Role (str): 
        - SecondaryFtag (number): 
        - SequenceNumber (number): 
        - SwitchId (number): 
        - SystemId (str): 

        Returns
        -------
        - self: This instance with matching rBridges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rBridges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rBridges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
