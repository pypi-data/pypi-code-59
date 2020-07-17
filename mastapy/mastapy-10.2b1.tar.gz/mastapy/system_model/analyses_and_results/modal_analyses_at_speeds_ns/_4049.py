'''_4049.py

KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2095
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6164
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4048, _4047, _4046
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds',)


class KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds(_4046.KlingelnbergCycloPalloidConicalGearSetModalAnalysesAtSpeeds):
    '''KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2095.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2095.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_modal_analyses_at_speeds(self) -> 'List[_4048.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtSpeeds, constructor.new(_4048.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_modal_analyses_at_speeds(self) -> 'List[_4047.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtSpeeds, constructor.new(_4047.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds))
        return value
