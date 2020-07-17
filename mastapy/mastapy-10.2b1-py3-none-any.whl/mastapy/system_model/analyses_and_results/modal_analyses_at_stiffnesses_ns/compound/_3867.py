'''_3867.py

AssemblyCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3743
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import (
    _3868, _3870, _3873, _3879,
    _3880, _3881, _3886, _3891,
    _3901, _3905, _3911, _3912,
    _3919, _3920, _3927, _3930,
    _3931, _3932, _3934, _3936,
    _3941, _3942, _3943, _3950,
    _3945, _3949, _3955, _3956,
    _3961, _3964, _3967, _3971,
    _3975, _3979, _3982, _3862
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'AssemblyCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysesAtStiffnesses',)


class AssemblyCompoundModalAnalysesAtStiffnesses(_3862.AbstractAssemblyCompoundModalAnalysesAtStiffnesses):
    '''AssemblyCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysesAtStiffnesses.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_3743.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3743.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3743.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3743.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def bearings(self) -> 'List[_3868.BearingCompoundModalAnalysesAtStiffnesses]':
        '''List[BearingCompoundModalAnalysesAtStiffnesses]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3868.BearingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def belt_drives(self) -> 'List[_3870.BeltDriveCompoundModalAnalysesAtStiffnesses]':
        '''List[BeltDriveCompoundModalAnalysesAtStiffnesses]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3870.BeltDriveCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3873.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3873.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolts(self) -> 'List[_3879.BoltCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltCompoundModalAnalysesAtStiffnesses]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3879.BoltCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolted_joints(self) -> 'List[_3880.BoltedJointCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltedJointCompoundModalAnalysesAtStiffnesses]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3880.BoltedJointCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def clutches(self) -> 'List[_3881.ClutchCompoundModalAnalysesAtStiffnesses]':
        '''List[ClutchCompoundModalAnalysesAtStiffnesses]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3881.ClutchCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_couplings(self) -> 'List[_3886.ConceptCouplingCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptCouplingCompoundModalAnalysesAtStiffnesses]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3886.ConceptCouplingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3891.ConceptGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptGearSetCompoundModalAnalysesAtStiffnesses]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3891.ConceptGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cv_ts(self) -> 'List[_3901.CVTCompoundModalAnalysesAtStiffnesses]':
        '''List[CVTCompoundModalAnalysesAtStiffnesses]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3901.CVTCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3905.CylindricalGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[CylindricalGearSetCompoundModalAnalysesAtStiffnesses]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3905.CylindricalGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3911.FaceGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[FaceGearSetCompoundModalAnalysesAtStiffnesses]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3911.FaceGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3912.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3912.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3919.HypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[HypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3919.HypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3920.ImportedFEComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtStiffnesses]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3920.ImportedFEComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3927.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3927.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3930.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3930.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def mass_discs(self) -> 'List[_3931.MassDiscCompoundModalAnalysesAtStiffnesses]':
        '''List[MassDiscCompoundModalAnalysesAtStiffnesses]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3931.MassDiscCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def measurement_components(self) -> 'List[_3932.MeasurementComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[MeasurementComponentCompoundModalAnalysesAtStiffnesses]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3932.MeasurementComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def oil_seals(self) -> 'List[_3934.OilSealCompoundModalAnalysesAtStiffnesses]':
        '''List[OilSealCompoundModalAnalysesAtStiffnesses]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3934.OilSealCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3936.PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses]':
        '''List[PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3936.PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def planet_carriers(self) -> 'List[_3941.PlanetCarrierCompoundModalAnalysesAtStiffnesses]':
        '''List[PlanetCarrierCompoundModalAnalysesAtStiffnesses]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3941.PlanetCarrierCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def point_loads(self) -> 'List[_3942.PointLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PointLoadCompoundModalAnalysesAtStiffnesses]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3942.PointLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def power_loads(self) -> 'List[_3943.PowerLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PowerLoadCompoundModalAnalysesAtStiffnesses]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3943.PowerLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3950.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3950.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3945.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3945.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shafts(self) -> 'List[_3949.ShaftCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftCompoundModalAnalysesAtStiffnesses]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3949.ShaftCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3955.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3955.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spring_dampers(self) -> 'List[_3956.SpringDamperCompoundModalAnalysesAtStiffnesses]':
        '''List[SpringDamperCompoundModalAnalysesAtStiffnesses]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3956.SpringDamperCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3961.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3961.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3964.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3964.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def synchronisers(self) -> 'List[_3967.SynchroniserCompoundModalAnalysesAtStiffnesses]':
        '''List[SynchroniserCompoundModalAnalysesAtStiffnesses]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3967.SynchroniserCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def torque_converters(self) -> 'List[_3971.TorqueConverterCompoundModalAnalysesAtStiffnesses]':
        '''List[TorqueConverterCompoundModalAnalysesAtStiffnesses]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3971.TorqueConverterCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3975.UnbalancedMassCompoundModalAnalysesAtStiffnesses]':
        '''List[UnbalancedMassCompoundModalAnalysesAtStiffnesses]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3975.UnbalancedMassCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3979.WormGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[WormGearSetCompoundModalAnalysesAtStiffnesses]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3979.WormGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3982.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3982.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value
