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


class Atm(Base):
    """
    The Atm class encapsulates a required atm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'atm'
    _SDM_ATT_MAP = {
        'AvailableSpeeds': 'availableSpeeds',
        'C2Expected': 'c2Expected',
        'C2Tx': 'c2Tx',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'CellHeader': 'cellHeader',
        'CosetActive': 'cosetActive',
        'CrcSize': 'crcSize',
        'DataScrambling': 'dataScrambling',
        'EnablePPM': 'enablePPM',
        'FillerCell': 'fillerCell',
        'InterfaceType': 'interfaceType',
        'Loopback': 'loopback',
        'PatternMatching': 'patternMatching',
        'Ppm': 'ppm',
        'ReassemblyTimeout': 'reassemblyTimeout',
        'SelectedSpeeds': 'selectedSpeeds',
        'TransmitClocking': 'transmitClocking',
    }

    def __init__(self, parent):
        super(Atm, self).__init__(parent)

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSpeeds'])

    @property
    def C2Expected(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['C2Expected'])
    @C2Expected.setter
    def C2Expected(self, value):
        self._set_attribute(self._SDM_ATT_MAP['C2Expected'], value)

    @property
    def C2Tx(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['C2Tx'])
    @C2Tx.setter
    def C2Tx(self, value):
        self._set_attribute(self._SDM_ATT_MAP['C2Tx'], value)

    @property
    def CanModifySpeed(self):
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanModifySpeed'])

    @property
    def CanSetMultipleSpeeds(self):
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanSetMultipleSpeeds'])

    @property
    def CellHeader(self):
        """
        Returns
        -------
        - str(nni | uni): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CellHeader'])
    @CellHeader.setter
    def CellHeader(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CellHeader'], value)

    @property
    def CosetActive(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CosetActive'])
    @CosetActive.setter
    def CosetActive(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CosetActive'], value)

    @property
    def CrcSize(self):
        """
        Returns
        -------
        - str(crc16 | crc32): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CrcSize'])
    @CrcSize.setter
    def CrcSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CrcSize'], value)

    @property
    def DataScrambling(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataScrambling'])
    @DataScrambling.setter
    def DataScrambling(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataScrambling'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])
    @EnablePPM.setter
    def EnablePPM(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePPM'], value)

    @property
    def FillerCell(self):
        """
        Returns
        -------
        - str(idle | unassigned): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FillerCell'])
    @FillerCell.setter
    def FillerCell(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FillerCell'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str(oc12 | oc3 | stm1 | stm4): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def PatternMatching(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternMatching'])
    @PatternMatching.setter
    def PatternMatching(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternMatching'], value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ppm'])
    @Ppm.setter
    def Ppm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ppm'], value)

    @property
    def ReassemblyTimeout(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReassemblyTimeout'])
    @ReassemblyTimeout.setter
    def ReassemblyTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReassemblyTimeout'], value)

    @property
    def SelectedSpeeds(self):
        """
        Returns
        -------
        - list(str[]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectedSpeeds'])
    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectedSpeeds'], value)

    @property
    def TransmitClocking(self):
        """
        Returns
        -------
        - str(external | internal | recovered): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitClocking'])
    @TransmitClocking.setter
    def TransmitClocking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmitClocking'], value)

    def update(self, C2Expected=None, C2Tx=None, CellHeader=None, CosetActive=None, CrcSize=None, DataScrambling=None, EnablePPM=None, FillerCell=None, InterfaceType=None, Loopback=None, PatternMatching=None, Ppm=None, ReassemblyTimeout=None, SelectedSpeeds=None, TransmitClocking=None):
        """Updates atm resource on the server.

        Args
        ----
        - C2Expected (number): 
        - C2Tx (number): 
        - CellHeader (str(nni | uni)): 
        - CosetActive (bool): 
        - CrcSize (str(crc16 | crc32)): 
        - DataScrambling (bool): 
        - EnablePPM (bool): 
        - FillerCell (str(idle | unassigned)): 
        - InterfaceType (str(oc12 | oc3 | stm1 | stm4)): 
        - Loopback (bool): 
        - PatternMatching (bool): 
        - Ppm (number): 
        - ReassemblyTimeout (number): 
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TransmitClocking (str(external | internal | recovered)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
