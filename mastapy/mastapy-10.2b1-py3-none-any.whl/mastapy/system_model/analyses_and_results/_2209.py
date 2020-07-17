'''_2209.py

CompoundGearWhineAnalysisAnalysis
'''


from typing import Iterable

from mastapy.system_model.part_model import (
    _1996, _1997, _2000, _2002,
    _2003, _2004, _2007, _2008,
    _2011, _2012, _1995, _2013,
    _2016, _2020, _2021, _2022,
    _2024, _2026, _2027, _2029,
    _2030, _2032, _2034, _2035,
    _2036
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import (
    _5685, _5686, _5691, _5702,
    _5703, _5708, _5719, _5730,
    _5731, _5735, _5690, _5739,
    _5743, _5754, _5755, _5756,
    _5757, _5758, _5764, _5765,
    _5766, _5771, _5775, _5798,
    _5799, _5772, _5712, _5714,
    _5732, _5734, _5687, _5689,
    _5694, _5696, _5697, _5698,
    _5699, _5701, _5715, _5717,
    _5726, _5728, _5729, _5736,
    _5738, _5740, _5742, _5745,
    _5747, _5748, _5750, _5751,
    _5753, _5763, _5776, _5778,
    _5782, _5784, _5785, _5787,
    _5788, _5789, _5800, _5802,
    _5803, _5805, _5759, _5761,
    _5693, _5704, _5706, _5709,
    _5711, _5720, _5722, _5724,
    _5725, _5767, _5773, _5769,
    _5768, _5779, _5781, _5790,
    _5791, _5792, _5793, _5794,
    _5796, _5797, _5723, _5692,
    _5707, _5718, _5744, _5762,
    _5770, _5774, _5695, _5713,
    _5733, _5783, _5700, _5716,
    _5688, _5727, _5741, _5746,
    _5749, _5752, _5777, _5786,
    _5801, _5804, _5737, _5760,
    _5705, _5710, _5721, _5780,
    _5795
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2039
from mastapy.system_model.part_model.gears import (
    _2077, _2078, _2084, _2085,
    _2069, _2070, _2071, _2072,
    _2073, _2074, _2075, _2076,
    _2079, _2080, _2081, _2082,
    _2083, _2086, _2088, _2090,
    _2091, _2092, _2093, _2094,
    _2095, _2096, _2097, _2098,
    _2099, _2100, _2101, _2102,
    _2103, _2104, _2105, _2106,
    _2107, _2108, _2109, _2110
)
from mastapy.system_model.part_model.couplings import (
    _2139, _2140, _2128, _2130,
    _2131, _2133, _2134, _2135,
    _2136, _2137, _2138, _2141,
    _2149, _2147, _2148, _2150,
    _2151, _2152, _2154, _2155,
    _2156, _2157, _2158, _2160
)
from mastapy.system_model.connections_and_sockets import (
    _1852, _1847, _1848, _1851,
    _1860, _1863, _1867, _1871
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1877, _1881, _1887, _1901,
    _1879, _1883, _1875, _1885,
    _1891, _1894, _1895, _1896,
    _1899, _1903, _1905, _1907,
    _1889
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1915, _1909, _1911, _1913,
    _1917, _1919
)
from mastapy.system_model.analyses_and_results import _2169
from mastapy._internal.python_net import python_net_import

_COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundGearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundGearWhineAnalysisAnalysis',)


class CompoundGearWhineAnalysisAnalysis(_2169.CompoundAnalysis):
    '''CompoundGearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundGearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> 'Iterable[_5685.AbstractAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5685.AbstractAssemblyCompoundGearWhineAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> 'Iterable[_5686.AbstractShaftOrHousingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractShaftOrHousingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5686.AbstractShaftOrHousingCompoundGearWhineAnalysis))

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> 'Iterable[_5691.BearingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BearingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5691.BearingCompoundGearWhineAnalysis))

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> 'Iterable[_5702.BoltCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5702.BoltCompoundGearWhineAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> 'Iterable[_5703.BoltedJointCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltedJointCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5703.BoltedJointCompoundGearWhineAnalysis))

    def results_for_component(self, design_entity: '_2004.Component') -> 'Iterable[_5708.ComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5708.ComponentCompoundGearWhineAnalysis))

    def results_for_connector(self, design_entity: '_2007.Connector') -> 'Iterable[_5719.ConnectorCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectorCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5719.ConnectorCompoundGearWhineAnalysis))

    def results_for_datum(self, design_entity: '_2008.Datum') -> 'Iterable[_5730.DatumCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.DatumCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5730.DatumCompoundGearWhineAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> 'Iterable[_5731.ExternalCADModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ExternalCADModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5731.ExternalCADModelCompoundGearWhineAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> 'Iterable[_5735.FlexiblePinAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FlexiblePinAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5735.FlexiblePinAssemblyCompoundGearWhineAnalysis))

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> 'Iterable[_5690.AssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5690.AssemblyCompoundGearWhineAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> 'Iterable[_5739.GuideDxfModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GuideDxfModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5739.GuideDxfModelCompoundGearWhineAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> 'Iterable[_5743.ImportedFEComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ImportedFEComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5743.ImportedFEComponentCompoundGearWhineAnalysis))

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> 'Iterable[_5754.MassDiscCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MassDiscCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5754.MassDiscCompoundGearWhineAnalysis))

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> 'Iterable[_5755.MeasurementComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MeasurementComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5755.MeasurementComponentCompoundGearWhineAnalysis))

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> 'Iterable[_5756.MountableComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MountableComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5756.MountableComponentCompoundGearWhineAnalysis))

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> 'Iterable[_5757.OilSealCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.OilSealCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5757.OilSealCompoundGearWhineAnalysis))

    def results_for_part(self, design_entity: '_2026.Part') -> 'Iterable[_5758.PartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5758.PartCompoundGearWhineAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> 'Iterable[_5764.PlanetCarrierCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetCarrierCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5764.PlanetCarrierCompoundGearWhineAnalysis))

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> 'Iterable[_5765.PointLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PointLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5765.PointLoadCompoundGearWhineAnalysis))

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> 'Iterable[_5766.PowerLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PowerLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5766.PowerLoadCompoundGearWhineAnalysis))

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> 'Iterable[_5771.RootAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RootAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5771.RootAssemblyCompoundGearWhineAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> 'Iterable[_5775.SpecialisedAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpecialisedAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5775.SpecialisedAssemblyCompoundGearWhineAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> 'Iterable[_5798.UnbalancedMassCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.UnbalancedMassCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5798.UnbalancedMassCompoundGearWhineAnalysis))

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> 'Iterable[_5799.VirtualComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.VirtualComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5799.VirtualComponentCompoundGearWhineAnalysis))

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> 'Iterable[_5772.ShaftCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5772.ShaftCompoundGearWhineAnalysis))

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> 'Iterable[_5712.ConceptGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5712.ConceptGearCompoundGearWhineAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> 'Iterable[_5714.ConceptGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5714.ConceptGearSetCompoundGearWhineAnalysis))

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> 'Iterable[_5732.FaceGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5732.FaceGearCompoundGearWhineAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> 'Iterable[_5734.FaceGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5734.FaceGearSetCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> 'Iterable[_5687.AGMAGleasonConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5687.AGMAGleasonConicalGearCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> 'Iterable[_5689.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5689.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> 'Iterable[_5694.BevelDifferentialGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5694.BevelDifferentialGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> 'Iterable[_5696.BevelDifferentialGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5696.BevelDifferentialGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> 'Iterable[_5697.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5697.BevelDifferentialPlanetGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> 'Iterable[_5698.BevelDifferentialSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5698.BevelDifferentialSunGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> 'Iterable[_5699.BevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5699.BevelGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> 'Iterable[_5701.BevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5701.BevelGearSetCompoundGearWhineAnalysis))

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> 'Iterable[_5715.ConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5715.ConicalGearCompoundGearWhineAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> 'Iterable[_5717.ConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5717.ConicalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> 'Iterable[_5726.CylindricalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5726.CylindricalGearCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> 'Iterable[_5728.CylindricalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5728.CylindricalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> 'Iterable[_5729.CylindricalPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5729.CylindricalPlanetGearCompoundGearWhineAnalysis))

    def results_for_gear(self, design_entity: '_2086.Gear') -> 'Iterable[_5736.GearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5736.GearCompoundGearWhineAnalysis))

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> 'Iterable[_5738.GearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5738.GearSetCompoundGearWhineAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> 'Iterable[_5740.HypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5740.HypoidGearCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> 'Iterable[_5742.HypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5742.HypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5745.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5745.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5747.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5747.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5748.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5748.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5750.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5750.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5751.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5751.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5753.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5753.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> 'Iterable[_5763.PlanetaryGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5763.PlanetaryGearSetCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> 'Iterable[_5776.SpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5776.SpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> 'Iterable[_5778.SpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5778.SpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> 'Iterable[_5782.StraightBevelDiffGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5782.StraightBevelDiffGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> 'Iterable[_5784.StraightBevelDiffGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5784.StraightBevelDiffGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> 'Iterable[_5785.StraightBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5785.StraightBevelGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> 'Iterable[_5787.StraightBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5787.StraightBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> 'Iterable[_5788.StraightBevelPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5788.StraightBevelPlanetGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> 'Iterable[_5789.StraightBevelSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5789.StraightBevelSunGearCompoundGearWhineAnalysis))

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> 'Iterable[_5800.WormGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5800.WormGearCompoundGearWhineAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> 'Iterable[_5802.WormGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5802.WormGearSetCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> 'Iterable[_5803.ZerolBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5803.ZerolBevelGearCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> 'Iterable[_5805.ZerolBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5805.ZerolBevelGearSetCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> 'Iterable[_5759.PartToPartShearCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5759.PartToPartShearCouplingCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> 'Iterable[_5761.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5761.PartToPartShearCouplingHalfCompoundGearWhineAnalysis))

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> 'Iterable[_5693.BeltDriveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltDriveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5693.BeltDriveCompoundGearWhineAnalysis))

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> 'Iterable[_5704.ClutchCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5704.ClutchCompoundGearWhineAnalysis))

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> 'Iterable[_5706.ClutchHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5706.ClutchHalfCompoundGearWhineAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> 'Iterable[_5709.ConceptCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5709.ConceptCouplingCompoundGearWhineAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> 'Iterable[_5711.ConceptCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5711.ConceptCouplingHalfCompoundGearWhineAnalysis))

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> 'Iterable[_5720.CouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5720.CouplingCompoundGearWhineAnalysis))

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> 'Iterable[_5722.CouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5722.CouplingHalfCompoundGearWhineAnalysis))

    def results_for_cvt(self, design_entity: '_2137.CVT') -> 'Iterable[_5724.CVTCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5724.CVTCompoundGearWhineAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> 'Iterable[_5725.CVTPulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTPulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5725.CVTPulleyCompoundGearWhineAnalysis))

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> 'Iterable[_5767.PulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5767.PulleyCompoundGearWhineAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> 'Iterable[_5773.ShaftHubConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftHubConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5773.ShaftHubConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> 'Iterable[_5769.RollingRingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5769.RollingRingCompoundGearWhineAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> 'Iterable[_5768.RollingRingAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5768.RollingRingAssemblyCompoundGearWhineAnalysis))

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> 'Iterable[_5779.SpringDamperCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5779.SpringDamperCompoundGearWhineAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> 'Iterable[_5781.SpringDamperHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5781.SpringDamperHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> 'Iterable[_5790.SynchroniserCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5790.SynchroniserCompoundGearWhineAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> 'Iterable[_5791.SynchroniserHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5791.SynchroniserHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> 'Iterable[_5792.SynchroniserPartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserPartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5792.SynchroniserPartCompoundGearWhineAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> 'Iterable[_5793.SynchroniserSleeveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserSleeveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5793.SynchroniserSleeveCompoundGearWhineAnalysis))

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> 'Iterable[_5794.TorqueConverterCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5794.TorqueConverterCompoundGearWhineAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> 'Iterable[_5796.TorqueConverterPumpCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterPumpCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5796.TorqueConverterPumpCompoundGearWhineAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> 'Iterable[_5797.TorqueConverterTurbineCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterTurbineCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5797.TorqueConverterTurbineCompoundGearWhineAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> 'Iterable[_5723.CVTBeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTBeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5723.CVTBeltConnectionCompoundGearWhineAnalysis))

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> 'Iterable[_5692.BeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5692.BeltConnectionCompoundGearWhineAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> 'Iterable[_5707.CoaxialConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CoaxialConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5707.CoaxialConnectionCompoundGearWhineAnalysis))

    def results_for_connection(self, design_entity: '_1851.Connection') -> 'Iterable[_5718.ConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5718.ConnectionCompoundGearWhineAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> 'Iterable[_5744.InterMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.InterMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5744.InterMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> 'Iterable[_5762.PlanetaryConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5762.PlanetaryConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> 'Iterable[_5770.RollingRingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5770.RollingRingConnectionCompoundGearWhineAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> 'Iterable[_5774.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5774.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> 'Iterable[_5695.BevelDifferentialGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5695.BevelDifferentialGearMeshCompoundGearWhineAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> 'Iterable[_5713.ConceptGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5713.ConceptGearMeshCompoundGearWhineAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> 'Iterable[_5733.FaceGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5733.FaceGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> 'Iterable[_5783.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5783.StraightBevelDiffGearMeshCompoundGearWhineAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> 'Iterable[_5700.BevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5700.BevelGearMeshCompoundGearWhineAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> 'Iterable[_5716.ConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5716.ConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> 'Iterable[_5688.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5688.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> 'Iterable[_5727.CylindricalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5727.CylindricalGearMeshCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> 'Iterable[_5741.HypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5741.HypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5746.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5746.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5749.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5749.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5752.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5752.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> 'Iterable[_5777.SpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5777.SpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> 'Iterable[_5786.StraightBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5786.StraightBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> 'Iterable[_5801.WormGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5801.WormGearMeshCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> 'Iterable[_5804.ZerolBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5804.ZerolBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> 'Iterable[_5737.GearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5737.GearMeshCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> 'Iterable[_5760.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5760.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> 'Iterable[_5705.ClutchConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5705.ClutchConnectionCompoundGearWhineAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> 'Iterable[_5710.ConceptCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5710.ConceptCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> 'Iterable[_5721.CouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5721.CouplingConnectionCompoundGearWhineAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> 'Iterable[_5780.SpringDamperConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5780.SpringDamperConnectionCompoundGearWhineAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> 'Iterable[_5795.TorqueConverterConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_5795.TorqueConverterConnectionCompoundGearWhineAnalysis))
