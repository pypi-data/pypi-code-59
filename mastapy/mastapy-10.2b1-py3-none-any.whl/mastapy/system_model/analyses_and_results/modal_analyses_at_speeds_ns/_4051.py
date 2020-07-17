'''_4051.py

KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.gears import _2096
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6165
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4045
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds',)


class KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds(_4045.KlingelnbergCycloPalloidConicalGearModalAnalysesAtSpeeds):
    '''KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2096.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2096.KlingelnbergCycloPalloidSpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
