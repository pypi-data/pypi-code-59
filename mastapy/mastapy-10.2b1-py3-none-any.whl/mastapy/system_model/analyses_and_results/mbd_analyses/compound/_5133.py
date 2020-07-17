'''_5133.py

AssemblyCompoundMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _4989
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
    _5134, _5136, _5139, _5145,
    _5146, _5147, _5152, _5157,
    _5167, _5171, _5177, _5178,
    _5185, _5186, _5193, _5196,
    _5197, _5198, _5200, _5202,
    _5207, _5208, _5209, _5216,
    _5211, _5215, _5221, _5222,
    _5227, _5230, _5233, _5237,
    _5241, _5245, _5248, _5128
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AssemblyCompoundMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundMultiBodyDynamicsAnalysis',)


class AssemblyCompoundMultiBodyDynamicsAnalysis(_5128.AbstractAssemblyCompoundMultiBodyDynamicsAnalysis):
    '''AssemblyCompoundMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundMultiBodyDynamicsAnalysis.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_4989.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4989.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def assembly_multi_body_dynamics_analysis_load_cases(self) -> 'List[_4989.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'AssemblyMultiBodyDynamicsAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyMultiBodyDynamicsAnalysisLoadCases, constructor.new(_4989.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5134.BearingCompoundMultiBodyDynamicsAnalysis]':
        '''List[BearingCompoundMultiBodyDynamicsAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5134.BearingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5136.BeltDriveCompoundMultiBodyDynamicsAnalysis]':
        '''List[BeltDriveCompoundMultiBodyDynamicsAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5136.BeltDriveCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5139.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5139.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5145.BoltCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltCompoundMultiBodyDynamicsAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5145.BoltCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5146.BoltedJointCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltedJointCompoundMultiBodyDynamicsAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5146.BoltedJointCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5147.ClutchCompoundMultiBodyDynamicsAnalysis]':
        '''List[ClutchCompoundMultiBodyDynamicsAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5147.ClutchCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5152.ConceptCouplingCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptCouplingCompoundMultiBodyDynamicsAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5152.ConceptCouplingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5157.ConceptGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearSetCompoundMultiBodyDynamicsAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5157.ConceptGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5167.CVTCompoundMultiBodyDynamicsAnalysis]':
        '''List[CVTCompoundMultiBodyDynamicsAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5167.CVTCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5171.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5171.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5177.FaceGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[FaceGearSetCompoundMultiBodyDynamicsAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5177.FaceGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5178.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5178.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5185.HypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5185.HypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5186.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5186.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5193.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5193.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5196.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5196.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5197.MassDiscCompoundMultiBodyDynamicsAnalysis]':
        '''List[MassDiscCompoundMultiBodyDynamicsAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5197.MassDiscCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5198.MeasurementComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[MeasurementComponentCompoundMultiBodyDynamicsAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5198.MeasurementComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5200.OilSealCompoundMultiBodyDynamicsAnalysis]':
        '''List[OilSealCompoundMultiBodyDynamicsAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5200.OilSealCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5202.PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis]':
        '''List[PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5202.PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5207.PlanetCarrierCompoundMultiBodyDynamicsAnalysis]':
        '''List[PlanetCarrierCompoundMultiBodyDynamicsAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5207.PlanetCarrierCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5208.PointLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PointLoadCompoundMultiBodyDynamicsAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5208.PointLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5209.PowerLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PowerLoadCompoundMultiBodyDynamicsAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5209.PowerLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5216.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5216.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5211.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5211.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5215.ShaftCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftCompoundMultiBodyDynamicsAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5215.ShaftCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5221.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5221.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5222.SpringDamperCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpringDamperCompoundMultiBodyDynamicsAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5222.SpringDamperCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5227.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5227.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5230.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5230.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5233.SynchroniserCompoundMultiBodyDynamicsAnalysis]':
        '''List[SynchroniserCompoundMultiBodyDynamicsAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5233.SynchroniserCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5237.TorqueConverterCompoundMultiBodyDynamicsAnalysis]':
        '''List[TorqueConverterCompoundMultiBodyDynamicsAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5237.TorqueConverterCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5241.UnbalancedMassCompoundMultiBodyDynamicsAnalysis]':
        '''List[UnbalancedMassCompoundMultiBodyDynamicsAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5241.UnbalancedMassCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5245.WormGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[WormGearSetCompoundMultiBodyDynamicsAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5245.WormGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5248.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5248.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value
