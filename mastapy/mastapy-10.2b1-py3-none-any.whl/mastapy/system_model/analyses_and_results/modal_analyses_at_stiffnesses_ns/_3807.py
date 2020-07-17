'''_3807.py

KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2097
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6167
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3806, _3805, _3801
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses',)


class KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses(_3801.KlingelnbergCycloPalloidConicalGearSetModalAnalysesAtStiffnesses):
    '''KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2097.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3806.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysesAtStiffnesses, constructor.new(_3806.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3805.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysesAtStiffnesses, constructor.new(_3805.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtStiffnesses))
        return value
