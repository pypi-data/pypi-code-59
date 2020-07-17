'''_5455.py

ConceptGearMeshSingleMeshWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _1881
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6096
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5479
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'ConceptGearMeshSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshSingleMeshWhineAnalysis',)


class ConceptGearMeshSingleMeshWhineAnalysis(_5479.GearMeshSingleMeshWhineAnalysis):
    '''ConceptGearMeshSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshSingleMeshWhineAnalysis.TYPE'):
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
