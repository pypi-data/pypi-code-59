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


class SenderRange(Base):
    """
    The SenderRange class encapsulates a list of senderRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SenderRange.find() method.
    The list can be managed by using the SenderRange.add() and SenderRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'senderRange'
    _SDM_ATT_MAP = {
        'AutoGenerateSessionName': 'autoGenerateSessionName',
        'BackupLspIdPoolStart': 'backupLspIdPoolStart',
        'Bandwidth': 'bandwidth',
        'BandwidthProtectionDesired': 'bandwidthProtectionDesired',
        'EnableBfdMpls': 'enableBfdMpls',
        'EnableFastReroute': 'enableFastReroute',
        'EnableLspPing': 'enableLspPing',
        'EnablePathReoptimization': 'enablePathReoptimization',
        'EnablePeriodicReEvaluationRequest': 'enablePeriodicReEvaluationRequest',
        'EnableResourceAffinities': 'enableResourceAffinities',
        'Enabled': 'enabled',
        'ExcludeAny': 'excludeAny',
        'FastRerouteBandwidth': 'fastRerouteBandwidth',
        'FastRerouteDetour': 'fastRerouteDetour',
        'FastRerouteExcludeAny': 'fastRerouteExcludeAny',
        'FastRerouteFacilityBackupDesired': 'fastRerouteFacilityBackupDesired',
        'FastRerouteHoldingPriority': 'fastRerouteHoldingPriority',
        'FastRerouteHopLimit': 'fastRerouteHopLimit',
        'FastRerouteIncludeAll': 'fastRerouteIncludeAll',
        'FastRerouteIncludeAny': 'fastRerouteIncludeAny',
        'FastRerouteOne2OneBackupDesired': 'fastRerouteOne2OneBackupDesired',
        'FastRerouteSendDetour': 'fastRerouteSendDetour',
        'FastRerouteSetupPriority': 'fastRerouteSetupPriority',
        'HoldingPriority': 'holdingPriority',
        'IncludeAll': 'includeAll',
        'IncludeAny': 'includeAny',
        'IpCount': 'ipCount',
        'IpStart': 'ipStart',
        'LabelRecordingDesired': 'labelRecordingDesired',
        'LocalProtectionDesired': 'localProtectionDesired',
        'LspIdCount': 'lspIdCount',
        'LspIdStart': 'lspIdStart',
        'MaximumPacketSize': 'maximumPacketSize',
        'MinimumPolicedUnit': 'minimumPolicedUnit',
        'NodeProtectionDesired': 'nodeProtectionDesired',
        'PathTearTlv': 'pathTearTlv',
        'PathTlv': 'pathTlv',
        'PeakDataRate': 'peakDataRate',
        'ReEvaluationRequestInterval': 'reEvaluationRequestInterval',
        'RefreshInterval': 'refreshInterval',
        'SeStyleDesired': 'seStyleDesired',
        'SessionName': 'sessionName',
        'SetupPriority': 'setupPriority',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TokenBucketRate': 'tokenBucketRate',
        'TokenBucketSize': 'tokenBucketSize',
    }

    def __init__(self, parent):
        super(SenderRange, self).__init__(parent)

    @property
    def TunnelHeadToLeaf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtoleaf_e69a9a69601e0735ed9794ff412c72e6.TunnelHeadToLeaf): An instance of the TunnelHeadToLeaf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtoleaf_e69a9a69601e0735ed9794ff412c72e6 import TunnelHeadToLeaf
        return TunnelHeadToLeaf(self)

    @property
    def TunnelHeadTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtrafficendpoint_399e6e14fa13954b413c4572ebd3725e.TunnelHeadTrafficEndPoint): An instance of the TunnelHeadTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelheadtrafficendpoint_399e6e14fa13954b413c4572ebd3725e import TunnelHeadTrafficEndPoint
        return TunnelHeadTrafficEndPoint(self)

    @property
    def AutoGenerateSessionName(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoGenerateSessionName'])
    @AutoGenerateSessionName.setter
    def AutoGenerateSessionName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoGenerateSessionName'], value)

    @property
    def BackupLspIdPoolStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackupLspIdPoolStart'])
    @BackupLspIdPoolStart.setter
    def BackupLspIdPoolStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackupLspIdPoolStart'], value)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Bandwidth'])
    @Bandwidth.setter
    def Bandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Bandwidth'], value)

    @property
    def BandwidthProtectionDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BandwidthProtectionDesired'])
    @BandwidthProtectionDesired.setter
    def BandwidthProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BandwidthProtectionDesired'], value)

    @property
    def EnableBfdMpls(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdMpls'])
    @EnableBfdMpls.setter
    def EnableBfdMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdMpls'], value)

    @property
    def EnableFastReroute(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFastReroute'])
    @EnableFastReroute.setter
    def EnableFastReroute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFastReroute'], value)

    @property
    def EnableLspPing(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLspPing'])
    @EnableLspPing.setter
    def EnableLspPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLspPing'], value)

    @property
    def EnablePathReoptimization(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePathReoptimization'])
    @EnablePathReoptimization.setter
    def EnablePathReoptimization(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePathReoptimization'], value)

    @property
    def EnablePeriodicReEvaluationRequest(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicReEvaluationRequest'])
    @EnablePeriodicReEvaluationRequest.setter
    def EnablePeriodicReEvaluationRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeriodicReEvaluationRequest'], value)

    @property
    def EnableResourceAffinities(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableResourceAffinities'])
    @EnableResourceAffinities.setter
    def EnableResourceAffinities(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableResourceAffinities'], value)

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
    def ExcludeAny(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExcludeAny'])
    @ExcludeAny.setter
    def ExcludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExcludeAny'], value)

    @property
    def FastRerouteBandwidth(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteBandwidth'])
    @FastRerouteBandwidth.setter
    def FastRerouteBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteBandwidth'], value)

    @property
    def FastRerouteDetour(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteDetour'])
    @FastRerouteDetour.setter
    def FastRerouteDetour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteDetour'], value)

    @property
    def FastRerouteExcludeAny(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteExcludeAny'])
    @FastRerouteExcludeAny.setter
    def FastRerouteExcludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteExcludeAny'], value)

    @property
    def FastRerouteFacilityBackupDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteFacilityBackupDesired'])
    @FastRerouteFacilityBackupDesired.setter
    def FastRerouteFacilityBackupDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteFacilityBackupDesired'], value)

    @property
    def FastRerouteHoldingPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteHoldingPriority'])
    @FastRerouteHoldingPriority.setter
    def FastRerouteHoldingPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteHoldingPriority'], value)

    @property
    def FastRerouteHopLimit(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteHopLimit'])
    @FastRerouteHopLimit.setter
    def FastRerouteHopLimit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteHopLimit'], value)

    @property
    def FastRerouteIncludeAll(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAll'])
    @FastRerouteIncludeAll.setter
    def FastRerouteIncludeAll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAll'], value)

    @property
    def FastRerouteIncludeAny(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAny'])
    @FastRerouteIncludeAny.setter
    def FastRerouteIncludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteIncludeAny'], value)

    @property
    def FastRerouteOne2OneBackupDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteOne2OneBackupDesired'])
    @FastRerouteOne2OneBackupDesired.setter
    def FastRerouteOne2OneBackupDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteOne2OneBackupDesired'], value)

    @property
    def FastRerouteSendDetour(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteSendDetour'])
    @FastRerouteSendDetour.setter
    def FastRerouteSendDetour(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteSendDetour'], value)

    @property
    def FastRerouteSetupPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastRerouteSetupPriority'])
    @FastRerouteSetupPriority.setter
    def FastRerouteSetupPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastRerouteSetupPriority'], value)

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldingPriority'])
    @HoldingPriority.setter
    def HoldingPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HoldingPriority'], value)

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeAll'])
    @IncludeAll.setter
    def IncludeAll(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeAll'], value)

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeAny'])
    @IncludeAny.setter
    def IncludeAny(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeAny'], value)

    @property
    def IpCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpCount'])
    @IpCount.setter
    def IpCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpCount'], value)

    @property
    def IpStart(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStart'])
    @IpStart.setter
    def IpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStart'], value)

    @property
    def LabelRecordingDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelRecordingDesired'])
    @LabelRecordingDesired.setter
    def LabelRecordingDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelRecordingDesired'], value)

    @property
    def LocalProtectionDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalProtectionDesired'])
    @LocalProtectionDesired.setter
    def LocalProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalProtectionDesired'], value)

    @property
    def LspIdCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspIdCount'])
    @LspIdCount.setter
    def LspIdCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspIdCount'], value)

    @property
    def LspIdStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspIdStart'])
    @LspIdStart.setter
    def LspIdStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspIdStart'], value)

    @property
    def MaximumPacketSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumPacketSize'])
    @MaximumPacketSize.setter
    def MaximumPacketSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumPacketSize'], value)

    @property
    def MinimumPolicedUnit(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinimumPolicedUnit'])
    @MinimumPolicedUnit.setter
    def MinimumPolicedUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinimumPolicedUnit'], value)

    @property
    def NodeProtectionDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NodeProtectionDesired'])
    @NodeProtectionDesired.setter
    def NodeProtectionDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NodeProtectionDesired'], value)

    @property
    def PathTearTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathTearTlv'])
    @PathTearTlv.setter
    def PathTearTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathTearTlv'], value)

    @property
    def PathTlv(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:str)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathTlv'])
    @PathTlv.setter
    def PathTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathTlv'], value)

    @property
    def PeakDataRate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeakDataRate'])
    @PeakDataRate.setter
    def PeakDataRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeakDataRate'], value)

    @property
    def ReEvaluationRequestInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReEvaluationRequestInterval'])
    @ReEvaluationRequestInterval.setter
    def ReEvaluationRequestInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReEvaluationRequestInterval'], value)

    @property
    def RefreshInterval(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RefreshInterval'])
    @RefreshInterval.setter
    def RefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RefreshInterval'], value)

    @property
    def SeStyleDesired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeStyleDesired'])
    @SeStyleDesired.setter
    def SeStyleDesired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SeStyleDesired'], value)

    @property
    def SessionName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionName'])
    @SessionName.setter
    def SessionName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SessionName'], value)

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupPriority'])
    @SetupPriority.setter
    def SetupPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupPriority'], value)

    @property
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'])
    @TimeoutMultiplier.setter
    def TimeoutMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeoutMultiplier'], value)

    @property
    def TokenBucketRate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TokenBucketRate'])
    @TokenBucketRate.setter
    def TokenBucketRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TokenBucketRate'], value)

    @property
    def TokenBucketSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TokenBucketSize'])
    @TokenBucketSize.setter
    def TokenBucketSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TokenBucketSize'], value)

    def update(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Updates senderRange resource on the server.

        Args
        ----
        - AutoGenerateSessionName (bool): 
        - BackupLspIdPoolStart (number): 
        - Bandwidth (str): 
        - BandwidthProtectionDesired (bool): 
        - EnableBfdMpls (bool): 
        - EnableFastReroute (bool): 
        - EnableLspPing (bool): 
        - EnablePathReoptimization (bool): 
        - EnablePeriodicReEvaluationRequest (bool): 
        - EnableResourceAffinities (bool): 
        - Enabled (bool): 
        - ExcludeAny (number): 
        - FastRerouteBandwidth (str): 
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): 
        - FastRerouteExcludeAny (number): 
        - FastRerouteFacilityBackupDesired (bool): 
        - FastRerouteHoldingPriority (number): 
        - FastRerouteHopLimit (number): 
        - FastRerouteIncludeAll (number): 
        - FastRerouteIncludeAny (number): 
        - FastRerouteOne2OneBackupDesired (bool): 
        - FastRerouteSendDetour (bool): 
        - FastRerouteSetupPriority (number): 
        - HoldingPriority (number): 
        - IncludeAll (number): 
        - IncludeAny (number): 
        - IpCount (number): 
        - IpStart (str): 
        - LabelRecordingDesired (bool): 
        - LocalProtectionDesired (bool): 
        - LspIdCount (number): 
        - LspIdStart (number): 
        - MaximumPacketSize (number): 
        - MinimumPolicedUnit (number): 
        - NodeProtectionDesired (bool): 
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PeakDataRate (number): 
        - ReEvaluationRequestInterval (number): 
        - RefreshInterval (number): 
        - SeStyleDesired (bool): 
        - SessionName (str): 
        - SetupPriority (number): 
        - TimeoutMultiplier (number): 
        - TokenBucketRate (number): 
        - TokenBucketSize (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Adds a new senderRange resource on the server and adds it to the container.

        Args
        ----
        - AutoGenerateSessionName (bool): 
        - BackupLspIdPoolStart (number): 
        - Bandwidth (str): 
        - BandwidthProtectionDesired (bool): 
        - EnableBfdMpls (bool): 
        - EnableFastReroute (bool): 
        - EnableLspPing (bool): 
        - EnablePathReoptimization (bool): 
        - EnablePeriodicReEvaluationRequest (bool): 
        - EnableResourceAffinities (bool): 
        - Enabled (bool): 
        - ExcludeAny (number): 
        - FastRerouteBandwidth (str): 
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): 
        - FastRerouteExcludeAny (number): 
        - FastRerouteFacilityBackupDesired (bool): 
        - FastRerouteHoldingPriority (number): 
        - FastRerouteHopLimit (number): 
        - FastRerouteIncludeAll (number): 
        - FastRerouteIncludeAny (number): 
        - FastRerouteOne2OneBackupDesired (bool): 
        - FastRerouteSendDetour (bool): 
        - FastRerouteSetupPriority (number): 
        - HoldingPriority (number): 
        - IncludeAll (number): 
        - IncludeAny (number): 
        - IpCount (number): 
        - IpStart (str): 
        - LabelRecordingDesired (bool): 
        - LocalProtectionDesired (bool): 
        - LspIdCount (number): 
        - LspIdStart (number): 
        - MaximumPacketSize (number): 
        - MinimumPolicedUnit (number): 
        - NodeProtectionDesired (bool): 
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PeakDataRate (number): 
        - ReEvaluationRequestInterval (number): 
        - RefreshInterval (number): 
        - SeStyleDesired (bool): 
        - SessionName (str): 
        - SetupPriority (number): 
        - TimeoutMultiplier (number): 
        - TokenBucketRate (number): 
        - TokenBucketSize (number): 

        Returns
        -------
        - self: This instance with all currently retrieved senderRange resources using find and the newly added senderRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained senderRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoGenerateSessionName=None, BackupLspIdPoolStart=None, Bandwidth=None, BandwidthProtectionDesired=None, EnableBfdMpls=None, EnableFastReroute=None, EnableLspPing=None, EnablePathReoptimization=None, EnablePeriodicReEvaluationRequest=None, EnableResourceAffinities=None, Enabled=None, ExcludeAny=None, FastRerouteBandwidth=None, FastRerouteDetour=None, FastRerouteExcludeAny=None, FastRerouteFacilityBackupDesired=None, FastRerouteHoldingPriority=None, FastRerouteHopLimit=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteOne2OneBackupDesired=None, FastRerouteSendDetour=None, FastRerouteSetupPriority=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IpCount=None, IpStart=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspIdCount=None, LspIdStart=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, PathTearTlv=None, PathTlv=None, PeakDataRate=None, ReEvaluationRequestInterval=None, RefreshInterval=None, SeStyleDesired=None, SessionName=None, SetupPriority=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None):
        """Finds and retrieves senderRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve senderRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all senderRange resources from the server.

        Args
        ----
        - AutoGenerateSessionName (bool): 
        - BackupLspIdPoolStart (number): 
        - Bandwidth (str): 
        - BandwidthProtectionDesired (bool): 
        - EnableBfdMpls (bool): 
        - EnableFastReroute (bool): 
        - EnableLspPing (bool): 
        - EnablePathReoptimization (bool): 
        - EnablePeriodicReEvaluationRequest (bool): 
        - EnableResourceAffinities (bool): 
        - Enabled (bool): 
        - ExcludeAny (number): 
        - FastRerouteBandwidth (str): 
        - FastRerouteDetour (list(dict(arg1:str,arg2:str))): 
        - FastRerouteExcludeAny (number): 
        - FastRerouteFacilityBackupDesired (bool): 
        - FastRerouteHoldingPriority (number): 
        - FastRerouteHopLimit (number): 
        - FastRerouteIncludeAll (number): 
        - FastRerouteIncludeAny (number): 
        - FastRerouteOne2OneBackupDesired (bool): 
        - FastRerouteSendDetour (bool): 
        - FastRerouteSetupPriority (number): 
        - HoldingPriority (number): 
        - IncludeAll (number): 
        - IncludeAny (number): 
        - IpCount (number): 
        - IpStart (str): 
        - LabelRecordingDesired (bool): 
        - LocalProtectionDesired (bool): 
        - LspIdCount (number): 
        - LspIdStart (number): 
        - MaximumPacketSize (number): 
        - MinimumPolicedUnit (number): 
        - NodeProtectionDesired (bool): 
        - PathTearTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PathTlv (list(dict(arg1:number,arg2:number,arg3:str))): 
        - PeakDataRate (number): 
        - ReEvaluationRequestInterval (number): 
        - RefreshInterval (number): 
        - SeStyleDesired (bool): 
        - SessionName (str): 
        - SetupPriority (number): 
        - TimeoutMultiplier (number): 
        - TokenBucketRate (number): 
        - TokenBucketSize (number): 

        Returns
        -------
        - self: This instance with matching senderRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of senderRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the senderRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DoMakeBeforeBreak(self):
        """Executes the doMakeBeforeBreak operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('doMakeBeforeBreak', payload=payload, response_object=None)

    def SendReEvaluationRequest(self):
        """Executes the sendReEvaluationRequest operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendReEvaluationRequest', payload=payload, response_object=None)
