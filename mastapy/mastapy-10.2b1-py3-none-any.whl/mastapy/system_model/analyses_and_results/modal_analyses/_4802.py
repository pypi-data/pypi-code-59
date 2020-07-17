'''_4802.py

PlanetCarrierModalAnalysis
'''


from mastapy.system_model.part_model import _2027
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6182
from mastapy.system_model.analyses_and_results.system_deflections import _2315
from mastapy.system_model.analyses_and_results.modal_analyses import _4793
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'PlanetCarrierModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierModalAnalysis',)


class PlanetCarrierModalAnalysis(_4793.MountableComponentModalAnalysis):
    '''PlanetCarrierModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2027.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2027.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6182.PlanetCarrierLoadCase':
        '''PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6182.PlanetCarrierLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2315.PlanetCarrierSystemDeflection':
        '''PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2315.PlanetCarrierSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
