'''_3506.py

ConceptCouplingParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2133
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.system_deflections import _2252
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3517
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConceptCouplingParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingParametricStudyTool',)


class ConceptCouplingParametricStudyTool(_3517.CouplingParametricStudyTool):
    '''ConceptCouplingParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2133.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2133.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6094.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6094.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2252.ConceptCouplingSystemDeflection]':
        '''List[ConceptCouplingSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2252.ConceptCouplingSystemDeflection))
        return value
