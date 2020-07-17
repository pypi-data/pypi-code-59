'''_5336.py

GearMeshExcitationDetail
'''


from mastapy.system_model.analyses_and_results.system_deflections import (
    _2285, _2227, _2234, _2239,
    _2253, _2257, _2268, _2269,
    _2270, _2281, _2289, _2294,
    _2297, _2300, _2329, _2335,
    _2338, _2358, _2361
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6217
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5293, _5270
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'GearMeshExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshExcitationDetail',)


class GearMeshExcitationDetail(_5270.AbstractPeriodicExcitationDetail):
    '''GearMeshExcitationDetail

    This is a mastapy class.
    '''

    TYPE = _GEAR_MESH_EXCITATION_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def gear_mesh(self) -> '_2285.GearMeshSystemDeflection':
        '''GearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2285.GearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_agma_gleason_conical_gear_mesh_system_deflection(self) -> '_2227.AGMAGleasonConicalGearMeshSystemDeflection':
        '''AGMAGleasonConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2227.AGMAGleasonConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to AGMAGleasonConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2227.AGMAGleasonConicalGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2234.BevelDifferentialGearMeshSystemDeflection':
        '''BevelDifferentialGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2234.BevelDifferentialGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2234.BevelDifferentialGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_bevel_gear_mesh_system_deflection(self) -> '_2239.BevelGearMeshSystemDeflection':
        '''BevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2239.BevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to BevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2239.BevelGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_concept_gear_mesh_system_deflection(self) -> '_2253.ConceptGearMeshSystemDeflection':
        '''ConceptGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2253.ConceptGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ConceptGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2253.ConceptGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_conical_gear_mesh_system_deflection(self) -> '_2257.ConicalGearMeshSystemDeflection':
        '''ConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2257.ConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2257.ConicalGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection(self) -> '_2268.CylindricalGearMeshSystemDeflection':
        '''CylindricalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2268.CylindricalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2268.CylindricalGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2269.CylindricalGearMeshSystemDeflectionTimestep':
        '''CylindricalGearMeshSystemDeflectionTimestep: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2269.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2269.CylindricalGearMeshSystemDeflectionTimestep)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        '''CylindricalGearMeshSystemDeflectionWithLTCAResults: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2270.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_face_gear_mesh_system_deflection(self) -> '_2281.FaceGearMeshSystemDeflection':
        '''FaceGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2281.FaceGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to FaceGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2281.FaceGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_hypoid_gear_mesh_system_deflection(self) -> '_2289.HypoidGearMeshSystemDeflection':
        '''HypoidGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2289.HypoidGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to HypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2289.HypoidGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> '_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self) -> '_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self) -> '_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2329.SpiralBevelGearMeshSystemDeflection':
        '''SpiralBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2329.SpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2329.SpiralBevelGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2335.StraightBevelDiffGearMeshSystemDeflection':
        '''StraightBevelDiffGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2335.StraightBevelDiffGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2335.StraightBevelDiffGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2338.StraightBevelGearMeshSystemDeflection':
        '''StraightBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2338.StraightBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2338.StraightBevelGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_worm_gear_mesh_system_deflection(self) -> '_2358.WormGearMeshSystemDeflection':
        '''WormGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2358.WormGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to WormGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2358.WormGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2361.ZerolBevelGearMeshSystemDeflection':
        '''ZerolBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2361.ZerolBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new(_2361.ZerolBevelGearMeshSystemDeflection)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    def get_compliance_and_force_data(self, excitation_type: '_6217.TEExcitationType') -> '_5293.ComplianceAndForceData':
        ''' 'GetComplianceAndForceData' is the original name of this method.

        Args:
            excitation_type (mastapy.system_model.analyses_and_results.static_loads.TEExcitationType)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComplianceAndForceData
        '''

        excitation_type = conversion.mp_to_pn_enum(excitation_type)
        method_result = self.wrapped.GetComplianceAndForceData(excitation_type)
        return constructor.new(_5293.ComplianceAndForceData)(method_result) if method_result else None
