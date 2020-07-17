'''_4600.py

AssemblyCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4478
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _4601, _4603, _4606, _4612,
    _4613, _4614, _4619, _4624,
    _4634, _4638, _4644, _4645,
    _4652, _4653, _4660, _4663,
    _4664, _4665, _4667, _4669,
    _4674, _4675, _4676, _4683,
    _4678, _4682, _4688, _4689,
    _4694, _4697, _4700, _4704,
    _4708, _4712, _4715, _4595
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'AssemblyCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysisAtASpeed',)


class AssemblyCompoundModalAnalysisAtASpeed(_4595.AbstractAssemblyCompoundModalAnalysisAtASpeed):
    '''AssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysisAtASpeed.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_4478.AssemblyModalAnalysisAtASpeed]':
        '''List[AssemblyModalAnalysisAtASpeed]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4478.AssemblyModalAnalysisAtASpeed))
        return value

    @property
    def assembly_modal_analysis_at_a_speed_load_cases(self) -> 'List[_4478.AssemblyModalAnalysisAtASpeed]':
        '''List[AssemblyModalAnalysisAtASpeed]: 'AssemblyModalAnalysisAtASpeedLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysisAtASpeedLoadCases, constructor.new(_4478.AssemblyModalAnalysisAtASpeed))
        return value

    @property
    def bearings(self) -> 'List[_4601.BearingCompoundModalAnalysisAtASpeed]':
        '''List[BearingCompoundModalAnalysisAtASpeed]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4601.BearingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def belt_drives(self) -> 'List[_4603.BeltDriveCompoundModalAnalysisAtASpeed]':
        '''List[BeltDriveCompoundModalAnalysisAtASpeed]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4603.BeltDriveCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4606.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysisAtASpeed]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4606.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bolts(self) -> 'List[_4612.BoltCompoundModalAnalysisAtASpeed]':
        '''List[BoltCompoundModalAnalysisAtASpeed]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4612.BoltCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bolted_joints(self) -> 'List[_4613.BoltedJointCompoundModalAnalysisAtASpeed]':
        '''List[BoltedJointCompoundModalAnalysisAtASpeed]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4613.BoltedJointCompoundModalAnalysisAtASpeed))
        return value

    @property
    def clutches(self) -> 'List[_4614.ClutchCompoundModalAnalysisAtASpeed]':
        '''List[ClutchCompoundModalAnalysisAtASpeed]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4614.ClutchCompoundModalAnalysisAtASpeed))
        return value

    @property
    def concept_couplings(self) -> 'List[_4619.ConceptCouplingCompoundModalAnalysisAtASpeed]':
        '''List[ConceptCouplingCompoundModalAnalysisAtASpeed]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4619.ConceptCouplingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4624.ConceptGearSetCompoundModalAnalysisAtASpeed]':
        '''List[ConceptGearSetCompoundModalAnalysisAtASpeed]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4624.ConceptGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cv_ts(self) -> 'List[_4634.CVTCompoundModalAnalysisAtASpeed]':
        '''List[CVTCompoundModalAnalysisAtASpeed]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4634.CVTCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4638.CylindricalGearSetCompoundModalAnalysisAtASpeed]':
        '''List[CylindricalGearSetCompoundModalAnalysisAtASpeed]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4638.CylindricalGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4644.FaceGearSetCompoundModalAnalysisAtASpeed]':
        '''List[FaceGearSetCompoundModalAnalysisAtASpeed]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4644.FaceGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4645.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysisAtASpeed]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4645.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4652.HypoidGearSetCompoundModalAnalysisAtASpeed]':
        '''List[HypoidGearSetCompoundModalAnalysisAtASpeed]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4652.HypoidGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4653.ImportedFEComponentCompoundModalAnalysisAtASpeed]':
        '''List[ImportedFEComponentCompoundModalAnalysisAtASpeed]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4653.ImportedFEComponentCompoundModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4660.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4660.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4663.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4663.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def mass_discs(self) -> 'List[_4664.MassDiscCompoundModalAnalysisAtASpeed]':
        '''List[MassDiscCompoundModalAnalysisAtASpeed]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4664.MassDiscCompoundModalAnalysisAtASpeed))
        return value

    @property
    def measurement_components(self) -> 'List[_4665.MeasurementComponentCompoundModalAnalysisAtASpeed]':
        '''List[MeasurementComponentCompoundModalAnalysisAtASpeed]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4665.MeasurementComponentCompoundModalAnalysisAtASpeed))
        return value

    @property
    def oil_seals(self) -> 'List[_4667.OilSealCompoundModalAnalysisAtASpeed]':
        '''List[OilSealCompoundModalAnalysisAtASpeed]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4667.OilSealCompoundModalAnalysisAtASpeed))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4669.PartToPartShearCouplingCompoundModalAnalysisAtASpeed]':
        '''List[PartToPartShearCouplingCompoundModalAnalysisAtASpeed]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4669.PartToPartShearCouplingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def planet_carriers(self) -> 'List[_4674.PlanetCarrierCompoundModalAnalysisAtASpeed]':
        '''List[PlanetCarrierCompoundModalAnalysisAtASpeed]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4674.PlanetCarrierCompoundModalAnalysisAtASpeed))
        return value

    @property
    def point_loads(self) -> 'List[_4675.PointLoadCompoundModalAnalysisAtASpeed]':
        '''List[PointLoadCompoundModalAnalysisAtASpeed]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4675.PointLoadCompoundModalAnalysisAtASpeed))
        return value

    @property
    def power_loads(self) -> 'List[_4676.PowerLoadCompoundModalAnalysisAtASpeed]':
        '''List[PowerLoadCompoundModalAnalysisAtASpeed]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4676.PowerLoadCompoundModalAnalysisAtASpeed))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4683.ShaftHubConnectionCompoundModalAnalysisAtASpeed]':
        '''List[ShaftHubConnectionCompoundModalAnalysisAtASpeed]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4683.ShaftHubConnectionCompoundModalAnalysisAtASpeed))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4678.RollingRingAssemblyCompoundModalAnalysisAtASpeed]':
        '''List[RollingRingAssemblyCompoundModalAnalysisAtASpeed]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4678.RollingRingAssemblyCompoundModalAnalysisAtASpeed))
        return value

    @property
    def shafts(self) -> 'List[_4682.ShaftCompoundModalAnalysisAtASpeed]':
        '''List[ShaftCompoundModalAnalysisAtASpeed]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4682.ShaftCompoundModalAnalysisAtASpeed))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4688.SpiralBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[SpiralBevelGearSetCompoundModalAnalysisAtASpeed]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4688.SpiralBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def spring_dampers(self) -> 'List[_4689.SpringDamperCompoundModalAnalysisAtASpeed]':
        '''List[SpringDamperCompoundModalAnalysisAtASpeed]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4689.SpringDamperCompoundModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4694.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4694.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4697.StraightBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelGearSetCompoundModalAnalysisAtASpeed]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4697.StraightBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def synchronisers(self) -> 'List[_4700.SynchroniserCompoundModalAnalysisAtASpeed]':
        '''List[SynchroniserCompoundModalAnalysisAtASpeed]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4700.SynchroniserCompoundModalAnalysisAtASpeed))
        return value

    @property
    def torque_converters(self) -> 'List[_4704.TorqueConverterCompoundModalAnalysisAtASpeed]':
        '''List[TorqueConverterCompoundModalAnalysisAtASpeed]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4704.TorqueConverterCompoundModalAnalysisAtASpeed))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4708.UnbalancedMassCompoundModalAnalysisAtASpeed]':
        '''List[UnbalancedMassCompoundModalAnalysisAtASpeed]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4708.UnbalancedMassCompoundModalAnalysisAtASpeed))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4712.WormGearSetCompoundModalAnalysisAtASpeed]':
        '''List[WormGearSetCompoundModalAnalysisAtASpeed]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4712.WormGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4715.ZerolBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[ZerolBevelGearSetCompoundModalAnalysisAtASpeed]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4715.ZerolBevelGearSetCompoundModalAnalysisAtASpeed))
        return value
