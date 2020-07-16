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


class CMacRange(Base):
    """
    The CMacRange class encapsulates a list of cMacRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CMacRange.find() method.
    The list can be managed by using the CMacRange.add() and CMacRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'cMacRange'
    _SDM_ATT_MAP = {
        'CmacPrefixLength': 'cmacPrefixLength',
        'CvlanId': 'cvlanId',
        'CvlanPriority': 'cvlanPriority',
        'CvlanTpId': 'cvlanTpId',
        'EnableCvlan': 'enableCvlan',
        'EnableSecondLabel': 'enableSecondLabel',
        'EnableSvlan': 'enableSvlan',
        'Enabled': 'enabled',
        'FirstLabelStart': 'firstLabelStart',
        'LabelMode': 'labelMode',
        'LabelStep': 'labelStep',
        'NoOfCmacs': 'noOfCmacs',
        'SecondLabelStart': 'secondLabelStart',
        'StartCmacPrefix': 'startCmacPrefix',
        'SvlanId': 'svlanId',
        'SvlanPriority': 'svlanPriority',
        'SvlanTpId': 'svlanTpId',
        'UseSameSequenceNumber': 'useSameSequenceNumber',
    }

    def __init__(self, parent):
        super(CMacRange, self).__init__(parent)

    @property
    def CMacMappedIp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacmappedip_a8bca85601ce75e7339ae5e16dd43dd6.CMacMappedIp): An instance of the CMacMappedIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacmappedip_a8bca85601ce75e7339ae5e16dd43dd6 import CMacMappedIp
        return CMacMappedIp(self)

    @property
    def CmacRouteAttributes(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacrouteattributes_7c8e2aaaa1bf92f1ad81525344771986.CmacRouteAttributes): An instance of the CmacRouteAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacrouteattributes_7c8e2aaaa1bf92f1ad81525344771986 import CmacRouteAttributes
        return CmacRouteAttributes(self)._select()

    @property
    def CmacPrefixLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CmacPrefixLength'])
    @CmacPrefixLength.setter
    def CmacPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CmacPrefixLength'], value)

    @property
    def CvlanId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanId'])
    @CvlanId.setter
    def CvlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanId'], value)

    @property
    def CvlanPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanPriority'])
    @CvlanPriority.setter
    def CvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanPriority'], value)

    @property
    def CvlanTpId(self):
        """
        Returns
        -------
        - str(0x8100 | 0x9100 | 0x9200 | 0x88A8): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanTpId'])
    @CvlanTpId.setter
    def CvlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanTpId'], value)

    @property
    def EnableCvlan(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCvlan'])
    @EnableCvlan.setter
    def EnableCvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCvlan'], value)

    @property
    def EnableSecondLabel(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSecondLabel'])
    @EnableSecondLabel.setter
    def EnableSecondLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSecondLabel'], value)

    @property
    def EnableSvlan(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSvlan'])
    @EnableSvlan.setter
    def EnableSvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSvlan'], value)

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
    def FirstLabelStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstLabelStart'])
    @FirstLabelStart.setter
    def FirstLabelStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstLabelStart'], value)

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - str(fixed | increment): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelMode'])
    @LabelMode.setter
    def LabelMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelMode'], value)

    @property
    def LabelStep(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelStep'])
    @LabelStep.setter
    def LabelStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelStep'], value)

    @property
    def NoOfCmacs(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfCmacs'])
    @NoOfCmacs.setter
    def NoOfCmacs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfCmacs'], value)

    @property
    def SecondLabelStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SecondLabelStart'])
    @SecondLabelStart.setter
    def SecondLabelStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SecondLabelStart'], value)

    @property
    def StartCmacPrefix(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartCmacPrefix'])
    @StartCmacPrefix.setter
    def StartCmacPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartCmacPrefix'], value)

    @property
    def SvlanId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanId'])
    @SvlanId.setter
    def SvlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanId'], value)

    @property
    def SvlanPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanPriority'])
    @SvlanPriority.setter
    def SvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanPriority'], value)

    @property
    def SvlanTpId(self):
        """
        Returns
        -------
        - str(0x8100 | 0x9100 | 0x9200 | 0x88A8): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanTpId'])
    @SvlanTpId.setter
    def SvlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanTpId'], value)

    @property
    def UseSameSequenceNumber(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber'])
    @UseSameSequenceNumber.setter
    def UseSameSequenceNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseSameSequenceNumber'], value)

    def update(self, CmacPrefixLength=None, CvlanId=None, CvlanPriority=None, CvlanTpId=None, EnableCvlan=None, EnableSecondLabel=None, EnableSvlan=None, Enabled=None, FirstLabelStart=None, LabelMode=None, LabelStep=None, NoOfCmacs=None, SecondLabelStart=None, StartCmacPrefix=None, SvlanId=None, SvlanPriority=None, SvlanTpId=None, UseSameSequenceNumber=None):
        """Updates cMacRange resource on the server.

        Args
        ----
        - CmacPrefixLength (number): 
        - CvlanId (number): 
        - CvlanPriority (number): 
        - CvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - EnableCvlan (bool): 
        - EnableSecondLabel (bool): 
        - EnableSvlan (bool): 
        - Enabled (bool): 
        - FirstLabelStart (number): 
        - LabelMode (str(fixed | increment)): 
        - LabelStep (number): 
        - NoOfCmacs (number): 
        - SecondLabelStart (number): 
        - StartCmacPrefix (str): 
        - SvlanId (number): 
        - SvlanPriority (number): 
        - SvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - UseSameSequenceNumber (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CmacPrefixLength=None, CvlanId=None, CvlanPriority=None, CvlanTpId=None, EnableCvlan=None, EnableSecondLabel=None, EnableSvlan=None, Enabled=None, FirstLabelStart=None, LabelMode=None, LabelStep=None, NoOfCmacs=None, SecondLabelStart=None, StartCmacPrefix=None, SvlanId=None, SvlanPriority=None, SvlanTpId=None, UseSameSequenceNumber=None):
        """Adds a new cMacRange resource on the server and adds it to the container.

        Args
        ----
        - CmacPrefixLength (number): 
        - CvlanId (number): 
        - CvlanPriority (number): 
        - CvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - EnableCvlan (bool): 
        - EnableSecondLabel (bool): 
        - EnableSvlan (bool): 
        - Enabled (bool): 
        - FirstLabelStart (number): 
        - LabelMode (str(fixed | increment)): 
        - LabelStep (number): 
        - NoOfCmacs (number): 
        - SecondLabelStart (number): 
        - StartCmacPrefix (str): 
        - SvlanId (number): 
        - SvlanPriority (number): 
        - SvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - UseSameSequenceNumber (bool): 

        Returns
        -------
        - self: This instance with all currently retrieved cMacRange resources using find and the newly added cMacRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained cMacRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CmacPrefixLength=None, CvlanId=None, CvlanPriority=None, CvlanTpId=None, EnableCvlan=None, EnableSecondLabel=None, EnableSvlan=None, Enabled=None, FirstLabelStart=None, LabelMode=None, LabelStep=None, NoOfCmacs=None, SecondLabelStart=None, StartCmacPrefix=None, SvlanId=None, SvlanPriority=None, SvlanTpId=None, UseSameSequenceNumber=None):
        """Finds and retrieves cMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cMacRange resources from the server.

        Args
        ----
        - CmacPrefixLength (number): 
        - CvlanId (number): 
        - CvlanPriority (number): 
        - CvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - EnableCvlan (bool): 
        - EnableSecondLabel (bool): 
        - EnableSvlan (bool): 
        - Enabled (bool): 
        - FirstLabelStart (number): 
        - LabelMode (str(fixed | increment)): 
        - LabelStep (number): 
        - NoOfCmacs (number): 
        - SecondLabelStart (number): 
        - StartCmacPrefix (str): 
        - SvlanId (number): 
        - SvlanPriority (number): 
        - SvlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): 
        - UseSameSequenceNumber (bool): 

        Returns
        -------
        - self: This instance with matching cMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cMacRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ReadvertiseCmac(self):
        """Executes the readvertiseCmac operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('readvertiseCmac', payload=payload, response_object=None)
