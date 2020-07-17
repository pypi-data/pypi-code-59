'''_3782.py

CylindricalGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2082
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6115
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3781, _3780, _3792
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'CylindricalGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetModalAnalysesAtStiffnesses',)


class CylindricalGearSetModalAnalysesAtStiffnesses(_3792.GearSetModalAnalysesAtStiffnesses):
    '''CylindricalGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2082.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2082.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6115.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6115.CylindricalGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def cylindrical_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3781.CylindricalGearModalAnalysesAtStiffnesses]':
        '''List[CylindricalGearModalAnalysesAtStiffnesses]: 'CylindricalGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsModalAnalysesAtStiffnesses, constructor.new(_3781.CylindricalGearModalAnalysesAtStiffnesses))
        return value

    @property
    def cylindrical_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3780.CylindricalGearMeshModalAnalysesAtStiffnesses]':
        '''List[CylindricalGearMeshModalAnalysesAtStiffnesses]: 'CylindricalMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesModalAnalysesAtStiffnesses, constructor.new(_3780.CylindricalGearMeshModalAnalysesAtStiffnesses))
        return value
