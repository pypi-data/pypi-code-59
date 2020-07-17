'''_4104.py

WormGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6231
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4103, _4102, _4037
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'WormGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetModalAnalysesAtSpeeds',)


class WormGearSetModalAnalysesAtSpeeds(_4037.GearSetModalAnalysesAtSpeeds):
    '''WormGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetModalAnalysesAtSpeeds.TYPE'):
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
    def worm_gears_modal_analyses_at_speeds(self) -> 'List[_4103.WormGearModalAnalysesAtSpeeds]':
        '''List[WormGearModalAnalysesAtSpeeds]: 'WormGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsModalAnalysesAtSpeeds, constructor.new(_4103.WormGearModalAnalysesAtSpeeds))
        return value

    @property
    def worm_meshes_modal_analyses_at_speeds(self) -> 'List[_4102.WormGearMeshModalAnalysesAtSpeeds]':
        '''List[WormGearMeshModalAnalysesAtSpeeds]: 'WormMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesModalAnalysesAtSpeeds, constructor.new(_4102.WormGearMeshModalAnalysesAtSpeeds))
        return value
