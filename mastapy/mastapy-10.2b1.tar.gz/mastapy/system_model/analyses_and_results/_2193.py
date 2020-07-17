'''_2193.py

SystemDeflectionAnalysis
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
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2359, _2363, _2362, _2313,
    _2312, _2233, _2246, _2245,
    _2252, _2251, _2264, _2263,
    _2267, _2266, _2318, _2323,
    _2321, _2319, _2334, _2333,
    _2346, _2343, _2344, _2345,
    _2352, _2351, _2353, _2265,
    _2232, _2247, _2260, _2293,
    _2314, _2320, _2327, _2234,
    _2253, _2281, _2335, _2239,
    _2257, _2227, _2270, _2289,
    _2294, _2297, _2300, _2329,
    _2338, _2358, _2361, _2285,
    _2311, _2244, _2250, _2262,
    _2332, _2350, _2225, _2226,
    _2231, _2243, _2242, _2248,
    _2261, _2278, _2279, _2284,
    _2230, _2288, _2292, _2304,
    _2305, _2307, _2309, _2310,
    _2315, _2316, _2317, _2322,
    _2328, _2356, _2357, _2326,
    _2255, _2254, _2283, _2282,
    _2229, _2228, _2236, _2235,
    _2237, _2238, _2241, _2240,
    _2259, _2258, _2276, _2273,
    _2277, _2287, _2286, _2291,
    _2290, _2296, _2295, _2299,
    _2298, _2302, _2301, _2331,
    _2330, _2337, _2336, _2340,
    _2339, _2341, _2342, _2360
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

_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionAnalysis',)


class SystemDeflectionAnalysis(_2170.SingleAnalysis):
    '''SystemDeflectionAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYSTEM_DEFLECTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6231.WormGearSetLoadCase') -> '_2359.WormGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2359.WormGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> '_2363.ZerolBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2363.ZerolBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6232.ZerolBevelGearLoadCase') -> '_2363.ZerolBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2363.ZerolBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> '_2362.ZerolBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2362.ZerolBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6234.ZerolBevelGearSetLoadCase') -> '_2362.ZerolBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2362.ZerolBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> '_2313.PartToPartShearCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2313.PartToPartShearCouplingSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6178.PartToPartShearCouplingLoadCase') -> '_2313.PartToPartShearCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2313.PartToPartShearCouplingSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> '_2312.PartToPartShearCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2312.PartToPartShearCouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6177.PartToPartShearCouplingHalfLoadCase') -> '_2312.PartToPartShearCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2312.PartToPartShearCouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> '_2233.BeltDriveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2233.BeltDriveSystemDeflection)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6076.BeltDriveLoadCase') -> '_2233.BeltDriveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2233.BeltDriveSystemDeflection)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> '_2246.ClutchSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2246.ClutchSystemDeflection)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6089.ClutchLoadCase') -> '_2246.ClutchSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2246.ClutchSystemDeflection)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> '_2245.ClutchHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2245.ClutchHalfSystemDeflection)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6088.ClutchHalfLoadCase') -> '_2245.ClutchHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2245.ClutchHalfSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> '_2252.ConceptCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2252.ConceptCouplingSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6094.ConceptCouplingLoadCase') -> '_2252.ConceptCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2252.ConceptCouplingSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> '_2251.ConceptCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2251.ConceptCouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6093.ConceptCouplingHalfLoadCase') -> '_2251.ConceptCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2251.ConceptCouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> '_2264.CouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2264.CouplingSystemDeflection)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6107.CouplingLoadCase') -> '_2264.CouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2264.CouplingSystemDeflection)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> '_2263.CouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2263.CouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6106.CouplingHalfLoadCase') -> '_2263.CouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2263.CouplingHalfSystemDeflection)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2137.CVT') -> '_2267.CVTSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2267.CVTSystemDeflection)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6109.CVTLoadCase') -> '_2267.CVTSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2267.CVTSystemDeflection)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> '_2266.CVTPulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2266.CVTPulleySystemDeflection)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6110.CVTPulleyLoadCase') -> '_2266.CVTPulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2266.CVTPulleySystemDeflection)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> '_2318.PulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2318.PulleySystemDeflection)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6187.PulleyLoadCase') -> '_2318.PulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2318.PulleySystemDeflection)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> '_2323.ShaftHubConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2323.ShaftHubConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6193.ShaftHubConnectionLoadCase') -> '_2323.ShaftHubConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2323.ShaftHubConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> '_2321.RollingRingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2321.RollingRingSystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6191.RollingRingLoadCase') -> '_2321.RollingRingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2321.RollingRingSystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> '_2319.RollingRingAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2319.RollingRingAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6189.RollingRingAssemblyLoadCase') -> '_2319.RollingRingAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2319.RollingRingAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> '_2334.SpringDamperSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2334.SpringDamperSystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6203.SpringDamperLoadCase') -> '_2334.SpringDamperSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2334.SpringDamperSystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> '_2333.SpringDamperHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2333.SpringDamperHalfSystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6202.SpringDamperHalfLoadCase') -> '_2333.SpringDamperHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2333.SpringDamperHalfSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> '_2346.SynchroniserSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2346.SynchroniserSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6214.SynchroniserLoadCase') -> '_2346.SynchroniserSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2346.SynchroniserSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> '_2343.SynchroniserHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2343.SynchroniserHalfSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6213.SynchroniserHalfLoadCase') -> '_2343.SynchroniserHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2343.SynchroniserHalfSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> '_2344.SynchroniserPartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2344.SynchroniserPartSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6215.SynchroniserPartLoadCase') -> '_2344.SynchroniserPartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2344.SynchroniserPartSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> '_2345.SynchroniserSleeveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2345.SynchroniserSleeveSystemDeflection)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6216.SynchroniserSleeveLoadCase') -> '_2345.SynchroniserSleeveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2345.SynchroniserSleeveSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> '_2352.TorqueConverterSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2352.TorqueConverterSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6220.TorqueConverterLoadCase') -> '_2352.TorqueConverterSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2352.TorqueConverterSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> '_2351.TorqueConverterPumpSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2351.TorqueConverterPumpSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6221.TorqueConverterPumpLoadCase') -> '_2351.TorqueConverterPumpSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2351.TorqueConverterPumpSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> '_2353.TorqueConverterTurbineSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2353.TorqueConverterTurbineSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6222.TorqueConverterTurbineLoadCase') -> '_2353.TorqueConverterTurbineSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2353.TorqueConverterTurbineSystemDeflection)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> '_2265.CVTBeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2265.CVTBeltConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6108.CVTBeltConnectionLoadCase') -> '_2265.CVTBeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2265.CVTBeltConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> '_2232.BeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2232.BeltConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6075.BeltConnectionLoadCase') -> '_2232.BeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2232.BeltConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> '_2247.CoaxialConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2247.CoaxialConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6090.CoaxialConnectionLoadCase') -> '_2247.CoaxialConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2247.CoaxialConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1851.Connection') -> '_2260.ConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2260.ConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6103.ConnectionLoadCase') -> '_2260.ConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2260.ConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> '_2293.InterMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2293.InterMountableComponentConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6158.InterMountableComponentConnectionLoadCase') -> '_2293.InterMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2293.InterMountableComponentConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> '_2314.PlanetaryConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2314.PlanetaryConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6179.PlanetaryConnectionLoadCase') -> '_2314.PlanetaryConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2314.PlanetaryConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> '_2320.RollingRingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2320.RollingRingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6190.RollingRingConnectionLoadCase') -> '_2320.RollingRingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2320.RollingRingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> '_2327.ShaftToMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2327.ShaftToMountableComponentConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6195.ShaftToMountableComponentConnectionLoadCase') -> '_2327.ShaftToMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2327.ShaftToMountableComponentConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> '_2234.BevelDifferentialGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2234.BevelDifferentialGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6078.BevelDifferentialGearMeshLoadCase') -> '_2234.BevelDifferentialGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2234.BevelDifferentialGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> '_2253.ConceptGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2253.ConceptGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6096.ConceptGearMeshLoadCase') -> '_2253.ConceptGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2253.ConceptGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> '_2281.FaceGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2281.FaceGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6134.FaceGearMeshLoadCase') -> '_2281.FaceGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2281.FaceGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> '_2335.StraightBevelDiffGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2335.StraightBevelDiffGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6206.StraightBevelDiffGearMeshLoadCase') -> '_2335.StraightBevelDiffGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2335.StraightBevelDiffGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> '_2239.BevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2239.BevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6083.BevelGearMeshLoadCase') -> '_2239.BevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2239.BevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> '_2257.ConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2257.ConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6100.ConicalGearMeshLoadCase') -> '_2257.ConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2257.ConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> '_2227.AGMAGleasonConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2227.AGMAGleasonConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6070.AGMAGleasonConicalGearMeshLoadCase') -> '_2227.AGMAGleasonConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2227.AGMAGleasonConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> '_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6113.CylindricalGearMeshLoadCase') -> '_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2270.CylindricalGearMeshSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> '_2289.HypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2289.HypoidGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6154.HypoidGearMeshLoadCase') -> '_2289.HypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2289.HypoidGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> '_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6160.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2294.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> '_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6163.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2297.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2300.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> '_2329.SpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2329.SpiralBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6199.SpiralBevelGearMeshLoadCase') -> '_2329.SpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2329.SpiralBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> '_2338.StraightBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2338.StraightBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6209.StraightBevelGearMeshLoadCase') -> '_2338.StraightBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2338.StraightBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> '_2358.WormGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2358.WormGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6230.WormGearMeshLoadCase') -> '_2358.WormGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2358.WormGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> '_2361.ZerolBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2361.ZerolBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6233.ZerolBevelGearMeshLoadCase') -> '_2361.ZerolBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2361.ZerolBevelGearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> '_2285.GearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2285.GearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6140.GearMeshLoadCase') -> '_2285.GearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2285.GearMeshSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> '_2311.PartToPartShearCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2311.PartToPartShearCouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6176.PartToPartShearCouplingConnectionLoadCase') -> '_2311.PartToPartShearCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2311.PartToPartShearCouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> '_2244.ClutchConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2244.ClutchConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6087.ClutchConnectionLoadCase') -> '_2244.ClutchConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2244.ClutchConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> '_2250.ConceptCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2250.ConceptCouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6092.ConceptCouplingConnectionLoadCase') -> '_2250.ConceptCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2250.ConceptCouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> '_2262.CouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2262.CouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6105.CouplingConnectionLoadCase') -> '_2262.CouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2262.CouplingConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> '_2332.SpringDamperConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2332.SpringDamperConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6201.SpringDamperConnectionLoadCase') -> '_2332.SpringDamperConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2332.SpringDamperConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> '_2350.TorqueConverterConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2350.TorqueConverterConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6219.TorqueConverterConnectionLoadCase') -> '_2350.TorqueConverterConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2350.TorqueConverterConnectionSystemDeflection)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> '_2225.AbstractAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2225.AbstractAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6066.AbstractAssemblyLoadCase') -> '_2225.AbstractAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2225.AbstractAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> '_2226.AbstractShaftOrHousingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2226.AbstractShaftOrHousingSystemDeflection)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6067.AbstractShaftOrHousingLoadCase') -> '_2226.AbstractShaftOrHousingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2226.AbstractShaftOrHousingSystemDeflection)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> '_2231.BearingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2231.BearingSystemDeflection)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6074.BearingLoadCase') -> '_2231.BearingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2231.BearingSystemDeflection)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> '_2243.BoltSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2243.BoltSystemDeflection)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6086.BoltLoadCase') -> '_2243.BoltSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2243.BoltSystemDeflection)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> '_2242.BoltedJointSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2242.BoltedJointSystemDeflection)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6085.BoltedJointLoadCase') -> '_2242.BoltedJointSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2242.BoltedJointSystemDeflection)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2004.Component') -> '_2248.ComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2248.ComponentSystemDeflection)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6091.ComponentLoadCase') -> '_2248.ComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2248.ComponentSystemDeflection)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2007.Connector') -> '_2261.ConnectorSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2261.ConnectorSystemDeflection)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6104.ConnectorLoadCase') -> '_2261.ConnectorSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2261.ConnectorSystemDeflection)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2008.Datum') -> '_2278.DatumSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2278.DatumSystemDeflection)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6119.DatumLoadCase') -> '_2278.DatumSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2278.DatumSystemDeflection)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> '_2279.ExternalCADModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2279.ExternalCADModelSystemDeflection)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6132.ExternalCADModelLoadCase') -> '_2279.ExternalCADModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2279.ExternalCADModelSystemDeflection)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> '_2284.FlexiblePinAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2284.FlexiblePinAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6136.FlexiblePinAssemblyLoadCase') -> '_2284.FlexiblePinAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2284.FlexiblePinAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> '_2230.AssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2230.AssemblySystemDeflection)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6073.AssemblyLoadCase') -> '_2230.AssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2230.AssemblySystemDeflection)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> '_2288.GuideDxfModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2288.GuideDxfModelSystemDeflection)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6144.GuideDxfModelLoadCase') -> '_2288.GuideDxfModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2288.GuideDxfModelSystemDeflection)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> '_2292.ImportedFEComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ImportedFEComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2292.ImportedFEComponentSystemDeflection)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6156.ImportedFEComponentLoadCase') -> '_2292.ImportedFEComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ImportedFEComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2292.ImportedFEComponentSystemDeflection)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> '_2304.MassDiscSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2304.MassDiscSystemDeflection)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6168.MassDiscLoadCase') -> '_2304.MassDiscSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2304.MassDiscSystemDeflection)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> '_2305.MeasurementComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2305.MeasurementComponentSystemDeflection)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6169.MeasurementComponentLoadCase') -> '_2305.MeasurementComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2305.MeasurementComponentSystemDeflection)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> '_2307.MountableComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2307.MountableComponentSystemDeflection)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6171.MountableComponentLoadCase') -> '_2307.MountableComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2307.MountableComponentSystemDeflection)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> '_2309.OilSealSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2309.OilSealSystemDeflection)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6173.OilSealLoadCase') -> '_2309.OilSealSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2309.OilSealSystemDeflection)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2026.Part') -> '_2310.PartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2310.PartSystemDeflection)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6175.PartLoadCase') -> '_2310.PartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2310.PartSystemDeflection)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> '_2315.PlanetCarrierSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2315.PlanetCarrierSystemDeflection)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6182.PlanetCarrierLoadCase') -> '_2315.PlanetCarrierSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2315.PlanetCarrierSystemDeflection)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> '_2316.PointLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2316.PointLoadSystemDeflection)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6185.PointLoadLoadCase') -> '_2316.PointLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2316.PointLoadSystemDeflection)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> '_2317.PowerLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2317.PowerLoadSystemDeflection)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6186.PowerLoadLoadCase') -> '_2317.PowerLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2317.PowerLoadSystemDeflection)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> '_2322.RootAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2322.RootAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6192.RootAssemblyLoadCase') -> '_2322.RootAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2322.RootAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> '_2328.SpecialisedAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2328.SpecialisedAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6196.SpecialisedAssemblyLoadCase') -> '_2328.SpecialisedAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2328.SpecialisedAssemblySystemDeflection)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> '_2356.UnbalancedMassSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2356.UnbalancedMassSystemDeflection)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6227.UnbalancedMassLoadCase') -> '_2356.UnbalancedMassSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2356.UnbalancedMassSystemDeflection)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> '_2357.VirtualComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2357.VirtualComponentSystemDeflection)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6228.VirtualComponentLoadCase') -> '_2357.VirtualComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2357.VirtualComponentSystemDeflection)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> '_2326.ShaftSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2326.ShaftSystemDeflection)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6194.ShaftLoadCase') -> '_2326.ShaftSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2326.ShaftSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> '_2255.ConceptGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2255.ConceptGearSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6095.ConceptGearLoadCase') -> '_2255.ConceptGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2255.ConceptGearSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> '_2254.ConceptGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2254.ConceptGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6097.ConceptGearSetLoadCase') -> '_2254.ConceptGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2254.ConceptGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> '_2283.FaceGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2283.FaceGearSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6133.FaceGearLoadCase') -> '_2283.FaceGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2283.FaceGearSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> '_2282.FaceGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2282.FaceGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6135.FaceGearSetLoadCase') -> '_2282.FaceGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2282.FaceGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> '_2229.AGMAGleasonConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2229.AGMAGleasonConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6069.AGMAGleasonConicalGearLoadCase') -> '_2229.AGMAGleasonConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2229.AGMAGleasonConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> '_2228.AGMAGleasonConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2228.AGMAGleasonConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6071.AGMAGleasonConicalGearSetLoadCase') -> '_2228.AGMAGleasonConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2228.AGMAGleasonConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> '_2236.BevelDifferentialGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2236.BevelDifferentialGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6077.BevelDifferentialGearLoadCase') -> '_2236.BevelDifferentialGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2236.BevelDifferentialGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> '_2235.BevelDifferentialGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2235.BevelDifferentialGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6079.BevelDifferentialGearSetLoadCase') -> '_2235.BevelDifferentialGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2235.BevelDifferentialGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> '_2237.BevelDifferentialPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2237.BevelDifferentialPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6080.BevelDifferentialPlanetGearLoadCase') -> '_2237.BevelDifferentialPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2237.BevelDifferentialPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> '_2238.BevelDifferentialSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2238.BevelDifferentialSunGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6081.BevelDifferentialSunGearLoadCase') -> '_2238.BevelDifferentialSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2238.BevelDifferentialSunGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> '_2241.BevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2241.BevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6082.BevelGearLoadCase') -> '_2241.BevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2241.BevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> '_2240.BevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2240.BevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6084.BevelGearSetLoadCase') -> '_2240.BevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2240.BevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> '_2259.ConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2259.ConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6098.ConicalGearLoadCase') -> '_2259.ConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2259.ConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> '_2258.ConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2258.ConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6102.ConicalGearSetLoadCase') -> '_2258.ConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2258.ConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> '_2276.CylindricalGearSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2276.CylindricalGearSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6111.CylindricalGearLoadCase') -> '_2276.CylindricalGearSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2276.CylindricalGearSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> '_2273.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2273.CylindricalGearSetSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6115.CylindricalGearSetLoadCase') -> '_2273.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2273.CylindricalGearSetSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> '_2277.CylindricalPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2277.CylindricalPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6116.CylindricalPlanetGearLoadCase') -> '_2277.CylindricalPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2277.CylindricalPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2086.Gear') -> '_2287.GearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2287.GearSystemDeflection)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6138.GearLoadCase') -> '_2287.GearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2287.GearSystemDeflection)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> '_2286.GearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2286.GearSetSystemDeflection)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6143.GearSetLoadCase') -> '_2286.GearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2286.GearSetSystemDeflection)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> '_2291.HypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2291.HypoidGearSystemDeflection)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6153.HypoidGearLoadCase') -> '_2291.HypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2291.HypoidGearSystemDeflection)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> '_2290.HypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2290.HypoidGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6155.HypoidGearSetLoadCase') -> '_2290.HypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2290.HypoidGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> '_2296.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2296.KlingelnbergCycloPalloidConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6159.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_2296.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2296.KlingelnbergCycloPalloidConicalGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> '_2295.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2295.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6161.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_2295.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2295.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> '_2299.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2299.KlingelnbergCycloPalloidHypoidGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6162.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_2299.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2299.KlingelnbergCycloPalloidHypoidGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> '_2298.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2298.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_2298.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2298.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> '_2302.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2302.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_2302.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2302.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_2301.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2301.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_2301.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2301.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> '_2273.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2273.CylindricalGearSetSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6180.PlanetaryGearSetLoadCase') -> '_2273.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2273.CylindricalGearSetSystemDeflectionWithLTCAResults)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> '_2331.SpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2331.SpiralBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6198.SpiralBevelGearLoadCase') -> '_2331.SpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2331.SpiralBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> '_2330.SpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2330.SpiralBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6200.SpiralBevelGearSetLoadCase') -> '_2330.SpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2330.SpiralBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> '_2337.StraightBevelDiffGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2337.StraightBevelDiffGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6205.StraightBevelDiffGearLoadCase') -> '_2337.StraightBevelDiffGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2337.StraightBevelDiffGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> '_2336.StraightBevelDiffGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2336.StraightBevelDiffGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6207.StraightBevelDiffGearSetLoadCase') -> '_2336.StraightBevelDiffGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2336.StraightBevelDiffGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> '_2340.StraightBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2340.StraightBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6208.StraightBevelGearLoadCase') -> '_2340.StraightBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2340.StraightBevelGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> '_2339.StraightBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2339.StraightBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6210.StraightBevelGearSetLoadCase') -> '_2339.StraightBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2339.StraightBevelGearSetSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> '_2341.StraightBevelPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2341.StraightBevelPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6211.StraightBevelPlanetGearLoadCase') -> '_2341.StraightBevelPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2341.StraightBevelPlanetGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> '_2342.StraightBevelSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2342.StraightBevelSunGearSystemDeflection)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelSunGearLoadCase') -> '_2342.StraightBevelSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2342.StraightBevelSunGearSystemDeflection)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> '_2360.WormGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2360.WormGearSystemDeflection)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6229.WormGearLoadCase') -> '_2360.WormGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2360.WormGearSystemDeflection)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> '_2359.WormGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_2359.WormGearSetSystemDeflection)(method_result) if method_result else None
