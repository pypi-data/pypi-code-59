'''_2189.py

SingleMeshWhineAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import (
    _5546, _5550, _5549, _5505,
    _5504, _5436, _5449, _5448,
    _5454, _5453, _5465, _5464,
    _5468, _5467, _5511, _5516,
    _5514, _5512, _5526, _5525,
    _5537, _5535, _5536, _5538,
    _5541, _5540, _5542, _5466,
    _5435, _5450, _5461, _5487,
    _5506, _5513, _5518, _5437,
    _5455, _5475, _5527, _5442,
    _5458, _5430, _5469, _5483,
    _5488, _5491, _5494, _5521,
    _5530, _5545, _5548, _5479,
    _5503, _5447, _5452, _5463,
    _5524, _5539, _5428, _5429,
    _5434, _5446, _5445, _5451,
    _5462, _5473, _5474, _5478,
    _5433, _5482, _5486, _5497,
    _5498, _5500, _5501, _5502,
    _5508, _5509, _5510, _5515,
    _5520, _5543, _5544, _5517,
    _5457, _5456, _5477, _5476,
    _5432, _5431, _5439, _5438,
    _5440, _5441, _5444, _5443,
    _5460, _5459, _5471, _5470,
    _5472, _5481, _5480, _5485,
    _5484, _5490, _5489, _5493,
    _5492, _5496, _5495, _5507,
    _5523, _5522, _5529, _5528,
    _5532, _5531, _5533, _5534,
    _5547
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

_SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SingleMeshWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleMeshWhineAnalysisAnalysis',)


class SingleMeshWhineAnalysisAnalysis(_2170.SingleAnalysis):
    '''SingleMeshWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleMeshWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6231.WormGearSetLoadCase') -> '_5546.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5546.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> '_5550.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5550.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6232.ZerolBevelGearLoadCase') -> '_5550.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5550.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> '_5549.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5549.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6234.ZerolBevelGearSetLoadCase') -> '_5549.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5549.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> '_5505.PartToPartShearCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5505.PartToPartShearCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6178.PartToPartShearCouplingLoadCase') -> '_5505.PartToPartShearCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5505.PartToPartShearCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> '_5504.PartToPartShearCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5504.PartToPartShearCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6177.PartToPartShearCouplingHalfLoadCase') -> '_5504.PartToPartShearCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5504.PartToPartShearCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> '_5436.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5436.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6076.BeltDriveLoadCase') -> '_5436.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5436.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> '_5449.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5449.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6089.ClutchLoadCase') -> '_5449.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5449.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> '_5448.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5448.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6088.ClutchHalfLoadCase') -> '_5448.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5448.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> '_5454.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5454.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6094.ConceptCouplingLoadCase') -> '_5454.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5454.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> '_5453.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5453.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6093.ConceptCouplingHalfLoadCase') -> '_5453.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5453.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> '_5465.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5465.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6107.CouplingLoadCase') -> '_5465.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5465.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> '_5464.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5464.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6106.CouplingHalfLoadCase') -> '_5464.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5464.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2137.CVT') -> '_5468.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5468.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6109.CVTLoadCase') -> '_5468.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5468.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> '_5467.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5467.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6110.CVTPulleyLoadCase') -> '_5467.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5467.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> '_5511.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5511.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6187.PulleyLoadCase') -> '_5511.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5511.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> '_5516.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5516.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6193.ShaftHubConnectionLoadCase') -> '_5516.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5516.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> '_5514.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5514.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6191.RollingRingLoadCase') -> '_5514.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5514.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> '_5512.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5512.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6189.RollingRingAssemblyLoadCase') -> '_5512.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5512.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> '_5526.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5526.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6203.SpringDamperLoadCase') -> '_5526.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5526.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> '_5525.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5525.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6202.SpringDamperHalfLoadCase') -> '_5525.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5525.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> '_5537.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5537.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6214.SynchroniserLoadCase') -> '_5537.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5537.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> '_5535.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5535.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6213.SynchroniserHalfLoadCase') -> '_5535.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5535.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> '_5536.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5536.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6215.SynchroniserPartLoadCase') -> '_5536.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5536.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> '_5538.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5538.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6216.SynchroniserSleeveLoadCase') -> '_5538.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5538.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> '_5541.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5541.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6220.TorqueConverterLoadCase') -> '_5541.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5541.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> '_5540.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5540.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6221.TorqueConverterPumpLoadCase') -> '_5540.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5540.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> '_5542.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5542.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6222.TorqueConverterTurbineLoadCase') -> '_5542.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5542.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> '_5466.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5466.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6108.CVTBeltConnectionLoadCase') -> '_5466.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5466.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> '_5435.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5435.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6075.BeltConnectionLoadCase') -> '_5435.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5435.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> '_5450.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5450.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6090.CoaxialConnectionLoadCase') -> '_5450.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5450.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1851.Connection') -> '_5461.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5461.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6103.ConnectionLoadCase') -> '_5461.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5461.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> '_5487.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5487.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6158.InterMountableComponentConnectionLoadCase') -> '_5487.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5487.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> '_5506.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5506.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6179.PlanetaryConnectionLoadCase') -> '_5506.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5506.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> '_5513.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5513.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6190.RollingRingConnectionLoadCase') -> '_5513.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5513.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> '_5518.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5518.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6195.ShaftToMountableComponentConnectionLoadCase') -> '_5518.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5518.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> '_5437.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5437.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6078.BevelDifferentialGearMeshLoadCase') -> '_5437.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5437.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> '_5455.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5455.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6096.ConceptGearMeshLoadCase') -> '_5455.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5455.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> '_5475.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5475.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6134.FaceGearMeshLoadCase') -> '_5475.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5475.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> '_5527.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5527.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6206.StraightBevelDiffGearMeshLoadCase') -> '_5527.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5527.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> '_5442.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5442.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6083.BevelGearMeshLoadCase') -> '_5442.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5442.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> '_5458.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5458.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6100.ConicalGearMeshLoadCase') -> '_5458.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5458.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> '_5430.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5430.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6070.AGMAGleasonConicalGearMeshLoadCase') -> '_5430.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5430.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> '_5469.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5469.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6113.CylindricalGearMeshLoadCase') -> '_5469.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5469.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> '_5483.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5483.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6154.HypoidGearMeshLoadCase') -> '_5483.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5483.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> '_5488.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5488.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6160.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5488.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5488.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5491.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5491.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6163.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5491.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5491.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5494.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5494.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5494.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5494.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> '_5521.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5521.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6199.SpiralBevelGearMeshLoadCase') -> '_5521.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5521.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> '_5530.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5530.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6209.StraightBevelGearMeshLoadCase') -> '_5530.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5530.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> '_5545.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5545.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6230.WormGearMeshLoadCase') -> '_5545.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5545.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> '_5548.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5548.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6233.ZerolBevelGearMeshLoadCase') -> '_5548.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5548.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> '_5479.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5479.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6140.GearMeshLoadCase') -> '_5479.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5479.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> '_5503.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5503.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6176.PartToPartShearCouplingConnectionLoadCase') -> '_5503.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5503.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> '_5447.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5447.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6087.ClutchConnectionLoadCase') -> '_5447.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5447.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> '_5452.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5452.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6092.ConceptCouplingConnectionLoadCase') -> '_5452.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5452.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> '_5463.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5463.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6105.CouplingConnectionLoadCase') -> '_5463.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5463.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> '_5524.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5524.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6201.SpringDamperConnectionLoadCase') -> '_5524.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5524.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> '_5539.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5539.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6219.TorqueConverterConnectionLoadCase') -> '_5539.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5539.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> '_5428.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5428.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6066.AbstractAssemblyLoadCase') -> '_5428.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5428.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> '_5429.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5429.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6067.AbstractShaftOrHousingLoadCase') -> '_5429.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5429.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> '_5434.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5434.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6074.BearingLoadCase') -> '_5434.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5434.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> '_5446.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5446.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6086.BoltLoadCase') -> '_5446.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5446.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> '_5445.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5445.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6085.BoltedJointLoadCase') -> '_5445.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5445.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2004.Component') -> '_5451.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5451.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6091.ComponentLoadCase') -> '_5451.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5451.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2007.Connector') -> '_5462.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5462.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6104.ConnectorLoadCase') -> '_5462.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5462.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2008.Datum') -> '_5473.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5473.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6119.DatumLoadCase') -> '_5473.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5473.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> '_5474.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5474.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6132.ExternalCADModelLoadCase') -> '_5474.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5474.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> '_5478.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5478.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6136.FlexiblePinAssemblyLoadCase') -> '_5478.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5478.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> '_5433.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5433.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6073.AssemblyLoadCase') -> '_5433.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5433.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> '_5482.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5482.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6144.GuideDxfModelLoadCase') -> '_5482.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5482.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> '_5486.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5486.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6156.ImportedFEComponentLoadCase') -> '_5486.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5486.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> '_5497.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5497.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6168.MassDiscLoadCase') -> '_5497.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5497.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> '_5498.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5498.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6169.MeasurementComponentLoadCase') -> '_5498.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5498.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> '_5500.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5500.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6171.MountableComponentLoadCase') -> '_5500.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5500.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> '_5501.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5501.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6173.OilSealLoadCase') -> '_5501.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5501.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2026.Part') -> '_5502.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5502.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6175.PartLoadCase') -> '_5502.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5502.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> '_5508.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5508.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6182.PlanetCarrierLoadCase') -> '_5508.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5508.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> '_5509.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5509.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6185.PointLoadLoadCase') -> '_5509.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5509.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> '_5510.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5510.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6186.PowerLoadLoadCase') -> '_5510.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5510.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> '_5515.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5515.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6192.RootAssemblyLoadCase') -> '_5515.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5515.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> '_5520.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5520.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6196.SpecialisedAssemblyLoadCase') -> '_5520.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5520.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> '_5543.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5543.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6227.UnbalancedMassLoadCase') -> '_5543.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5543.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> '_5544.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5544.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6228.VirtualComponentLoadCase') -> '_5544.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5544.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> '_5517.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5517.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6194.ShaftLoadCase') -> '_5517.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5517.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> '_5457.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5457.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6095.ConceptGearLoadCase') -> '_5457.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5457.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> '_5456.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5456.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6097.ConceptGearSetLoadCase') -> '_5456.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5456.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> '_5477.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5477.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6133.FaceGearLoadCase') -> '_5477.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5477.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> '_5476.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5476.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6135.FaceGearSetLoadCase') -> '_5476.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5476.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> '_5432.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5432.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6069.AGMAGleasonConicalGearLoadCase') -> '_5432.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5432.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> '_5431.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5431.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6071.AGMAGleasonConicalGearSetLoadCase') -> '_5431.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5431.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> '_5439.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5439.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6077.BevelDifferentialGearLoadCase') -> '_5439.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5439.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> '_5438.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5438.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6079.BevelDifferentialGearSetLoadCase') -> '_5438.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5438.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> '_5440.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5440.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6080.BevelDifferentialPlanetGearLoadCase') -> '_5440.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5440.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> '_5441.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5441.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6081.BevelDifferentialSunGearLoadCase') -> '_5441.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5441.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> '_5444.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5444.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6082.BevelGearLoadCase') -> '_5444.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5444.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> '_5443.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5443.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6084.BevelGearSetLoadCase') -> '_5443.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5443.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> '_5460.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5460.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6098.ConicalGearLoadCase') -> '_5460.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5460.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> '_5459.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5459.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6102.ConicalGearSetLoadCase') -> '_5459.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5459.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> '_5471.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5471.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6111.CylindricalGearLoadCase') -> '_5471.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5471.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> '_5470.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5470.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6115.CylindricalGearSetLoadCase') -> '_5470.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5470.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> '_5472.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5472.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6116.CylindricalPlanetGearLoadCase') -> '_5472.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5472.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2086.Gear') -> '_5481.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5481.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6138.GearLoadCase') -> '_5481.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5481.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> '_5480.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5480.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6143.GearSetLoadCase') -> '_5480.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5480.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> '_5485.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5485.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6153.HypoidGearLoadCase') -> '_5485.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5485.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> '_5484.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5484.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6155.HypoidGearSetLoadCase') -> '_5484.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5484.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> '_5490.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5490.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6159.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5490.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5490.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> '_5489.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5489.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6161.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5489.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5489.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> '_5493.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5493.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6162.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5493.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5493.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> '_5492.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5492.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5492.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5492.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5496.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5496.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5496.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5496.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5495.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5495.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5495.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5495.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> '_5507.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5507.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6180.PlanetaryGearSetLoadCase') -> '_5507.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5507.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> '_5523.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5523.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6198.SpiralBevelGearLoadCase') -> '_5523.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5523.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> '_5522.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5522.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6200.SpiralBevelGearSetLoadCase') -> '_5522.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5522.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> '_5529.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5529.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6205.StraightBevelDiffGearLoadCase') -> '_5529.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5529.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> '_5528.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5528.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6207.StraightBevelDiffGearSetLoadCase') -> '_5528.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5528.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> '_5532.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5532.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6208.StraightBevelGearLoadCase') -> '_5532.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5532.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> '_5531.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5531.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6210.StraightBevelGearSetLoadCase') -> '_5531.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5531.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> '_5533.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5533.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6211.StraightBevelPlanetGearLoadCase') -> '_5533.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5533.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> '_5534.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5534.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelSunGearLoadCase') -> '_5534.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5534.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> '_5547.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5547.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6229.WormGearLoadCase') -> '_5547.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5547.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> '_5546.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5546.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None
