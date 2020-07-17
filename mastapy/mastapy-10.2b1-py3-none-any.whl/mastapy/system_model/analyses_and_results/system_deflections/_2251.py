'''_2251.py

ConceptCouplingHalfSystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2134
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6093
from mastapy.system_model.analyses_and_results.power_flows import _3259
from mastapy.system_model.analyses_and_results.system_deflections import _2263
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptCouplingHalfSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfSystemDeflection',)


class ConceptCouplingHalfSystemDeflection(_2263.CouplingHalfSystemDeflection):
    '''ConceptCouplingHalfSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2134.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2134.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6093.ConceptCouplingHalfLoadCase':
        '''ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6093.ConceptCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def power_flow_results(self) -> '_3259.ConceptCouplingHalfPowerFlow':
        '''ConceptCouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3259.ConceptCouplingHalfPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
