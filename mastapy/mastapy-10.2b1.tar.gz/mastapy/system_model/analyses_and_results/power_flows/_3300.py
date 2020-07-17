'''_3300.py

KlingelnbergCycloPalloidHypoidGearSetPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2095
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6164
from mastapy.gears.rating.klingelnberg_hypoid import _212
from mastapy.system_model.analyses_and_results.power_flows import _3299, _3298, _3297
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'KlingelnbergCycloPalloidHypoidGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetPowerFlow',)


class KlingelnbergCycloPalloidHypoidGearSetPowerFlow(_3297.KlingelnbergCycloPalloidConicalGearSetPowerFlow):
    '''KlingelnbergCycloPalloidHypoidGearSetPowerFlow

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetPowerFlow.TYPE'):
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
    def rating(self) -> '_212.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_212.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_212.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_212.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def gears_power_flow(self) -> 'List[_3299.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsPowerFlow, constructor.new(_3299.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_power_flow(self) -> 'List[_3299.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsPowerFlow, constructor.new(_3299.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value

    @property
    def meshes_power_flow(self) -> 'List[_3298.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesPowerFlow, constructor.new(_3298.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_power_flow(self) -> 'List[_3298.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]: 'KlingelnbergCycloPalloidHypoidMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesPowerFlow, constructor.new(_3298.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow))
        return value
