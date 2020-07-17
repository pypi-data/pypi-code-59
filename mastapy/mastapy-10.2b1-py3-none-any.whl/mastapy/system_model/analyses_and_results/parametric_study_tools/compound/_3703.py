'''_3703.py

RootAssemblyCompoundParametricStudyTool
'''


from mastapy.system_model.analyses_and_results.parametric_study_tools import _3566
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5250, _5249, _5251, _5254,
    _5255, _5257, _5259
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _3622
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'RootAssemblyCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundParametricStudyTool',)


class RootAssemblyCompoundParametricStudyTool(_3622.AssemblyCompoundParametricStudyTool):
    '''RootAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def parametric_analysis_options(self) -> '_3566.ParametricStudyToolOptions':
        '''ParametricStudyToolOptions: 'ParametricAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3566.ParametricStudyToolOptions)(self.wrapped.ParametricAnalysisOptions) if self.wrapped.ParametricAnalysisOptions else None

    @property
    def compound_load_case(self) -> '_5250.AbstractLoadCaseGroup':
        '''AbstractLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5250.AbstractLoadCaseGroup)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_abstract_design_state_load_case_group(self) -> '_5249.AbstractDesignStateLoadCaseGroup':
        '''AbstractDesignStateLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5249.AbstractDesignStateLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractDesignStateLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5249.AbstractDesignStateLoadCaseGroup)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_abstract_static_load_case_group(self) -> '_5251.AbstractStaticLoadCaseGroup':
        '''AbstractStaticLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5251.AbstractStaticLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractStaticLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5251.AbstractStaticLoadCaseGroup)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_design_state(self) -> '_5254.DesignState':
        '''DesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5254.DesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5254.DesignState)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_duty_cycle(self) -> '_5255.DutyCycle':
        '''DutyCycle: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5255.DutyCycle.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DutyCycle. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5255.DutyCycle)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_group_of_time_series_load_cases(self) -> '_5257.GroupOfTimeSeriesLoadCases':
        '''GroupOfTimeSeriesLoadCases: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5257.GroupOfTimeSeriesLoadCases.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to GroupOfTimeSeriesLoadCases. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5257.GroupOfTimeSeriesLoadCases)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_sub_group_in_single_design_state(self) -> '_5259.SubGroupInSingleDesignState':
        '''SubGroupInSingleDesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5259.SubGroupInSingleDesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to SubGroupInSingleDesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new(_5259.SubGroupInSingleDesignState)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None
