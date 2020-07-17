'''_3491.py

BevelDifferentialGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2072
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6079
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3490, _3489, _3496
from mastapy.system_model.analyses_and_results.system_deflections import _2235
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BevelDifferentialGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetParametricStudyTool',)


class BevelDifferentialGearSetParametricStudyTool(_3496.BevelGearSetParametricStudyTool):
    '''BevelDifferentialGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2072.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2072.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6079.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6079.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bevel_differential_gears_parametric_study_tool(self) -> 'List[_3490.BevelDifferentialGearParametricStudyTool]':
        '''List[BevelDifferentialGearParametricStudyTool]: 'BevelDifferentialGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsParametricStudyTool, constructor.new(_3490.BevelDifferentialGearParametricStudyTool))
        return value

    @property
    def bevel_differential_meshes_parametric_study_tool(self) -> 'List[_3489.BevelDifferentialGearMeshParametricStudyTool]':
        '''List[BevelDifferentialGearMeshParametricStudyTool]: 'BevelDifferentialMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesParametricStudyTool, constructor.new(_3489.BevelDifferentialGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2235.BevelDifferentialGearSetSystemDeflection]':
        '''List[BevelDifferentialGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2235.BevelDifferentialGearSetSystemDeflection))
        return value
