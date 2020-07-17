'''_2174.py

DynamicAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.dynamic_analyses import (
    _5934, _5935, _5937, _5892,
    _5893, _5823, _5835, _5836,
    _5840, _5841, _5851, _5852,
    _5854, _5855, _5899, _5905,
    _5902, _5900, _5912, _5913,
    _5922, _5923, _5924, _5925,
    _5927, _5928, _5929, _5853,
    _5822, _5837, _5848, _5876,
    _5894, _5901, _5906, _5825,
    _5843, _5865, _5915, _5830,
    _5846, _5818, _5857, _5873,
    _5878, _5881, _5884, _5909,
    _5918, _5933, _5936, _5869,
    _5891, _5834, _5839, _5850,
    _5911, _5926, _5815, _5816,
    _5821, _5832, _5833, _5838,
    _5849, _5860, _5863, _5867,
    _5820, _5871, _5875, _5886,
    _5887, _5888, _5889, _5890,
    _5896, _5897, _5898, _5903,
    _5907, _5930, _5931, _5904,
    _5842, _5844, _5864, _5866,
    _5817, _5819, _5824, _5826,
    _5827, _5828, _5829, _5831,
    _5845, _5847, _5856, _5858,
    _5859, _5868, _5870, _5872,
    _5874, _5877, _5879, _5880,
    _5882, _5883, _5885, _5895,
    _5908, _5910, _5914, _5916,
    _5917, _5919, _5920, _5921,
    _5932
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

_DYNAMIC_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'DynamicAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysisAnalysis',)


class DynamicAnalysisAnalysis(_2170.SingleAnalysis):
    '''DynamicAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6231.WormGearSetLoadCase') -> '_5934.WormGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5934.WormGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> '_5935.ZerolBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5935.ZerolBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6232.ZerolBevelGearLoadCase') -> '_5935.ZerolBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5935.ZerolBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> '_5937.ZerolBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5937.ZerolBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6234.ZerolBevelGearSetLoadCase') -> '_5937.ZerolBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5937.ZerolBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> '_5892.PartToPartShearCouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5892.PartToPartShearCouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6178.PartToPartShearCouplingLoadCase') -> '_5892.PartToPartShearCouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5892.PartToPartShearCouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> '_5893.PartToPartShearCouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5893.PartToPartShearCouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6177.PartToPartShearCouplingHalfLoadCase') -> '_5893.PartToPartShearCouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5893.PartToPartShearCouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> '_5823.BeltDriveDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BeltDriveDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5823.BeltDriveDynamicAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6076.BeltDriveLoadCase') -> '_5823.BeltDriveDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BeltDriveDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5823.BeltDriveDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> '_5835.ClutchDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5835.ClutchDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6089.ClutchLoadCase') -> '_5835.ClutchDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5835.ClutchDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> '_5836.ClutchHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5836.ClutchHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6088.ClutchHalfLoadCase') -> '_5836.ClutchHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5836.ClutchHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> '_5840.ConceptCouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5840.ConceptCouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6094.ConceptCouplingLoadCase') -> '_5840.ConceptCouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5840.ConceptCouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> '_5841.ConceptCouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5841.ConceptCouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6093.ConceptCouplingHalfLoadCase') -> '_5841.ConceptCouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5841.ConceptCouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> '_5851.CouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5851.CouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6107.CouplingLoadCase') -> '_5851.CouplingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5851.CouplingDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> '_5852.CouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5852.CouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6106.CouplingHalfLoadCase') -> '_5852.CouplingHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5852.CouplingHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2137.CVT') -> '_5854.CVTDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5854.CVTDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6109.CVTLoadCase') -> '_5854.CVTDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5854.CVTDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> '_5855.CVTPulleyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5855.CVTPulleyDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6110.CVTPulleyLoadCase') -> '_5855.CVTPulleyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5855.CVTPulleyDynamicAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> '_5899.PulleyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5899.PulleyDynamicAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6187.PulleyLoadCase') -> '_5899.PulleyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5899.PulleyDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> '_5905.ShaftHubConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftHubConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5905.ShaftHubConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6193.ShaftHubConnectionLoadCase') -> '_5905.ShaftHubConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftHubConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5905.ShaftHubConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> '_5902.RollingRingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5902.RollingRingDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6191.RollingRingLoadCase') -> '_5902.RollingRingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5902.RollingRingDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> '_5900.RollingRingAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5900.RollingRingAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6189.RollingRingAssemblyLoadCase') -> '_5900.RollingRingAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5900.RollingRingAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> '_5912.SpringDamperDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5912.SpringDamperDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6203.SpringDamperLoadCase') -> '_5912.SpringDamperDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5912.SpringDamperDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> '_5913.SpringDamperHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5913.SpringDamperHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6202.SpringDamperHalfLoadCase') -> '_5913.SpringDamperHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5913.SpringDamperHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> '_5922.SynchroniserDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5922.SynchroniserDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6214.SynchroniserLoadCase') -> '_5922.SynchroniserDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5922.SynchroniserDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> '_5923.SynchroniserHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5923.SynchroniserHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6213.SynchroniserHalfLoadCase') -> '_5923.SynchroniserHalfDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5923.SynchroniserHalfDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> '_5924.SynchroniserPartDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5924.SynchroniserPartDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6215.SynchroniserPartLoadCase') -> '_5924.SynchroniserPartDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5924.SynchroniserPartDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> '_5925.SynchroniserSleeveDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5925.SynchroniserSleeveDynamicAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6216.SynchroniserSleeveLoadCase') -> '_5925.SynchroniserSleeveDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5925.SynchroniserSleeveDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> '_5927.TorqueConverterDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5927.TorqueConverterDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6220.TorqueConverterLoadCase') -> '_5927.TorqueConverterDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5927.TorqueConverterDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> '_5928.TorqueConverterPumpDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5928.TorqueConverterPumpDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6221.TorqueConverterPumpLoadCase') -> '_5928.TorqueConverterPumpDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5928.TorqueConverterPumpDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> '_5929.TorqueConverterTurbineDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5929.TorqueConverterTurbineDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6222.TorqueConverterTurbineLoadCase') -> '_5929.TorqueConverterTurbineDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5929.TorqueConverterTurbineDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> '_5853.CVTBeltConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5853.CVTBeltConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6108.CVTBeltConnectionLoadCase') -> '_5853.CVTBeltConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5853.CVTBeltConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> '_5822.BeltConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5822.BeltConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6075.BeltConnectionLoadCase') -> '_5822.BeltConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5822.BeltConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> '_5837.CoaxialConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5837.CoaxialConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6090.CoaxialConnectionLoadCase') -> '_5837.CoaxialConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5837.CoaxialConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1851.Connection') -> '_5848.ConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5848.ConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6103.ConnectionLoadCase') -> '_5848.ConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5848.ConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> '_5876.InterMountableComponentConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5876.InterMountableComponentConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6158.InterMountableComponentConnectionLoadCase') -> '_5876.InterMountableComponentConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5876.InterMountableComponentConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> '_5894.PlanetaryConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5894.PlanetaryConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6179.PlanetaryConnectionLoadCase') -> '_5894.PlanetaryConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5894.PlanetaryConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> '_5901.RollingRingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5901.RollingRingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6190.RollingRingConnectionLoadCase') -> '_5901.RollingRingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5901.RollingRingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> '_5906.ShaftToMountableComponentConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5906.ShaftToMountableComponentConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6195.ShaftToMountableComponentConnectionLoadCase') -> '_5906.ShaftToMountableComponentConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5906.ShaftToMountableComponentConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> '_5825.BevelDifferentialGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5825.BevelDifferentialGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6078.BevelDifferentialGearMeshLoadCase') -> '_5825.BevelDifferentialGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5825.BevelDifferentialGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> '_5843.ConceptGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5843.ConceptGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6096.ConceptGearMeshLoadCase') -> '_5843.ConceptGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5843.ConceptGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> '_5865.FaceGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5865.FaceGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6134.FaceGearMeshLoadCase') -> '_5865.FaceGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5865.FaceGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> '_5915.StraightBevelDiffGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5915.StraightBevelDiffGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6206.StraightBevelDiffGearMeshLoadCase') -> '_5915.StraightBevelDiffGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5915.StraightBevelDiffGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> '_5830.BevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5830.BevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6083.BevelGearMeshLoadCase') -> '_5830.BevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5830.BevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> '_5846.ConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5846.ConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6100.ConicalGearMeshLoadCase') -> '_5846.ConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5846.ConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> '_5818.AGMAGleasonConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5818.AGMAGleasonConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6070.AGMAGleasonConicalGearMeshLoadCase') -> '_5818.AGMAGleasonConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5818.AGMAGleasonConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> '_5857.CylindricalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5857.CylindricalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6113.CylindricalGearMeshLoadCase') -> '_5857.CylindricalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5857.CylindricalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> '_5873.HypoidGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5873.HypoidGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6154.HypoidGearMeshLoadCase') -> '_5873.HypoidGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5873.HypoidGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> '_5878.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5878.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6160.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5878.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5878.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5881.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5881.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6163.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5881.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5881.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5884.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5884.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5884.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5884.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> '_5909.SpiralBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5909.SpiralBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6199.SpiralBevelGearMeshLoadCase') -> '_5909.SpiralBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5909.SpiralBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> '_5918.StraightBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5918.StraightBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6209.StraightBevelGearMeshLoadCase') -> '_5918.StraightBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5918.StraightBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> '_5933.WormGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5933.WormGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6230.WormGearMeshLoadCase') -> '_5933.WormGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5933.WormGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> '_5936.ZerolBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5936.ZerolBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6233.ZerolBevelGearMeshLoadCase') -> '_5936.ZerolBevelGearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5936.ZerolBevelGearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> '_5869.GearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5869.GearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6140.GearMeshLoadCase') -> '_5869.GearMeshDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5869.GearMeshDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> '_5891.PartToPartShearCouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5891.PartToPartShearCouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6176.PartToPartShearCouplingConnectionLoadCase') -> '_5891.PartToPartShearCouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5891.PartToPartShearCouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> '_5834.ClutchConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5834.ClutchConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6087.ClutchConnectionLoadCase') -> '_5834.ClutchConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5834.ClutchConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> '_5839.ConceptCouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5839.ConceptCouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6092.ConceptCouplingConnectionLoadCase') -> '_5839.ConceptCouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5839.ConceptCouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> '_5850.CouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5850.CouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6105.CouplingConnectionLoadCase') -> '_5850.CouplingConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5850.CouplingConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> '_5911.SpringDamperConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5911.SpringDamperConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6201.SpringDamperConnectionLoadCase') -> '_5911.SpringDamperConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5911.SpringDamperConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> '_5926.TorqueConverterConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5926.TorqueConverterConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6219.TorqueConverterConnectionLoadCase') -> '_5926.TorqueConverterConnectionDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5926.TorqueConverterConnectionDynamicAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> '_5815.AbstractAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5815.AbstractAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6066.AbstractAssemblyLoadCase') -> '_5815.AbstractAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5815.AbstractAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> '_5816.AbstractShaftOrHousingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5816.AbstractShaftOrHousingDynamicAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6067.AbstractShaftOrHousingLoadCase') -> '_5816.AbstractShaftOrHousingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5816.AbstractShaftOrHousingDynamicAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> '_5821.BearingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BearingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5821.BearingDynamicAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6074.BearingLoadCase') -> '_5821.BearingDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BearingDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5821.BearingDynamicAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> '_5832.BoltDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BoltDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5832.BoltDynamicAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6086.BoltLoadCase') -> '_5832.BoltDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BoltDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5832.BoltDynamicAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> '_5833.BoltedJointDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5833.BoltedJointDynamicAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6085.BoltedJointLoadCase') -> '_5833.BoltedJointDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5833.BoltedJointDynamicAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2004.Component') -> '_5838.ComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5838.ComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6091.ComponentLoadCase') -> '_5838.ComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5838.ComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2007.Connector') -> '_5849.ConnectorDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5849.ConnectorDynamicAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6104.ConnectorLoadCase') -> '_5849.ConnectorDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5849.ConnectorDynamicAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2008.Datum') -> '_5860.DatumDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.DatumDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5860.DatumDynamicAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6119.DatumLoadCase') -> '_5860.DatumDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.DatumDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5860.DatumDynamicAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> '_5863.ExternalCADModelDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5863.ExternalCADModelDynamicAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6132.ExternalCADModelLoadCase') -> '_5863.ExternalCADModelDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5863.ExternalCADModelDynamicAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> '_5867.FlexiblePinAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FlexiblePinAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5867.FlexiblePinAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6136.FlexiblePinAssemblyLoadCase') -> '_5867.FlexiblePinAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FlexiblePinAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5867.FlexiblePinAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> '_5820.AssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5820.AssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6073.AssemblyLoadCase') -> '_5820.AssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5820.AssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> '_5871.GuideDxfModelDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GuideDxfModelDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5871.GuideDxfModelDynamicAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6144.GuideDxfModelLoadCase') -> '_5871.GuideDxfModelDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GuideDxfModelDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5871.GuideDxfModelDynamicAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> '_5875.ImportedFEComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ImportedFEComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5875.ImportedFEComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6156.ImportedFEComponentLoadCase') -> '_5875.ImportedFEComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ImportedFEComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5875.ImportedFEComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> '_5886.MassDiscDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5886.MassDiscDynamicAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6168.MassDiscLoadCase') -> '_5886.MassDiscDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5886.MassDiscDynamicAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> '_5887.MeasurementComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5887.MeasurementComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6169.MeasurementComponentLoadCase') -> '_5887.MeasurementComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5887.MeasurementComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> '_5888.MountableComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5888.MountableComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6171.MountableComponentLoadCase') -> '_5888.MountableComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5888.MountableComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> '_5889.OilSealDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5889.OilSealDynamicAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6173.OilSealLoadCase') -> '_5889.OilSealDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5889.OilSealDynamicAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2026.Part') -> '_5890.PartDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5890.PartDynamicAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6175.PartLoadCase') -> '_5890.PartDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5890.PartDynamicAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> '_5896.PlanetCarrierDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5896.PlanetCarrierDynamicAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6182.PlanetCarrierLoadCase') -> '_5896.PlanetCarrierDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5896.PlanetCarrierDynamicAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> '_5897.PointLoadDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5897.PointLoadDynamicAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6185.PointLoadLoadCase') -> '_5897.PointLoadDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5897.PointLoadDynamicAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> '_5898.PowerLoadDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5898.PowerLoadDynamicAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6186.PowerLoadLoadCase') -> '_5898.PowerLoadDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5898.PowerLoadDynamicAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> '_5903.RootAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5903.RootAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6192.RootAssemblyLoadCase') -> '_5903.RootAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5903.RootAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> '_5907.SpecialisedAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5907.SpecialisedAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6196.SpecialisedAssemblyLoadCase') -> '_5907.SpecialisedAssemblyDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5907.SpecialisedAssemblyDynamicAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> '_5930.UnbalancedMassDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5930.UnbalancedMassDynamicAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6227.UnbalancedMassLoadCase') -> '_5930.UnbalancedMassDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5930.UnbalancedMassDynamicAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> '_5931.VirtualComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5931.VirtualComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6228.VirtualComponentLoadCase') -> '_5931.VirtualComponentDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5931.VirtualComponentDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> '_5904.ShaftDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5904.ShaftDynamicAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6194.ShaftLoadCase') -> '_5904.ShaftDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5904.ShaftDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> '_5842.ConceptGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5842.ConceptGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6095.ConceptGearLoadCase') -> '_5842.ConceptGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5842.ConceptGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> '_5844.ConceptGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5844.ConceptGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6097.ConceptGearSetLoadCase') -> '_5844.ConceptGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5844.ConceptGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> '_5864.FaceGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5864.FaceGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6133.FaceGearLoadCase') -> '_5864.FaceGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5864.FaceGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> '_5866.FaceGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5866.FaceGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6135.FaceGearSetLoadCase') -> '_5866.FaceGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5866.FaceGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> '_5817.AGMAGleasonConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5817.AGMAGleasonConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6069.AGMAGleasonConicalGearLoadCase') -> '_5817.AGMAGleasonConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5817.AGMAGleasonConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> '_5819.AGMAGleasonConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5819.AGMAGleasonConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6071.AGMAGleasonConicalGearSetLoadCase') -> '_5819.AGMAGleasonConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5819.AGMAGleasonConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> '_5824.BevelDifferentialGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5824.BevelDifferentialGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6077.BevelDifferentialGearLoadCase') -> '_5824.BevelDifferentialGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5824.BevelDifferentialGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> '_5826.BevelDifferentialGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5826.BevelDifferentialGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6079.BevelDifferentialGearSetLoadCase') -> '_5826.BevelDifferentialGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5826.BevelDifferentialGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> '_5827.BevelDifferentialPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5827.BevelDifferentialPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6080.BevelDifferentialPlanetGearLoadCase') -> '_5827.BevelDifferentialPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5827.BevelDifferentialPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> '_5828.BevelDifferentialSunGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5828.BevelDifferentialSunGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6081.BevelDifferentialSunGearLoadCase') -> '_5828.BevelDifferentialSunGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5828.BevelDifferentialSunGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> '_5829.BevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5829.BevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6082.BevelGearLoadCase') -> '_5829.BevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5829.BevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> '_5831.BevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5831.BevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6084.BevelGearSetLoadCase') -> '_5831.BevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5831.BevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> '_5845.ConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5845.ConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6098.ConicalGearLoadCase') -> '_5845.ConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5845.ConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> '_5847.ConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5847.ConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6102.ConicalGearSetLoadCase') -> '_5847.ConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5847.ConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> '_5856.CylindricalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5856.CylindricalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6111.CylindricalGearLoadCase') -> '_5856.CylindricalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5856.CylindricalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> '_5858.CylindricalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5858.CylindricalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6115.CylindricalGearSetLoadCase') -> '_5858.CylindricalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5858.CylindricalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> '_5859.CylindricalPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5859.CylindricalPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6116.CylindricalPlanetGearLoadCase') -> '_5859.CylindricalPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5859.CylindricalPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2086.Gear') -> '_5868.GearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5868.GearDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6138.GearLoadCase') -> '_5868.GearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5868.GearDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> '_5870.GearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5870.GearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6143.GearSetLoadCase') -> '_5870.GearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5870.GearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> '_5872.HypoidGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5872.HypoidGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6153.HypoidGearLoadCase') -> '_5872.HypoidGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5872.HypoidGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> '_5874.HypoidGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5874.HypoidGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6155.HypoidGearSetLoadCase') -> '_5874.HypoidGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5874.HypoidGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> '_5877.KlingelnbergCycloPalloidConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5877.KlingelnbergCycloPalloidConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6159.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5877.KlingelnbergCycloPalloidConicalGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5877.KlingelnbergCycloPalloidConicalGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> '_5879.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5879.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6161.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5879.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5879.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> '_5880.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5880.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6162.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5880.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5880.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> '_5882.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5882.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5882.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5882.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5883.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5883.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5883.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5883.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5885.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5885.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5885.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5885.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> '_5895.PlanetaryGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5895.PlanetaryGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6180.PlanetaryGearSetLoadCase') -> '_5895.PlanetaryGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5895.PlanetaryGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> '_5908.SpiralBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5908.SpiralBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6198.SpiralBevelGearLoadCase') -> '_5908.SpiralBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5908.SpiralBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> '_5910.SpiralBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5910.SpiralBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6200.SpiralBevelGearSetLoadCase') -> '_5910.SpiralBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5910.SpiralBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> '_5914.StraightBevelDiffGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5914.StraightBevelDiffGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6205.StraightBevelDiffGearLoadCase') -> '_5914.StraightBevelDiffGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5914.StraightBevelDiffGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> '_5916.StraightBevelDiffGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5916.StraightBevelDiffGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6207.StraightBevelDiffGearSetLoadCase') -> '_5916.StraightBevelDiffGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5916.StraightBevelDiffGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> '_5917.StraightBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5917.StraightBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6208.StraightBevelGearLoadCase') -> '_5917.StraightBevelGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5917.StraightBevelGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> '_5919.StraightBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5919.StraightBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6210.StraightBevelGearSetLoadCase') -> '_5919.StraightBevelGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5919.StraightBevelGearSetDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> '_5920.StraightBevelPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5920.StraightBevelPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6211.StraightBevelPlanetGearLoadCase') -> '_5920.StraightBevelPlanetGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5920.StraightBevelPlanetGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> '_5921.StraightBevelSunGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelSunGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5921.StraightBevelSunGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelSunGearLoadCase') -> '_5921.StraightBevelSunGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelSunGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5921.StraightBevelSunGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> '_5932.WormGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5932.WormGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6229.WormGearLoadCase') -> '_5932.WormGearDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5932.WormGearDynamicAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> '_5934.WormGearSetDynamicAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearSetDynamicAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5934.WormGearSetDynamicAnalysis)(method_result) if method_result else None
