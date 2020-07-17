'''_3613.py

WormGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6231
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3612, _3611, _3539
from mastapy.system_model.analyses_and_results.system_deflections import _2359
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'WormGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetParametricStudyTool',)


class WormGearSetParametricStudyTool(_3539.GearSetParametricStudyTool):
    '''WormGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetParametricStudyTool.TYPE'):
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
    def worm_gears_parametric_study_tool(self) -> 'List[_3612.WormGearParametricStudyTool]':
        '''List[WormGearParametricStudyTool]: 'WormGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsParametricStudyTool, constructor.new(_3612.WormGearParametricStudyTool))
        return value

    @property
    def worm_meshes_parametric_study_tool(self) -> 'List[_3611.WormGearMeshParametricStudyTool]':
        '''List[WormGearMeshParametricStudyTool]: 'WormMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesParametricStudyTool, constructor.new(_3611.WormGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2359.WormGearSetSystemDeflection]':
        '''List[WormGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2359.WormGearSetSystemDeflection))
        return value
