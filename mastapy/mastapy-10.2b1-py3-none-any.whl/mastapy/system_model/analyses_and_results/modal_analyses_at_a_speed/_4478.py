'''_4478.py

AssemblyModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6073
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
    _4479, _4481, _4484, _4491,
    _4490, _4494, _4499, _4502,
    _4512, _4516, _4522, _4523,
    _4530, _4531, _4538, _4541,
    _4542, _4543, _4546, _4550,
    _4553, _4554, _4555, _4561,
    _4557, _4562, _4567, _4570,
    _4573, _4576, _4580, _4584,
    _4587, _4591, _4594, _4473
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'AssemblyModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyModalAnalysisAtASpeed',)


class AssemblyModalAnalysisAtASpeed(_4473.AbstractAssemblyModalAnalysisAtASpeed):
    '''AssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyModalAnalysisAtASpeed.TYPE'):
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
    def bearings(self) -> 'List[_4479.BearingModalAnalysisAtASpeed]':
        '''List[BearingModalAnalysisAtASpeed]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4479.BearingModalAnalysisAtASpeed))
        return value

    @property
    def belt_drives(self) -> 'List[_4481.BeltDriveModalAnalysisAtASpeed]':
        '''List[BeltDriveModalAnalysisAtASpeed]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4481.BeltDriveModalAnalysisAtASpeed))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4484.BevelDifferentialGearSetModalAnalysisAtASpeed]':
        '''List[BevelDifferentialGearSetModalAnalysisAtASpeed]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4484.BevelDifferentialGearSetModalAnalysisAtASpeed))
        return value

    @property
    def bolts(self) -> 'List[_4491.BoltModalAnalysisAtASpeed]':
        '''List[BoltModalAnalysisAtASpeed]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4491.BoltModalAnalysisAtASpeed))
        return value

    @property
    def bolted_joints(self) -> 'List[_4490.BoltedJointModalAnalysisAtASpeed]':
        '''List[BoltedJointModalAnalysisAtASpeed]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4490.BoltedJointModalAnalysisAtASpeed))
        return value

    @property
    def clutches(self) -> 'List[_4494.ClutchModalAnalysisAtASpeed]':
        '''List[ClutchModalAnalysisAtASpeed]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4494.ClutchModalAnalysisAtASpeed))
        return value

    @property
    def concept_couplings(self) -> 'List[_4499.ConceptCouplingModalAnalysisAtASpeed]':
        '''List[ConceptCouplingModalAnalysisAtASpeed]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4499.ConceptCouplingModalAnalysisAtASpeed))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4502.ConceptGearSetModalAnalysisAtASpeed]':
        '''List[ConceptGearSetModalAnalysisAtASpeed]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4502.ConceptGearSetModalAnalysisAtASpeed))
        return value

    @property
    def cv_ts(self) -> 'List[_4512.CVTModalAnalysisAtASpeed]':
        '''List[CVTModalAnalysisAtASpeed]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4512.CVTModalAnalysisAtASpeed))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4516.CylindricalGearSetModalAnalysisAtASpeed]':
        '''List[CylindricalGearSetModalAnalysisAtASpeed]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4516.CylindricalGearSetModalAnalysisAtASpeed))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4522.FaceGearSetModalAnalysisAtASpeed]':
        '''List[FaceGearSetModalAnalysisAtASpeed]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4522.FaceGearSetModalAnalysisAtASpeed))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4523.FlexiblePinAssemblyModalAnalysisAtASpeed]':
        '''List[FlexiblePinAssemblyModalAnalysisAtASpeed]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4523.FlexiblePinAssemblyModalAnalysisAtASpeed))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4530.HypoidGearSetModalAnalysisAtASpeed]':
        '''List[HypoidGearSetModalAnalysisAtASpeed]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4530.HypoidGearSetModalAnalysisAtASpeed))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4531.ImportedFEComponentModalAnalysisAtASpeed]':
        '''List[ImportedFEComponentModalAnalysisAtASpeed]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4531.ImportedFEComponentModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4538.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4538.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4541.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4541.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed))
        return value

    @property
    def mass_discs(self) -> 'List[_4542.MassDiscModalAnalysisAtASpeed]':
        '''List[MassDiscModalAnalysisAtASpeed]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4542.MassDiscModalAnalysisAtASpeed))
        return value

    @property
    def measurement_components(self) -> 'List[_4543.MeasurementComponentModalAnalysisAtASpeed]':
        '''List[MeasurementComponentModalAnalysisAtASpeed]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4543.MeasurementComponentModalAnalysisAtASpeed))
        return value

    @property
    def oil_seals(self) -> 'List[_4546.OilSealModalAnalysisAtASpeed]':
        '''List[OilSealModalAnalysisAtASpeed]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4546.OilSealModalAnalysisAtASpeed))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4550.PartToPartShearCouplingModalAnalysisAtASpeed]':
        '''List[PartToPartShearCouplingModalAnalysisAtASpeed]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4550.PartToPartShearCouplingModalAnalysisAtASpeed))
        return value

    @property
    def planet_carriers(self) -> 'List[_4553.PlanetCarrierModalAnalysisAtASpeed]':
        '''List[PlanetCarrierModalAnalysisAtASpeed]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4553.PlanetCarrierModalAnalysisAtASpeed))
        return value

    @property
    def point_loads(self) -> 'List[_4554.PointLoadModalAnalysisAtASpeed]':
        '''List[PointLoadModalAnalysisAtASpeed]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4554.PointLoadModalAnalysisAtASpeed))
        return value

    @property
    def power_loads(self) -> 'List[_4555.PowerLoadModalAnalysisAtASpeed]':
        '''List[PowerLoadModalAnalysisAtASpeed]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4555.PowerLoadModalAnalysisAtASpeed))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4561.ShaftHubConnectionModalAnalysisAtASpeed]':
        '''List[ShaftHubConnectionModalAnalysisAtASpeed]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4561.ShaftHubConnectionModalAnalysisAtASpeed))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4557.RollingRingAssemblyModalAnalysisAtASpeed]':
        '''List[RollingRingAssemblyModalAnalysisAtASpeed]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4557.RollingRingAssemblyModalAnalysisAtASpeed))
        return value

    @property
    def shafts(self) -> 'List[_4562.ShaftModalAnalysisAtASpeed]':
        '''List[ShaftModalAnalysisAtASpeed]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4562.ShaftModalAnalysisAtASpeed))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4567.SpiralBevelGearSetModalAnalysisAtASpeed]':
        '''List[SpiralBevelGearSetModalAnalysisAtASpeed]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4567.SpiralBevelGearSetModalAnalysisAtASpeed))
        return value

    @property
    def spring_dampers(self) -> 'List[_4570.SpringDamperModalAnalysisAtASpeed]':
        '''List[SpringDamperModalAnalysisAtASpeed]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4570.SpringDamperModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4573.StraightBevelDiffGearSetModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearSetModalAnalysisAtASpeed]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4573.StraightBevelDiffGearSetModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4576.StraightBevelGearSetModalAnalysisAtASpeed]':
        '''List[StraightBevelGearSetModalAnalysisAtASpeed]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4576.StraightBevelGearSetModalAnalysisAtASpeed))
        return value

    @property
    def synchronisers(self) -> 'List[_4580.SynchroniserModalAnalysisAtASpeed]':
        '''List[SynchroniserModalAnalysisAtASpeed]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4580.SynchroniserModalAnalysisAtASpeed))
        return value

    @property
    def torque_converters(self) -> 'List[_4584.TorqueConverterModalAnalysisAtASpeed]':
        '''List[TorqueConverterModalAnalysisAtASpeed]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4584.TorqueConverterModalAnalysisAtASpeed))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4587.UnbalancedMassModalAnalysisAtASpeed]':
        '''List[UnbalancedMassModalAnalysisAtASpeed]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4587.UnbalancedMassModalAnalysisAtASpeed))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4591.WormGearSetModalAnalysisAtASpeed]':
        '''List[WormGearSetModalAnalysisAtASpeed]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4591.WormGearSetModalAnalysisAtASpeed))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4594.ZerolBevelGearSetModalAnalysisAtASpeed]':
        '''List[ZerolBevelGearSetModalAnalysisAtASpeed]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4594.ZerolBevelGearSetModalAnalysisAtASpeed))
        return value
