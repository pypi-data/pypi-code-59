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


class Instructions(Base):
    """
    The Instructions class encapsulates a list of instructions resources that are managed by the user.
    A list of resources can be retrieved from the server using the Instructions.find() method.
    The list can be managed by using the Instructions.add() and Instructions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'instructions'
    _SDM_ATT_MAP = {
        'Experimenter': 'experimenter',
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'InstructionType': 'instructionType',
        'Metadata': 'metadata',
        'MetadataInHex': 'metadataInHex',
        'MetadataMask': 'metadataMask',
        'MeterId': 'meterId',
        'TableId': 'tableId',
    }

    def __init__(self, parent):
        super(Instructions, self).__init__(parent)

    @property
    def InstructionActions(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionactions_87bfa3f8fbf1803c85e9efa95765f620.InstructionActions): An instance of the InstructionActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionactions_87bfa3f8fbf1803c85e9efa95765f620 import InstructionActions
        return InstructionActions(self)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'], value)

    @property
    def InstructionType(self):
        """
        Returns
        -------
        - str(meter | applyActions | clearActions | experimenter | goToTable | writeActions | writeMetadata): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['InstructionType'])
    @InstructionType.setter
    def InstructionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InstructionType'], value)

    @property
    def Metadata(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metadata'])
    @Metadata.setter
    def Metadata(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metadata'], value)

    @property
    def MetadataInHex(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataInHex'])
    @MetadataInHex.setter
    def MetadataInHex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataInHex'], value)

    @property
    def MetadataMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MetadataMask'])
    @MetadataMask.setter
    def MetadataMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MetadataMask'], value)

    @property
    def MeterId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterId'])
    @MeterId.setter
    def MeterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeterId'], value)

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

    def update(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
        """Updates instructions resource on the server.

        Args
        ----
        - Experimenter (number): 
        - ExperimenterData (str): 
        - ExperimenterDataLength (number): 
        - InstructionType (str(meter | applyActions | clearActions | experimenter | goToTable | writeActions | writeMetadata)): 
        - Metadata (str): 
        - MetadataInHex (str): 
        - MetadataMask (str): 
        - MeterId (number): 
        - TableId (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
        """Adds a new instructions resource on the server and adds it to the container.

        Args
        ----
        - Experimenter (number): 
        - ExperimenterData (str): 
        - ExperimenterDataLength (number): 
        - InstructionType (str(meter | applyActions | clearActions | experimenter | goToTable | writeActions | writeMetadata)): 
        - Metadata (str): 
        - MetadataInHex (str): 
        - MetadataMask (str): 
        - MeterId (number): 
        - TableId (number): 

        Returns
        -------
        - self: This instance with all currently retrieved instructions resources using find and the newly added instructions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained instructions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
        """Finds and retrieves instructions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve instructions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all instructions resources from the server.

        Args
        ----
        - Experimenter (number): 
        - ExperimenterData (str): 
        - ExperimenterDataLength (number): 
        - InstructionType (str(meter | applyActions | clearActions | experimenter | goToTable | writeActions | writeMetadata)): 
        - Metadata (str): 
        - MetadataInHex (str): 
        - MetadataMask (str): 
        - MeterId (number): 
        - TableId (number): 

        Returns
        -------
        - self: This instance with matching instructions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of instructions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the instructions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
