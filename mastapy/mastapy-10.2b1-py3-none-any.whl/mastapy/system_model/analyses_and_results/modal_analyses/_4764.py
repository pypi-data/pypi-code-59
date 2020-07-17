'''_4764.py

FaceGearMeshModalAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _1887
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6134
from mastapy.system_model.analyses_and_results.system_deflections import _2281
from mastapy.system_model.analyses_and_results.modal_analyses import _4769
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FaceGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshModalAnalysis',)


class FaceGearMeshModalAnalysis(_4769.GearMeshModalAnalysis):
    '''FaceGearMeshModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2281.FaceGearMeshSystemDeflection':
        '''FaceGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2281.FaceGearMeshSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
