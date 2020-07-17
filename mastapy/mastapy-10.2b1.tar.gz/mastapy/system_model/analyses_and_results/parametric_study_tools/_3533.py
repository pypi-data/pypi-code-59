'''_3533.py

FaceGearMeshParametricStudyTool
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _1887
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6134
from mastapy.system_model.analyses_and_results.system_deflections import _2281
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3537
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'FaceGearMeshParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshParametricStudyTool',)


class FaceGearMeshParametricStudyTool(_3537.GearMeshParametricStudyTool):
    '''FaceGearMeshParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1887.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1887.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6134.FaceGearMeshLoadCase':
        '''FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6134.FaceGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2281.FaceGearMeshSystemDeflection]':
        '''List[FaceGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2281.FaceGearMeshSystemDeflection))
        return value
