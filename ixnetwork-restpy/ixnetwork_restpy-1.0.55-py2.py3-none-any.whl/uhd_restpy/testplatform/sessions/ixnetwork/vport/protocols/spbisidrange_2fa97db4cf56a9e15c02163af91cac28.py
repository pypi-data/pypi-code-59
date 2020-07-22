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


class SpbIsIdRange(Base):
    """
    The SpbIsIdRange class encapsulates a list of spbIsIdRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbIsIdRange.find() method.
    The list can be managed by using the SpbIsIdRange.add() and SpbIsIdRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'spbIsIdRange'
    _SDM_ATT_MAP = {
        'CMacAddressCount': 'cMacAddressCount',
        'CMacAddressStep': 'cMacAddressStep',
        'CVlan': 'cVlan',
        'Enabled': 'enabled',
        'ISid': 'iSid',
        'ITagEthernetType': 'iTagEthernetType',
        'RBit': 'rBit',
        'SVlan': 'sVlan',
        'StartCmacAddress': 'startCmacAddress',
        'TBit': 'tBit',
        'TrafficDestMacAddress': 'trafficDestMacAddress',
        'TransmissionType': 'transmissionType',
        'VlanType': 'vlanType',
    }

    def __init__(self, parent):
        super(SpbIsIdRange, self).__init__(parent)

    @property
    def CMacAddressCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressCount'])
    @CMacAddressCount.setter
    def CMacAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressCount'], value)

    @property
    def CMacAddressStep(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressStep'])
    @CMacAddressStep.setter
    def CMacAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressStep'], value)

    @property
    def CVlan(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])
    @CVlan.setter
    def CVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlan'], value)

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
    def ISid(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ISid'])
    @ISid.setter
    def ISid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ISid'], value)

    @property
    def ITagEthernetType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagEthernetType'])

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RBit'])
    @RBit.setter
    def RBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RBit'], value)

    @property
    def SVlan(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])
    @SVlan.setter
    def SVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlan'], value)

    @property
    def StartCmacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartCmacAddress'])
    @StartCmacAddress.setter
    def StartCmacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartCmacAddress'], value)

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])
    @TBit.setter
    def TBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TBit'], value)

    @property
    def TrafficDestMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficDestMacAddress'])
    @TrafficDestMacAddress.setter
    def TrafficDestMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficDestMacAddress'], value)

    @property
    def TransmissionType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmissionType'])
    @TransmissionType.setter
    def TransmissionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmissionType'], value)

    @property
    def VlanType(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanType'])
    @VlanType.setter
    def VlanType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanType'], value)

    def update(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Updates spbIsIdRange resource on the server.

        Args
        ----
        - CMacAddressCount (number): 
        - CMacAddressStep (str): 
        - CVlan (number): 
        - Enabled (bool): 
        - ISid (number): 
        - RBit (bool): 
        - SVlan (number): 
        - StartCmacAddress (str): 
        - TBit (bool): 
        - TrafficDestMacAddress (str): 
        - TransmissionType (number): 
        - VlanType (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Adds a new spbIsIdRange resource on the server and adds it to the container.

        Args
        ----
        - CMacAddressCount (number): 
        - CMacAddressStep (str): 
        - CVlan (number): 
        - Enabled (bool): 
        - ISid (number): 
        - RBit (bool): 
        - SVlan (number): 
        - StartCmacAddress (str): 
        - TBit (bool): 
        - TrafficDestMacAddress (str): 
        - TransmissionType (number): 
        - VlanType (number): 

        Returns
        -------
        - self: This instance with all currently retrieved spbIsIdRange resources using find and the newly added spbIsIdRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbIsIdRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CMacAddressCount=None, CMacAddressStep=None, CVlan=None, Enabled=None, ISid=None, ITagEthernetType=None, RBit=None, SVlan=None, StartCmacAddress=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Finds and retrieves spbIsIdRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbIsIdRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbIsIdRange resources from the server.

        Args
        ----
        - CMacAddressCount (number): 
        - CMacAddressStep (str): 
        - CVlan (number): 
        - Enabled (bool): 
        - ISid (number): 
        - ITagEthernetType (number): 
        - RBit (bool): 
        - SVlan (number): 
        - StartCmacAddress (str): 
        - TBit (bool): 
        - TrafficDestMacAddress (str): 
        - TransmissionType (number): 
        - VlanType (number): 

        Returns
        -------
        - self: This instance with matching spbIsIdRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbIsIdRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbIsIdRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
