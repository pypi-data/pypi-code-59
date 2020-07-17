'''_3507.py

ConceptGearMeshParametricStudyTool
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _1881
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6096
from mastapy.system_model.analyses_and_results.system_deflections import _2253
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3537
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConceptGearMeshParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshParametricStudyTool',)


class ConceptGearMeshParametricStudyTool(_3537.GearMeshParametricStudyTool):
    '''ConceptGearMeshParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1881.ConceptGearMesh':
        '''ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1881.ConceptGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6096.ConceptGearMeshLoadCase':
        '''ConceptGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6096.ConceptGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2253.ConceptGearMeshSystemDeflection]':
        '''List[ConceptGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2253.ConceptGearMeshSystemDeflection))
        return value
