'''_3258.py

ConceptCouplingConnectionPowerFlow
'''


from mastapy.system_model.connections_and_sockets.couplings import _1911
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6092
from mastapy.system_model.analyses_and_results.power_flows import _3269
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptCouplingConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionPowerFlow',)


class ConceptCouplingConnectionPowerFlow(_3269.CouplingConnectionPowerFlow):
    '''ConceptCouplingConnectionPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1911.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1911.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6092.ConceptCouplingConnectionLoadCase':
        '''ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6092.ConceptCouplingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
