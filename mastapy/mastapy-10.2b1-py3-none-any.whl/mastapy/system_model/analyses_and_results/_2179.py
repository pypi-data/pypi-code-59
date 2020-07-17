'''_2179.py

GearWhineAnalysisAnalysis
'''


from mastapy.system_model.analyses_and_results.static_loads import (
    _6231, _6232, _6234, _6178,
    _6177, _6076, _6089, _6088,
    _6094, _6093, _6107, _6106,
    _6109, _6110, _6187, _6193,
    _6191, _6189, _6203, _6202,
    _6214, _6213, _6215, _6216,
    _6220, _6221, _6222, _6108,
    _6075, _6090, _6103, _6158,
    _6179, _6190, _6195, _6078,
    _6096, _6134, _6206, _6083,
    _6100, _6070, _6113, _6154,
    _6160, _6163, _6166, _6199,
    _6209, _6230, _6233, _6140,
    _6176, _6087, _6092, _6105,
    _6201, _6219, _6066, _6067,
    _6074, _6086, _6085, _6091,
    _6104, _6119, _6132, _6136,
    _6073, _6144, _6156, _6168,
    _6169, _6171, _6173, _6175,
    _6182, _6185, _6186, _6192,
    _6196, _6227, _6228, _6194,
    _6095, _6097, _6133, _6135,
    _6069, _6071, _6077, _6079,
    _6080, _6081, _6082, _6084,
    _6098, _6102, _6111, _6115,
    _6116, _6138, _6143, _6153,
    _6155, _6159, _6161, _6162,
    _6164, _6165, _6167, _6180,
    _6198, _6200, _6205, _6207,
    _6208, _6210, _6211, _6212,
    _6229
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5413, _5414, _5416, _5367,
    _5368, _5278, _5290, _5291,
    _5296, _5297, _5307, _5308,
    _5310, _5311, _5375, _5381,
    _5378, _5376, _5390, _5391,
    _5400, _5401, _5402, _5403,
    _5405, _5406, _5407, _5309,
    _5277, _5292, _5304, _5351,
    _5370, _5377, _5382, _5280,
    _5299, _5331, _5393, _5285,
    _5302, _5273, _5313, _5348,
    _5353, _5356, _5359, _5387,
    _5396, _5412, _5415, _5337,
    _5366, _5289, _5295, _5306,
    _5389, _5404, _5269, _5271,
    _5276, _5288, _5287, _5294,
    _5305, _5316, _5329, _5333,
    _5275, _5345, _5350, _5361,
    _5362, _5363, _5364, _5365,
    _5372, _5373, _5374, _5379,
    _5384, _5409, _5410, _5380,
    _5298, _5300, _5330, _5332,
    _5272, _5274, _5279, _5281,
    _5282, _5283, _5284, _5286,
    _5301, _5303, _5312, _5314,
    _5315, _5335, _5340, _5347,
    _5349, _5352, _5354, _5355,
    _5357, _5358, _5360, _5371,
    _5386, _5388, _5392, _5394,
    _5395, _5397, _5398, _5399,
    _5411
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2109, _2110, _2077, _2078,
    _2084, _2085, _2069, _2070,
    _2071, _2072, _2073, _2074,
    _2075, _2076, _2079, _2080,
    _2081, _2082, _2083, _2086,
    _2088, _2090, _2091, _2092,
    _2093, _2094, _2095, _2096,
    _2097, _2098, _2099, _2100,
    _2101, _2102, _2103, _2104,
    _2105, _2106, _2107, _2108
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
from mastapy.system_model.part_model import (
    _1996, _1997, _2000, _2002,
    _2003, _2004, _2007, _2008,
    _2011, _2012, _1995, _2013,
    _2016, _2020, _2021, _2022,
    _2024, _2026, _2027, _2029,
    _2030, _2032, _2034, _2035,
    _2036
)
from mastapy.system_model.part_model.shaft_model import _2039
from mastapy.system_model.analyses_and_results import _2170
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'GearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisAnalysis',)


class GearWhineAnalysisAnalysis(_2170.SingleAnalysis):
    '''GearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6231.WormGearSetLoadCase') -> '_5413.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5413.WormGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> '_5414.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5414.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6232.ZerolBevelGearLoadCase') -> '_5414.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5414.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> '_5416.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5416.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6234.ZerolBevelGearSetLoadCase') -> '_5416.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5416.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> '_5367.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5367.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6178.PartToPartShearCouplingLoadCase') -> '_5367.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5367.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> '_5368.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5368.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6177.PartToPartShearCouplingHalfLoadCase') -> '_5368.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5368.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> '_5278.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5278.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6076.BeltDriveLoadCase') -> '_5278.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5278.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> '_5290.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5290.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6089.ClutchLoadCase') -> '_5290.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5290.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> '_5291.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5291.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6088.ClutchHalfLoadCase') -> '_5291.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5291.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> '_5296.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5296.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6094.ConceptCouplingLoadCase') -> '_5296.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5296.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> '_5297.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5297.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6093.ConceptCouplingHalfLoadCase') -> '_5297.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5297.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> '_5307.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5307.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6107.CouplingLoadCase') -> '_5307.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5307.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> '_5308.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5308.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6106.CouplingHalfLoadCase') -> '_5308.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5308.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2137.CVT') -> '_5310.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5310.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6109.CVTLoadCase') -> '_5310.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5310.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> '_5311.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5311.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6110.CVTPulleyLoadCase') -> '_5311.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5311.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> '_5375.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5375.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6187.PulleyLoadCase') -> '_5375.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5375.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> '_5381.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5381.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6193.ShaftHubConnectionLoadCase') -> '_5381.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5381.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> '_5378.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5378.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6191.RollingRingLoadCase') -> '_5378.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5378.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> '_5376.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5376.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6189.RollingRingAssemblyLoadCase') -> '_5376.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5376.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> '_5390.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5390.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6203.SpringDamperLoadCase') -> '_5390.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5390.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> '_5391.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5391.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6202.SpringDamperHalfLoadCase') -> '_5391.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5391.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> '_5400.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5400.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6214.SynchroniserLoadCase') -> '_5400.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5400.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> '_5401.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5401.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6213.SynchroniserHalfLoadCase') -> '_5401.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5401.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> '_5402.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5402.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6215.SynchroniserPartLoadCase') -> '_5402.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5402.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> '_5403.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5403.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6216.SynchroniserSleeveLoadCase') -> '_5403.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5403.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> '_5405.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5405.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6220.TorqueConverterLoadCase') -> '_5405.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5405.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> '_5406.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5406.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6221.TorqueConverterPumpLoadCase') -> '_5406.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5406.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> '_5407.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5407.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6222.TorqueConverterTurbineLoadCase') -> '_5407.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5407.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> '_5309.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5309.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6108.CVTBeltConnectionLoadCase') -> '_5309.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5309.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> '_5277.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5277.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6075.BeltConnectionLoadCase') -> '_5277.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5277.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> '_5292.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5292.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6090.CoaxialConnectionLoadCase') -> '_5292.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5292.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1851.Connection') -> '_5304.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5304.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6103.ConnectionLoadCase') -> '_5304.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5304.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> '_5351.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5351.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6158.InterMountableComponentConnectionLoadCase') -> '_5351.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5351.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> '_5370.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5370.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6179.PlanetaryConnectionLoadCase') -> '_5370.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5370.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> '_5377.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5377.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6190.RollingRingConnectionLoadCase') -> '_5377.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5377.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> '_5382.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5382.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6195.ShaftToMountableComponentConnectionLoadCase') -> '_5382.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5382.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> '_5280.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5280.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6078.BevelDifferentialGearMeshLoadCase') -> '_5280.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5280.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> '_5299.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5299.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6096.ConceptGearMeshLoadCase') -> '_5299.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5299.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> '_5331.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5331.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6134.FaceGearMeshLoadCase') -> '_5331.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5331.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> '_5393.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5393.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6206.StraightBevelDiffGearMeshLoadCase') -> '_5393.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5393.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> '_5285.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5285.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6083.BevelGearMeshLoadCase') -> '_5285.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5285.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> '_5302.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5302.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6100.ConicalGearMeshLoadCase') -> '_5302.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5302.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> '_5273.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5273.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6070.AGMAGleasonConicalGearMeshLoadCase') -> '_5273.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5273.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> '_5313.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5313.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6113.CylindricalGearMeshLoadCase') -> '_5313.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5313.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> '_5348.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5348.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6154.HypoidGearMeshLoadCase') -> '_5348.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5348.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> '_5353.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5353.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6160.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5353.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5353.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5356.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5356.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6163.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5356.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5356.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5359.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5359.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5359.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5359.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> '_5387.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5387.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6199.SpiralBevelGearMeshLoadCase') -> '_5387.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5387.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> '_5396.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5396.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6209.StraightBevelGearMeshLoadCase') -> '_5396.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5396.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> '_5412.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5412.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6230.WormGearMeshLoadCase') -> '_5412.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5412.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> '_5415.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5415.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6233.ZerolBevelGearMeshLoadCase') -> '_5415.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5415.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> '_5337.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5337.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6140.GearMeshLoadCase') -> '_5337.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5337.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> '_5366.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5366.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6176.PartToPartShearCouplingConnectionLoadCase') -> '_5366.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5366.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> '_5289.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5289.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6087.ClutchConnectionLoadCase') -> '_5289.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5289.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> '_5295.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5295.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6092.ConceptCouplingConnectionLoadCase') -> '_5295.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5295.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> '_5306.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5306.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6105.CouplingConnectionLoadCase') -> '_5306.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5306.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> '_5389.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5389.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6201.SpringDamperConnectionLoadCase') -> '_5389.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5389.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> '_5404.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5404.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6219.TorqueConverterConnectionLoadCase') -> '_5404.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5404.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> '_5269.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5269.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6066.AbstractAssemblyLoadCase') -> '_5269.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5269.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> '_5271.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5271.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6067.AbstractShaftOrHousingLoadCase') -> '_5271.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5271.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> '_5276.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5276.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6074.BearingLoadCase') -> '_5276.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5276.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> '_5288.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5288.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6086.BoltLoadCase') -> '_5288.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5288.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> '_5287.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5287.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6085.BoltedJointLoadCase') -> '_5287.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5287.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2004.Component') -> '_5294.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5294.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6091.ComponentLoadCase') -> '_5294.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5294.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2007.Connector') -> '_5305.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5305.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6104.ConnectorLoadCase') -> '_5305.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5305.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2008.Datum') -> '_5316.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5316.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6119.DatumLoadCase') -> '_5316.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5316.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> '_5329.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5329.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6132.ExternalCADModelLoadCase') -> '_5329.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5329.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> '_5333.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5333.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6136.FlexiblePinAssemblyLoadCase') -> '_5333.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5333.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> '_5275.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5275.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6073.AssemblyLoadCase') -> '_5275.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5275.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> '_5345.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5345.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6144.GuideDxfModelLoadCase') -> '_5345.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5345.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> '_5350.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5350.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6156.ImportedFEComponentLoadCase') -> '_5350.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5350.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> '_5361.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5361.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6168.MassDiscLoadCase') -> '_5361.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5361.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> '_5362.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5362.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6169.MeasurementComponentLoadCase') -> '_5362.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5362.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> '_5363.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5363.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6171.MountableComponentLoadCase') -> '_5363.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5363.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> '_5364.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5364.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6173.OilSealLoadCase') -> '_5364.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5364.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2026.Part') -> '_5365.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5365.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6175.PartLoadCase') -> '_5365.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5365.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> '_5372.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5372.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6182.PlanetCarrierLoadCase') -> '_5372.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5372.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> '_5373.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5373.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6185.PointLoadLoadCase') -> '_5373.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5373.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> '_5374.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5374.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6186.PowerLoadLoadCase') -> '_5374.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5374.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> '_5379.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5379.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6192.RootAssemblyLoadCase') -> '_5379.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5379.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> '_5384.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5384.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6196.SpecialisedAssemblyLoadCase') -> '_5384.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5384.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> '_5409.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5409.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6227.UnbalancedMassLoadCase') -> '_5409.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5409.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> '_5410.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5410.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6228.VirtualComponentLoadCase') -> '_5410.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5410.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> '_5380.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5380.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6194.ShaftLoadCase') -> '_5380.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5380.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> '_5298.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5298.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6095.ConceptGearLoadCase') -> '_5298.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5298.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> '_5300.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5300.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6097.ConceptGearSetLoadCase') -> '_5300.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5300.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> '_5330.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5330.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6133.FaceGearLoadCase') -> '_5330.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5330.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> '_5332.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5332.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6135.FaceGearSetLoadCase') -> '_5332.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5332.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> '_5272.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5272.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6069.AGMAGleasonConicalGearLoadCase') -> '_5272.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5272.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> '_5274.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5274.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6071.AGMAGleasonConicalGearSetLoadCase') -> '_5274.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5274.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> '_5279.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5279.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6077.BevelDifferentialGearLoadCase') -> '_5279.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5279.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> '_5281.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5281.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6079.BevelDifferentialGearSetLoadCase') -> '_5281.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5281.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> '_5282.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5282.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6080.BevelDifferentialPlanetGearLoadCase') -> '_5282.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5282.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> '_5283.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5283.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6081.BevelDifferentialSunGearLoadCase') -> '_5283.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5283.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> '_5284.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5284.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6082.BevelGearLoadCase') -> '_5284.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5284.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> '_5286.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5286.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6084.BevelGearSetLoadCase') -> '_5286.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5286.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> '_5301.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5301.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6098.ConicalGearLoadCase') -> '_5301.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5301.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> '_5303.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5303.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6102.ConicalGearSetLoadCase') -> '_5303.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5303.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> '_5312.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5312.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6111.CylindricalGearLoadCase') -> '_5312.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5312.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> '_5314.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5314.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6115.CylindricalGearSetLoadCase') -> '_5314.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5314.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> '_5315.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5315.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6116.CylindricalPlanetGearLoadCase') -> '_5315.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5315.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2086.Gear') -> '_5335.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5335.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6138.GearLoadCase') -> '_5335.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5335.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> '_5340.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5340.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6143.GearSetLoadCase') -> '_5340.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5340.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> '_5347.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5347.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6153.HypoidGearLoadCase') -> '_5347.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5347.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> '_5349.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5349.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6155.HypoidGearSetLoadCase') -> '_5349.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5349.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> '_5352.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5352.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6159.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5352.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5352.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> '_5354.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5354.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6161.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5354.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5354.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> '_5355.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5355.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6162.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5355.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5355.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> '_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5357.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5358.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5358.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5358.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5358.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5360.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> '_5371.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5371.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6180.PlanetaryGearSetLoadCase') -> '_5371.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5371.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> '_5386.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5386.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6198.SpiralBevelGearLoadCase') -> '_5386.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5386.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> '_5388.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5388.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6200.SpiralBevelGearSetLoadCase') -> '_5388.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5388.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> '_5392.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5392.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6205.StraightBevelDiffGearLoadCase') -> '_5392.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5392.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> '_5394.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5394.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6207.StraightBevelDiffGearSetLoadCase') -> '_5394.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5394.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> '_5395.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5395.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6208.StraightBevelGearLoadCase') -> '_5395.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5395.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> '_5397.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5397.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6210.StraightBevelGearSetLoadCase') -> '_5397.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5397.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> '_5398.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5398.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6211.StraightBevelPlanetGearLoadCase') -> '_5398.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5398.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> '_5399.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5399.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelSunGearLoadCase') -> '_5399.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5399.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> '_5411.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5411.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6229.WormGearLoadCase') -> '_5411.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5411.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> '_5413.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5413.WormGearSetGearWhineAnalysis)(method_result) if method_result else None
