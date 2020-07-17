'''_5275.py

AssemblyGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6073
from mastapy.system_model.analyses_and_results.system_deflections import _2230
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5340, _5276, _5278, _5281,
    _5288, _5287, _5290, _5296,
    _5300, _5310, _5314, _5332,
    _5333, _5349, _5350, _5357,
    _5360, _5361, _5362, _5364,
    _5367, _5372, _5373, _5374,
    _5381, _5376, _5380, _5388,
    _5390, _5394, _5397, _5400,
    _5405, _5409, _5413, _5416,
    _5269
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'AssemblyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyGearWhineAnalysis',)


class AssemblyGearWhineAnalysis(_5269.AbstractAssemblyGearWhineAnalysis):
    '''AssemblyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyGearWhineAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2230.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2230.AssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def loaded_gear_sets(self) -> 'List[_5340.GearSetGearWhineAnalysis]':
        '''List[GearSetGearWhineAnalysis]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadedGearSets, constructor.new(_5340.GearSetGearWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5276.BearingGearWhineAnalysis]':
        '''List[BearingGearWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5276.BearingGearWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5278.BeltDriveGearWhineAnalysis]':
        '''List[BeltDriveGearWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5278.BeltDriveGearWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5281.BevelDifferentialGearSetGearWhineAnalysis]':
        '''List[BevelDifferentialGearSetGearWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5281.BevelDifferentialGearSetGearWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5288.BoltGearWhineAnalysis]':
        '''List[BoltGearWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5288.BoltGearWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5287.BoltedJointGearWhineAnalysis]':
        '''List[BoltedJointGearWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5287.BoltedJointGearWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5290.ClutchGearWhineAnalysis]':
        '''List[ClutchGearWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5290.ClutchGearWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5296.ConceptCouplingGearWhineAnalysis]':
        '''List[ConceptCouplingGearWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5296.ConceptCouplingGearWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5300.ConceptGearSetGearWhineAnalysis]':
        '''List[ConceptGearSetGearWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5300.ConceptGearSetGearWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5310.CVTGearWhineAnalysis]':
        '''List[CVTGearWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5310.CVTGearWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5314.CylindricalGearSetGearWhineAnalysis]':
        '''List[CylindricalGearSetGearWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5314.CylindricalGearSetGearWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5332.FaceGearSetGearWhineAnalysis]':
        '''List[FaceGearSetGearWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5332.FaceGearSetGearWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5333.FlexiblePinAssemblyGearWhineAnalysis]':
        '''List[FlexiblePinAssemblyGearWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5333.FlexiblePinAssemblyGearWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5349.HypoidGearSetGearWhineAnalysis]':
        '''List[HypoidGearSetGearWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5349.HypoidGearSetGearWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5350.ImportedFEComponentGearWhineAnalysis]':
        '''List[ImportedFEComponentGearWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5350.ImportedFEComponentGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5361.MassDiscGearWhineAnalysis]':
        '''List[MassDiscGearWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5361.MassDiscGearWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5362.MeasurementComponentGearWhineAnalysis]':
        '''List[MeasurementComponentGearWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5362.MeasurementComponentGearWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5364.OilSealGearWhineAnalysis]':
        '''List[OilSealGearWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5364.OilSealGearWhineAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5367.PartToPartShearCouplingGearWhineAnalysis]':
        '''List[PartToPartShearCouplingGearWhineAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5367.PartToPartShearCouplingGearWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5372.PlanetCarrierGearWhineAnalysis]':
        '''List[PlanetCarrierGearWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5372.PlanetCarrierGearWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5373.PointLoadGearWhineAnalysis]':
        '''List[PointLoadGearWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5373.PointLoadGearWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5374.PowerLoadGearWhineAnalysis]':
        '''List[PowerLoadGearWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5374.PowerLoadGearWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5381.ShaftHubConnectionGearWhineAnalysis]':
        '''List[ShaftHubConnectionGearWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5381.ShaftHubConnectionGearWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5376.RollingRingAssemblyGearWhineAnalysis]':
        '''List[RollingRingAssemblyGearWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5376.RollingRingAssemblyGearWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5380.ShaftGearWhineAnalysis]':
        '''List[ShaftGearWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5380.ShaftGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5388.SpiralBevelGearSetGearWhineAnalysis]':
        '''List[SpiralBevelGearSetGearWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5388.SpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5390.SpringDamperGearWhineAnalysis]':
        '''List[SpringDamperGearWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5390.SpringDamperGearWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5394.StraightBevelDiffGearSetGearWhineAnalysis]':
        '''List[StraightBevelDiffGearSetGearWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5394.StraightBevelDiffGearSetGearWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5397.StraightBevelGearSetGearWhineAnalysis]':
        '''List[StraightBevelGearSetGearWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5397.StraightBevelGearSetGearWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5400.SynchroniserGearWhineAnalysis]':
        '''List[SynchroniserGearWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5400.SynchroniserGearWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5405.TorqueConverterGearWhineAnalysis]':
        '''List[TorqueConverterGearWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5405.TorqueConverterGearWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5409.UnbalancedMassGearWhineAnalysis]':
        '''List[UnbalancedMassGearWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5409.UnbalancedMassGearWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5413.WormGearSetGearWhineAnalysis]':
        '''List[WormGearSetGearWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5413.WormGearSetGearWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5416.ZerolBevelGearSetGearWhineAnalysis]':
        '''List[ZerolBevelGearSetGearWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5416.ZerolBevelGearSetGearWhineAnalysis))
        return value
