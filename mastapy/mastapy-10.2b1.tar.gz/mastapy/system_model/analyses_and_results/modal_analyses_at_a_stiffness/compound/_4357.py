'''_4357.py

AssemblyCompoundModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4234
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4358, _4360, _4363, _4369,
    _4370, _4371, _4376, _4381,
    _4391, _4395, _4401, _4402,
    _4409, _4410, _4417, _4420,
    _4421, _4422, _4424, _4426,
    _4431, _4432, _4433, _4440,
    _4435, _4439, _4445, _4446,
    _4451, _4454, _4457, _4461,
    _4465, _4469, _4472, _4352
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'AssemblyCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysisAtAStiffness',)


class AssemblyCompoundModalAnalysisAtAStiffness(_4352.AbstractAssemblyCompoundModalAnalysisAtAStiffness):
    '''AssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysisAtAStiffness.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_4234.AssemblyModalAnalysisAtAStiffness]':
        '''List[AssemblyModalAnalysisAtAStiffness]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4234.AssemblyModalAnalysisAtAStiffness))
        return value

    @property
    def assembly_modal_analysis_at_a_stiffness_load_cases(self) -> 'List[_4234.AssemblyModalAnalysisAtAStiffness]':
        '''List[AssemblyModalAnalysisAtAStiffness]: 'AssemblyModalAnalysisAtAStiffnessLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysisAtAStiffnessLoadCases, constructor.new(_4234.AssemblyModalAnalysisAtAStiffness))
        return value

    @property
    def bearings(self) -> 'List[_4358.BearingCompoundModalAnalysisAtAStiffness]':
        '''List[BearingCompoundModalAnalysisAtAStiffness]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4358.BearingCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def belt_drives(self) -> 'List[_4360.BeltDriveCompoundModalAnalysisAtAStiffness]':
        '''List[BeltDriveCompoundModalAnalysisAtAStiffness]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4360.BeltDriveCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4363.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4363.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def bolts(self) -> 'List[_4369.BoltCompoundModalAnalysisAtAStiffness]':
        '''List[BoltCompoundModalAnalysisAtAStiffness]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4369.BoltCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def bolted_joints(self) -> 'List[_4370.BoltedJointCompoundModalAnalysisAtAStiffness]':
        '''List[BoltedJointCompoundModalAnalysisAtAStiffness]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4370.BoltedJointCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def clutches(self) -> 'List[_4371.ClutchCompoundModalAnalysisAtAStiffness]':
        '''List[ClutchCompoundModalAnalysisAtAStiffness]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4371.ClutchCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def concept_couplings(self) -> 'List[_4376.ConceptCouplingCompoundModalAnalysisAtAStiffness]':
        '''List[ConceptCouplingCompoundModalAnalysisAtAStiffness]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4376.ConceptCouplingCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4381.ConceptGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[ConceptGearSetCompoundModalAnalysisAtAStiffness]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4381.ConceptGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def cv_ts(self) -> 'List[_4391.CVTCompoundModalAnalysisAtAStiffness]':
        '''List[CVTCompoundModalAnalysisAtAStiffness]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4391.CVTCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4395.CylindricalGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[CylindricalGearSetCompoundModalAnalysisAtAStiffness]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4395.CylindricalGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4401.FaceGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[FaceGearSetCompoundModalAnalysisAtAStiffness]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4401.FaceGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4402.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4402.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4409.HypoidGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[HypoidGearSetCompoundModalAnalysisAtAStiffness]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4409.HypoidGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4410.ImportedFEComponentCompoundModalAnalysisAtAStiffness]':
        '''List[ImportedFEComponentCompoundModalAnalysisAtAStiffness]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4410.ImportedFEComponentCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4417.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4417.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4420.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4420.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def mass_discs(self) -> 'List[_4421.MassDiscCompoundModalAnalysisAtAStiffness]':
        '''List[MassDiscCompoundModalAnalysisAtAStiffness]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4421.MassDiscCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def measurement_components(self) -> 'List[_4422.MeasurementComponentCompoundModalAnalysisAtAStiffness]':
        '''List[MeasurementComponentCompoundModalAnalysisAtAStiffness]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4422.MeasurementComponentCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def oil_seals(self) -> 'List[_4424.OilSealCompoundModalAnalysisAtAStiffness]':
        '''List[OilSealCompoundModalAnalysisAtAStiffness]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4424.OilSealCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4426.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness]':
        '''List[PartToPartShearCouplingCompoundModalAnalysisAtAStiffness]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4426.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def planet_carriers(self) -> 'List[_4431.PlanetCarrierCompoundModalAnalysisAtAStiffness]':
        '''List[PlanetCarrierCompoundModalAnalysisAtAStiffness]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4431.PlanetCarrierCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def point_loads(self) -> 'List[_4432.PointLoadCompoundModalAnalysisAtAStiffness]':
        '''List[PointLoadCompoundModalAnalysisAtAStiffness]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4432.PointLoadCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def power_loads(self) -> 'List[_4433.PowerLoadCompoundModalAnalysisAtAStiffness]':
        '''List[PowerLoadCompoundModalAnalysisAtAStiffness]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4433.PowerLoadCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4440.ShaftHubConnectionCompoundModalAnalysisAtAStiffness]':
        '''List[ShaftHubConnectionCompoundModalAnalysisAtAStiffness]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4440.ShaftHubConnectionCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4435.RollingRingAssemblyCompoundModalAnalysisAtAStiffness]':
        '''List[RollingRingAssemblyCompoundModalAnalysisAtAStiffness]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4435.RollingRingAssemblyCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def shafts(self) -> 'List[_4439.ShaftCompoundModalAnalysisAtAStiffness]':
        '''List[ShaftCompoundModalAnalysisAtAStiffness]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4439.ShaftCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4445.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[SpiralBevelGearSetCompoundModalAnalysisAtAStiffness]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4445.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def spring_dampers(self) -> 'List[_4446.SpringDamperCompoundModalAnalysisAtAStiffness]':
        '''List[SpringDamperCompoundModalAnalysisAtAStiffness]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4446.SpringDamperCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4451.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4451.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4454.StraightBevelGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[StraightBevelGearSetCompoundModalAnalysisAtAStiffness]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4454.StraightBevelGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def synchronisers(self) -> 'List[_4457.SynchroniserCompoundModalAnalysisAtAStiffness]':
        '''List[SynchroniserCompoundModalAnalysisAtAStiffness]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4457.SynchroniserCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def torque_converters(self) -> 'List[_4461.TorqueConverterCompoundModalAnalysisAtAStiffness]':
        '''List[TorqueConverterCompoundModalAnalysisAtAStiffness]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4461.TorqueConverterCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4465.UnbalancedMassCompoundModalAnalysisAtAStiffness]':
        '''List[UnbalancedMassCompoundModalAnalysisAtAStiffness]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4465.UnbalancedMassCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4469.WormGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[WormGearSetCompoundModalAnalysisAtAStiffness]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4469.WormGearSetCompoundModalAnalysisAtAStiffness))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4472.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness]':
        '''List[ZerolBevelGearSetCompoundModalAnalysisAtAStiffness]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4472.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness))
        return value
