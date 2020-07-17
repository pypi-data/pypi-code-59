'''_2501.py

AssemblySteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6073
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _2502, _2504, _2506, _2514,
    _2513, _2517, _2522, _2524,
    _2536, _2538, _2544, _2546,
    _2552, _2554, _2560, _2563,
    _2565, _2566, _2568, _2572,
    _2575, _2576, _2577, _2583,
    _2579, _2584, _2588, _2592,
    _2595, _2598, _2605, _2608,
    _2610, _2613, _2616, _2496
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'AssemblySteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblySteadyStateSynchronousResponseOnAShaft',)


class AssemblySteadyStateSynchronousResponseOnAShaft(_2496.AbstractAssemblySteadyStateSynchronousResponseOnAShaft):
    '''AssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblySteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1995.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6073.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6073.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bearings(self) -> 'List[_2502.BearingSteadyStateSynchronousResponseOnAShaft]':
        '''List[BearingSteadyStateSynchronousResponseOnAShaft]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2502.BearingSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def belt_drives(self) -> 'List[_2504.BeltDriveSteadyStateSynchronousResponseOnAShaft]':
        '''List[BeltDriveSteadyStateSynchronousResponseOnAShaft]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2504.BeltDriveSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2506.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2506.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bolts(self) -> 'List[_2514.BoltSteadyStateSynchronousResponseOnAShaft]':
        '''List[BoltSteadyStateSynchronousResponseOnAShaft]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2514.BoltSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bolted_joints(self) -> 'List[_2513.BoltedJointSteadyStateSynchronousResponseOnAShaft]':
        '''List[BoltedJointSteadyStateSynchronousResponseOnAShaft]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2513.BoltedJointSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def clutches(self) -> 'List[_2517.ClutchSteadyStateSynchronousResponseOnAShaft]':
        '''List[ClutchSteadyStateSynchronousResponseOnAShaft]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2517.ClutchSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def concept_couplings(self) -> 'List[_2522.ConceptCouplingSteadyStateSynchronousResponseOnAShaft]':
        '''List[ConceptCouplingSteadyStateSynchronousResponseOnAShaft]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2522.ConceptCouplingSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2524.ConceptGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[ConceptGearSetSteadyStateSynchronousResponseOnAShaft]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2524.ConceptGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cv_ts(self) -> 'List[_2536.CVTSteadyStateSynchronousResponseOnAShaft]':
        '''List[CVTSteadyStateSynchronousResponseOnAShaft]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_2536.CVTSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2538.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2538.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2544.FaceGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[FaceGearSetSteadyStateSynchronousResponseOnAShaft]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2544.FaceGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2546.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]':
        '''List[FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_2546.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2552.HypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[HypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2552.HypoidGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def imported_fe_components(self) -> 'List[_2554.ImportedFEComponentSteadyStateSynchronousResponseOnAShaft]':
        '''List[ImportedFEComponentSteadyStateSynchronousResponseOnAShaft]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_2554.ImportedFEComponentSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2560.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_2560.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2563.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_2563.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def mass_discs(self) -> 'List[_2565.MassDiscSteadyStateSynchronousResponseOnAShaft]':
        '''List[MassDiscSteadyStateSynchronousResponseOnAShaft]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_2565.MassDiscSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def measurement_components(self) -> 'List[_2566.MeasurementComponentSteadyStateSynchronousResponseOnAShaft]':
        '''List[MeasurementComponentSteadyStateSynchronousResponseOnAShaft]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_2566.MeasurementComponentSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def oil_seals(self) -> 'List[_2568.OilSealSteadyStateSynchronousResponseOnAShaft]':
        '''List[OilSealSteadyStateSynchronousResponseOnAShaft]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2568.OilSealSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_2572.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]':
        '''List[PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_2572.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def planet_carriers(self) -> 'List[_2575.PlanetCarrierSteadyStateSynchronousResponseOnAShaft]':
        '''List[PlanetCarrierSteadyStateSynchronousResponseOnAShaft]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_2575.PlanetCarrierSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def point_loads(self) -> 'List[_2576.PointLoadSteadyStateSynchronousResponseOnAShaft]':
        '''List[PointLoadSteadyStateSynchronousResponseOnAShaft]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2576.PointLoadSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def power_loads(self) -> 'List[_2577.PowerLoadSteadyStateSynchronousResponseOnAShaft]':
        '''List[PowerLoadSteadyStateSynchronousResponseOnAShaft]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2577.PowerLoadSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2583.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft]':
        '''List[ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2583.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2579.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft]':
        '''List[RollingRingAssemblySteadyStateSynchronousResponseOnAShaft]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_2579.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def shafts(self) -> 'List[_2584.ShaftSteadyStateSynchronousResponseOnAShaft]':
        '''List[ShaftSteadyStateSynchronousResponseOnAShaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2584.ShaftSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2588.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2588.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def spring_dampers(self) -> 'List[_2592.SpringDamperSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpringDamperSteadyStateSynchronousResponseOnAShaft]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_2592.SpringDamperSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_2595.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2598.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2598.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def synchronisers(self) -> 'List[_2605.SynchroniserSteadyStateSynchronousResponseOnAShaft]':
        '''List[SynchroniserSteadyStateSynchronousResponseOnAShaft]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_2605.SynchroniserSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def torque_converters(self) -> 'List[_2608.TorqueConverterSteadyStateSynchronousResponseOnAShaft]':
        '''List[TorqueConverterSteadyStateSynchronousResponseOnAShaft]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_2608.TorqueConverterSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2610.UnbalancedMassSteadyStateSynchronousResponseOnAShaft]':
        '''List[UnbalancedMassSteadyStateSynchronousResponseOnAShaft]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_2610.UnbalancedMassSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2613.WormGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[WormGearSetSteadyStateSynchronousResponseOnAShaft]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2613.WormGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2616.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_2616.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft))
        return value
