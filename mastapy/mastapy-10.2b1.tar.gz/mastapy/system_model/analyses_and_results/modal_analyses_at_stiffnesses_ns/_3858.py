'''_3858.py

WormGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6231
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3857, _3856, _3792
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'WormGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetModalAnalysesAtStiffnesses',)


class WormGearSetModalAnalysesAtStiffnesses(_3792.GearSetModalAnalysesAtStiffnesses):
    '''WormGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2108.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6231.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6231.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def worm_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3857.WormGearModalAnalysesAtStiffnesses]':
        '''List[WormGearModalAnalysesAtStiffnesses]: 'WormGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsModalAnalysesAtStiffnesses, constructor.new(_3857.WormGearModalAnalysesAtStiffnesses))
        return value

    @property
    def worm_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3856.WormGearMeshModalAnalysesAtStiffnesses]':
        '''List[WormGearMeshModalAnalysesAtStiffnesses]: 'WormMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesModalAnalysesAtStiffnesses, constructor.new(_3856.WormGearMeshModalAnalysesAtStiffnesses))
        return value
