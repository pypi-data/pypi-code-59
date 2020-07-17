'''_6386.py

AssemblyCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6260
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _6387, _6389, _6392, _6398,
    _6399, _6400, _6405, _6410,
    _6420, _6424, _6430, _6431,
    _6438, _6439, _6446, _6449,
    _6450, _6451, _6453, _6455,
    _6460, _6461, _6462, _6469,
    _6464, _6468, _6474, _6475,
    _6480, _6483, _6486, _6490,
    _6494, _6498, _6501, _6381
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'AssemblyCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundAdvancedSystemDeflection',)


class AssemblyCompoundAdvancedSystemDeflection(_6381.AbstractAssemblyCompoundAdvancedSystemDeflection):
    '''AssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1995.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1995.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_6260.AssemblyAdvancedSystemDeflection]':
        '''List[AssemblyAdvancedSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_6260.AssemblyAdvancedSystemDeflection))
        return value

    @property
    def assembly_advanced_system_deflection_load_cases(self) -> 'List[_6260.AssemblyAdvancedSystemDeflection]':
        '''List[AssemblyAdvancedSystemDeflection]: 'AssemblyAdvancedSystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAdvancedSystemDeflectionLoadCases, constructor.new(_6260.AssemblyAdvancedSystemDeflection))
        return value

    @property
    def bearings(self) -> 'List[_6387.BearingCompoundAdvancedSystemDeflection]':
        '''List[BearingCompoundAdvancedSystemDeflection]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_6387.BearingCompoundAdvancedSystemDeflection))
        return value

    @property
    def belt_drives(self) -> 'List[_6389.BeltDriveCompoundAdvancedSystemDeflection]':
        '''List[BeltDriveCompoundAdvancedSystemDeflection]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_6389.BeltDriveCompoundAdvancedSystemDeflection))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_6392.BevelDifferentialGearSetCompoundAdvancedSystemDeflection]':
        '''List[BevelDifferentialGearSetCompoundAdvancedSystemDeflection]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_6392.BevelDifferentialGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def bolts(self) -> 'List[_6398.BoltCompoundAdvancedSystemDeflection]':
        '''List[BoltCompoundAdvancedSystemDeflection]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_6398.BoltCompoundAdvancedSystemDeflection))
        return value

    @property
    def bolted_joints(self) -> 'List[_6399.BoltedJointCompoundAdvancedSystemDeflection]':
        '''List[BoltedJointCompoundAdvancedSystemDeflection]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_6399.BoltedJointCompoundAdvancedSystemDeflection))
        return value

    @property
    def clutches(self) -> 'List[_6400.ClutchCompoundAdvancedSystemDeflection]':
        '''List[ClutchCompoundAdvancedSystemDeflection]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_6400.ClutchCompoundAdvancedSystemDeflection))
        return value

    @property
    def concept_couplings(self) -> 'List[_6405.ConceptCouplingCompoundAdvancedSystemDeflection]':
        '''List[ConceptCouplingCompoundAdvancedSystemDeflection]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_6405.ConceptCouplingCompoundAdvancedSystemDeflection))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_6410.ConceptGearSetCompoundAdvancedSystemDeflection]':
        '''List[ConceptGearSetCompoundAdvancedSystemDeflection]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_6410.ConceptGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def cv_ts(self) -> 'List[_6420.CVTCompoundAdvancedSystemDeflection]':
        '''List[CVTCompoundAdvancedSystemDeflection]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_6420.CVTCompoundAdvancedSystemDeflection))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_6424.CylindricalGearSetCompoundAdvancedSystemDeflection]':
        '''List[CylindricalGearSetCompoundAdvancedSystemDeflection]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_6424.CylindricalGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def face_gear_sets(self) -> 'List[_6430.FaceGearSetCompoundAdvancedSystemDeflection]':
        '''List[FaceGearSetCompoundAdvancedSystemDeflection]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_6430.FaceGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_6431.FlexiblePinAssemblyCompoundAdvancedSystemDeflection]':
        '''List[FlexiblePinAssemblyCompoundAdvancedSystemDeflection]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_6431.FlexiblePinAssemblyCompoundAdvancedSystemDeflection))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_6438.HypoidGearSetCompoundAdvancedSystemDeflection]':
        '''List[HypoidGearSetCompoundAdvancedSystemDeflection]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_6438.HypoidGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def imported_fe_components(self) -> 'List[_6439.ImportedFEComponentCompoundAdvancedSystemDeflection]':
        '''List[ImportedFEComponentCompoundAdvancedSystemDeflection]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_6439.ImportedFEComponentCompoundAdvancedSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_6446.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_6446.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_6449.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_6449.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def mass_discs(self) -> 'List[_6450.MassDiscCompoundAdvancedSystemDeflection]':
        '''List[MassDiscCompoundAdvancedSystemDeflection]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_6450.MassDiscCompoundAdvancedSystemDeflection))
        return value

    @property
    def measurement_components(self) -> 'List[_6451.MeasurementComponentCompoundAdvancedSystemDeflection]':
        '''List[MeasurementComponentCompoundAdvancedSystemDeflection]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_6451.MeasurementComponentCompoundAdvancedSystemDeflection))
        return value

    @property
    def oil_seals(self) -> 'List[_6453.OilSealCompoundAdvancedSystemDeflection]':
        '''List[OilSealCompoundAdvancedSystemDeflection]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_6453.OilSealCompoundAdvancedSystemDeflection))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_6455.PartToPartShearCouplingCompoundAdvancedSystemDeflection]':
        '''List[PartToPartShearCouplingCompoundAdvancedSystemDeflection]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_6455.PartToPartShearCouplingCompoundAdvancedSystemDeflection))
        return value

    @property
    def planet_carriers(self) -> 'List[_6460.PlanetCarrierCompoundAdvancedSystemDeflection]':
        '''List[PlanetCarrierCompoundAdvancedSystemDeflection]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_6460.PlanetCarrierCompoundAdvancedSystemDeflection))
        return value

    @property
    def point_loads(self) -> 'List[_6461.PointLoadCompoundAdvancedSystemDeflection]':
        '''List[PointLoadCompoundAdvancedSystemDeflection]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_6461.PointLoadCompoundAdvancedSystemDeflection))
        return value

    @property
    def power_loads(self) -> 'List[_6462.PowerLoadCompoundAdvancedSystemDeflection]':
        '''List[PowerLoadCompoundAdvancedSystemDeflection]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_6462.PowerLoadCompoundAdvancedSystemDeflection))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_6469.ShaftHubConnectionCompoundAdvancedSystemDeflection]':
        '''List[ShaftHubConnectionCompoundAdvancedSystemDeflection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_6469.ShaftHubConnectionCompoundAdvancedSystemDeflection))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_6464.RollingRingAssemblyCompoundAdvancedSystemDeflection]':
        '''List[RollingRingAssemblyCompoundAdvancedSystemDeflection]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_6464.RollingRingAssemblyCompoundAdvancedSystemDeflection))
        return value

    @property
    def shafts(self) -> 'List[_6468.ShaftCompoundAdvancedSystemDeflection]':
        '''List[ShaftCompoundAdvancedSystemDeflection]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_6468.ShaftCompoundAdvancedSystemDeflection))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_6474.SpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        '''List[SpiralBevelGearSetCompoundAdvancedSystemDeflection]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_6474.SpiralBevelGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def spring_dampers(self) -> 'List[_6475.SpringDamperCompoundAdvancedSystemDeflection]':
        '''List[SpringDamperCompoundAdvancedSystemDeflection]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_6475.SpringDamperCompoundAdvancedSystemDeflection))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_6480.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]':
        '''List[StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_6480.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_6483.StraightBevelGearSetCompoundAdvancedSystemDeflection]':
        '''List[StraightBevelGearSetCompoundAdvancedSystemDeflection]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_6483.StraightBevelGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def synchronisers(self) -> 'List[_6486.SynchroniserCompoundAdvancedSystemDeflection]':
        '''List[SynchroniserCompoundAdvancedSystemDeflection]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_6486.SynchroniserCompoundAdvancedSystemDeflection))
        return value

    @property
    def torque_converters(self) -> 'List[_6490.TorqueConverterCompoundAdvancedSystemDeflection]':
        '''List[TorqueConverterCompoundAdvancedSystemDeflection]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_6490.TorqueConverterCompoundAdvancedSystemDeflection))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_6494.UnbalancedMassCompoundAdvancedSystemDeflection]':
        '''List[UnbalancedMassCompoundAdvancedSystemDeflection]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_6494.UnbalancedMassCompoundAdvancedSystemDeflection))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_6498.WormGearSetCompoundAdvancedSystemDeflection]':
        '''List[WormGearSetCompoundAdvancedSystemDeflection]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_6498.WormGearSetCompoundAdvancedSystemDeflection))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_6501.ZerolBevelGearSetCompoundAdvancedSystemDeflection]':
        '''List[ZerolBevelGearSetCompoundAdvancedSystemDeflection]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_6501.ZerolBevelGearSetCompoundAdvancedSystemDeflection))
        return value
