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


class GroupFeatureStatLearnedInformation(Base):
    """
    The GroupFeatureStatLearnedInformation class encapsulates a list of groupFeatureStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the GroupFeatureStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'groupFeatureStatLearnedInformation'
    _SDM_ATT_MAP = {
        'ActionsAll': 'actionsAll',
        'ActionsFastFailOver': 'actionsFastFailOver',
        'ActionsIndirect': 'actionsIndirect',
        'ActionsSelect': 'actionsSelect',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'DatapathId': 'datapathId',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'GroupCapabilities': 'groupCapabilities',
        'GroupType': 'groupType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'MaxGroupsAll': 'maxGroupsAll',
        'MaxGroupsFastFailOver': 'maxGroupsFastFailOver',
        'MaxGroupsIndirect': 'maxGroupsIndirect',
        'MaxGroupsSelect': 'maxGroupsSelect',
        'NegotiatedVersion': 'negotiatedVersion',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(GroupFeatureStatLearnedInformation, self).__init__(parent)

    @property
    def ActionsAll(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsAll'])

    @property
    def ActionsFastFailOver(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsFastFailOver'])

    @property
    def ActionsIndirect(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsIndirect'])

    @property
    def ActionsSelect(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionsSelect'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def DatapathId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathId'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def GroupCapabilities(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupCapabilities'])

    @property
    def GroupType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MaxGroupsAll(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxGroupsAll'])

    @property
    def MaxGroupsFastFailOver(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxGroupsFastFailOver'])

    @property
    def MaxGroupsIndirect(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxGroupsIndirect'])

    @property
    def MaxGroupsSelect(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxGroupsSelect'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, ActionsAll=None, ActionsFastFailOver=None, ActionsIndirect=None, ActionsSelect=None, DataPathIdAsHex=None, DatapathId=None, ErrorCode=None, ErrorType=None, GroupCapabilities=None, GroupType=None, Latency=None, LocalIp=None, MaxGroupsAll=None, MaxGroupsFastFailOver=None, MaxGroupsIndirect=None, MaxGroupsSelect=None, NegotiatedVersion=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves groupFeatureStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupFeatureStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupFeatureStatLearnedInformation resources from the server.

        Args
        ----
        - ActionsAll (str): 
        - ActionsFastFailOver (str): 
        - ActionsIndirect (str): 
        - ActionsSelect (str): 
        - DataPathIdAsHex (str): 
        - DatapathId (str): 
        - ErrorCode (str): 
        - ErrorType (str): 
        - GroupCapabilities (str): 
        - GroupType (str): 
        - Latency (number): 
        - LocalIp (str): 
        - MaxGroupsAll (number): 
        - MaxGroupsFastFailOver (number): 
        - MaxGroupsIndirect (number): 
        - MaxGroupsSelect (number): 
        - NegotiatedVersion (str): 
        - RemoteIp (str): 
        - ReplyState (str): 

        Returns
        -------
        - self: This instance with matching groupFeatureStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupFeatureStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupFeatureStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
