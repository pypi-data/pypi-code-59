'''_3595.py

StraightBevelDiffGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2102
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6207
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3594, _3593, _3496
from mastapy.system_model.analyses_and_results.system_deflections import _2336
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'StraightBevelDiffGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetParametricStudyTool',)


class StraightBevelDiffGearSetParametricStudyTool(_3496.BevelGearSetParametricStudyTool):
    '''StraightBevelDiffGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2102.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6207.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6207.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_diff_gears_parametric_study_tool(self) -> 'List[_3594.StraightBevelDiffGearParametricStudyTool]':
        '''List[StraightBevelDiffGearParametricStudyTool]: 'StraightBevelDiffGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsParametricStudyTool, constructor.new(_3594.StraightBevelDiffGearParametricStudyTool))
        return value

    @property
    def straight_bevel_diff_meshes_parametric_study_tool(self) -> 'List[_3593.StraightBevelDiffGearMeshParametricStudyTool]':
        '''List[StraightBevelDiffGearMeshParametricStudyTool]: 'StraightBevelDiffMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesParametricStudyTool, constructor.new(_3593.StraightBevelDiffGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2336.StraightBevelDiffGearSetSystemDeflection]':
        '''List[StraightBevelDiffGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2336.StraightBevelDiffGearSetSystemDeflection))
        return value
