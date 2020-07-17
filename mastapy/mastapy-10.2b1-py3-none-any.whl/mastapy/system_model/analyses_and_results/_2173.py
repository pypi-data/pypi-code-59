'''_2173.py

CompoundParametricStudyToolAnalysis
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
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _3734, _3735, _3737, _3691,
    _3693, _3625, _3636, _3638,
    _3641, _3643, _3652, _3654,
    _3656, _3657, _3699, _3705,
    _3701, _3700, _3711, _3713,
    _3722, _3723, _3724, _3725,
    _3726, _3728, _3729, _3655,
    _3624, _3639, _3650, _3676,
    _3694, _3702, _3706, _3627,
    _3645, _3665, _3715, _3632,
    _3648, _3620, _3659, _3673,
    _3678, _3681, _3684, _3709,
    _3718, _3733, _3736, _3669,
    _3692, _3637, _3642, _3653,
    _3712, _3727, _3617, _3618,
    _3623, _3634, _3635, _3640,
    _3651, _3662, _3663, _3667,
    _3622, _3671, _3675, _3686,
    _3687, _3688, _3689, _3690,
    _3696, _3697, _3698, _3703,
    _3707, _3730, _3731, _3704,
    _3644, _3646, _3664, _3666,
    _3619, _3621, _3626, _3628,
    _3629, _3630, _3631, _3633,
    _3647, _3649, _3658, _3660,
    _3661, _3668, _3670, _3672,
    _3674, _3677, _3679, _3680,
    _3682, _3683, _3685, _3695,
    _3708, _3710, _3714, _3716,
    _3717, _3719, _3720, _3721,
    _3732
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

_COMPOUND_PARAMETRIC_STUDY_TOOL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundParametricStudyToolAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundParametricStudyToolAnalysis',)


class CompoundParametricStudyToolAnalysis(_2170.SingleAnalysis):
    '''CompoundParametricStudyToolAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_PARAMETRIC_STUDY_TOOL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundParametricStudyToolAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6231.WormGearSetLoadCase') -> '_3734.WormGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3734.WormGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2109.ZerolBevelGear') -> '_3735.ZerolBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3735.ZerolBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6232.ZerolBevelGearLoadCase') -> '_3735.ZerolBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3735.ZerolBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2110.ZerolBevelGearSet') -> '_3737.ZerolBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3737.ZerolBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6234.ZerolBevelGearSetLoadCase') -> '_3737.ZerolBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3737.ZerolBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2139.PartToPartShearCoupling') -> '_3691.PartToPartShearCouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3691.PartToPartShearCouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6178.PartToPartShearCouplingLoadCase') -> '_3691.PartToPartShearCouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3691.PartToPartShearCouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2140.PartToPartShearCouplingHalf') -> '_3693.PartToPartShearCouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3693.PartToPartShearCouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6177.PartToPartShearCouplingHalfLoadCase') -> '_3693.PartToPartShearCouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3693.PartToPartShearCouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2128.BeltDrive') -> '_3625.BeltDriveCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BeltDriveCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3625.BeltDriveCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6076.BeltDriveLoadCase') -> '_3625.BeltDriveCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BeltDriveCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3625.BeltDriveCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2130.Clutch') -> '_3636.ClutchCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3636.ClutchCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6089.ClutchLoadCase') -> '_3636.ClutchCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3636.ClutchCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2131.ClutchHalf') -> '_3638.ClutchHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3638.ClutchHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6088.ClutchHalfLoadCase') -> '_3638.ClutchHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3638.ClutchHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2133.ConceptCoupling') -> '_3641.ConceptCouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3641.ConceptCouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6094.ConceptCouplingLoadCase') -> '_3641.ConceptCouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3641.ConceptCouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2134.ConceptCouplingHalf') -> '_3643.ConceptCouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3643.ConceptCouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6093.ConceptCouplingHalfLoadCase') -> '_3643.ConceptCouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3643.ConceptCouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2135.Coupling') -> '_3652.CouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3652.CouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6107.CouplingLoadCase') -> '_3652.CouplingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3652.CouplingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2136.CouplingHalf') -> '_3654.CouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3654.CouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6106.CouplingHalfLoadCase') -> '_3654.CouplingHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3654.CouplingHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2137.CVT') -> '_3656.CVTCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3656.CVTCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6109.CVTLoadCase') -> '_3656.CVTCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3656.CVTCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2138.CVTPulley') -> '_3657.CVTPulleyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTPulleyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3657.CVTPulleyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6110.CVTPulleyLoadCase') -> '_3657.CVTPulleyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTPulleyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3657.CVTPulleyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2141.Pulley') -> '_3699.PulleyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PulleyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3699.PulleyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6187.PulleyLoadCase') -> '_3699.PulleyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PulleyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3699.PulleyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2149.ShaftHubConnection') -> '_3705.ShaftHubConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftHubConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3705.ShaftHubConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6193.ShaftHubConnectionLoadCase') -> '_3705.ShaftHubConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftHubConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3705.ShaftHubConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2147.RollingRing') -> '_3701.RollingRingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3701.RollingRingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6191.RollingRingLoadCase') -> '_3701.RollingRingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3701.RollingRingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2148.RollingRingAssembly') -> '_3700.RollingRingAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3700.RollingRingAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6189.RollingRingAssemblyLoadCase') -> '_3700.RollingRingAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3700.RollingRingAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2150.SpringDamper') -> '_3711.SpringDamperCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3711.SpringDamperCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6203.SpringDamperLoadCase') -> '_3711.SpringDamperCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3711.SpringDamperCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2151.SpringDamperHalf') -> '_3713.SpringDamperHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3713.SpringDamperHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6202.SpringDamperHalfLoadCase') -> '_3713.SpringDamperHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3713.SpringDamperHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2152.Synchroniser') -> '_3722.SynchroniserCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3722.SynchroniserCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6214.SynchroniserLoadCase') -> '_3722.SynchroniserCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3722.SynchroniserCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2154.SynchroniserHalf') -> '_3723.SynchroniserHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3723.SynchroniserHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6213.SynchroniserHalfLoadCase') -> '_3723.SynchroniserHalfCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserHalfCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3723.SynchroniserHalfCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2155.SynchroniserPart') -> '_3724.SynchroniserPartCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserPartCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3724.SynchroniserPartCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6215.SynchroniserPartLoadCase') -> '_3724.SynchroniserPartCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserPartCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3724.SynchroniserPartCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2156.SynchroniserSleeve') -> '_3725.SynchroniserSleeveCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserSleeveCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3725.SynchroniserSleeveCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6216.SynchroniserSleeveLoadCase') -> '_3725.SynchroniserSleeveCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SynchroniserSleeveCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3725.SynchroniserSleeveCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2157.TorqueConverter') -> '_3726.TorqueConverterCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3726.TorqueConverterCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6220.TorqueConverterLoadCase') -> '_3726.TorqueConverterCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3726.TorqueConverterCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2158.TorqueConverterPump') -> '_3728.TorqueConverterPumpCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterPumpCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3728.TorqueConverterPumpCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6221.TorqueConverterPumpLoadCase') -> '_3728.TorqueConverterPumpCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterPumpCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3728.TorqueConverterPumpCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2160.TorqueConverterTurbine') -> '_3729.TorqueConverterTurbineCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterTurbineCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3729.TorqueConverterTurbineCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6222.TorqueConverterTurbineLoadCase') -> '_3729.TorqueConverterTurbineCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterTurbineCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3729.TorqueConverterTurbineCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1852.CVTBeltConnection') -> '_3655.CVTBeltConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTBeltConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3655.CVTBeltConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6108.CVTBeltConnectionLoadCase') -> '_3655.CVTBeltConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CVTBeltConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3655.CVTBeltConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1847.BeltConnection') -> '_3624.BeltConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BeltConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3624.BeltConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6075.BeltConnectionLoadCase') -> '_3624.BeltConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BeltConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3624.BeltConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1848.CoaxialConnection') -> '_3639.CoaxialConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CoaxialConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3639.CoaxialConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6090.CoaxialConnectionLoadCase') -> '_3639.CoaxialConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CoaxialConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3639.CoaxialConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1851.Connection') -> '_3650.ConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3650.ConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6103.ConnectionLoadCase') -> '_3650.ConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3650.ConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1860.InterMountableComponentConnection') -> '_3676.InterMountableComponentConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.InterMountableComponentConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3676.InterMountableComponentConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6158.InterMountableComponentConnectionLoadCase') -> '_3676.InterMountableComponentConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.InterMountableComponentConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3676.InterMountableComponentConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1863.PlanetaryConnection') -> '_3694.PlanetaryConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetaryConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3694.PlanetaryConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6179.PlanetaryConnectionLoadCase') -> '_3694.PlanetaryConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetaryConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3694.PlanetaryConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1867.RollingRingConnection') -> '_3702.RollingRingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3702.RollingRingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6190.RollingRingConnectionLoadCase') -> '_3702.RollingRingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3702.RollingRingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1871.ShaftToMountableComponentConnection') -> '_3706.ShaftToMountableComponentConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftToMountableComponentConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3706.ShaftToMountableComponentConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6195.ShaftToMountableComponentConnectionLoadCase') -> '_3706.ShaftToMountableComponentConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftToMountableComponentConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3706.ShaftToMountableComponentConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1877.BevelDifferentialGearMesh') -> '_3627.BevelDifferentialGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3627.BevelDifferentialGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6078.BevelDifferentialGearMeshLoadCase') -> '_3627.BevelDifferentialGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3627.BevelDifferentialGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1881.ConceptGearMesh') -> '_3645.ConceptGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3645.ConceptGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6096.ConceptGearMeshLoadCase') -> '_3645.ConceptGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3645.ConceptGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1887.FaceGearMesh') -> '_3665.FaceGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3665.FaceGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6134.FaceGearMeshLoadCase') -> '_3665.FaceGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3665.FaceGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1901.StraightBevelDiffGearMesh') -> '_3715.StraightBevelDiffGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3715.StraightBevelDiffGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6206.StraightBevelDiffGearMeshLoadCase') -> '_3715.StraightBevelDiffGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3715.StraightBevelDiffGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1879.BevelGearMesh') -> '_3632.BevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3632.BevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6083.BevelGearMeshLoadCase') -> '_3632.BevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3632.BevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1883.ConicalGearMesh') -> '_3648.ConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3648.ConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6100.ConicalGearMeshLoadCase') -> '_3648.ConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3648.ConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1875.AGMAGleasonConicalGearMesh') -> '_3620.AGMAGleasonConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3620.AGMAGleasonConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6070.AGMAGleasonConicalGearMeshLoadCase') -> '_3620.AGMAGleasonConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3620.AGMAGleasonConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1885.CylindricalGearMesh') -> '_3659.CylindricalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3659.CylindricalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6113.CylindricalGearMeshLoadCase') -> '_3659.CylindricalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3659.CylindricalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1891.HypoidGearMesh') -> '_3673.HypoidGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3673.HypoidGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6154.HypoidGearMeshLoadCase') -> '_3673.HypoidGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3673.HypoidGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1894.KlingelnbergCycloPalloidConicalGearMesh') -> '_3678.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3678.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6160.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_3678.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3678.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1895.KlingelnbergCycloPalloidHypoidGearMesh') -> '_3681.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3681.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6163.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_3681.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3681.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_3684.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3684.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_3684.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3684.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1899.SpiralBevelGearMesh') -> '_3709.SpiralBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3709.SpiralBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6199.SpiralBevelGearMeshLoadCase') -> '_3709.SpiralBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3709.SpiralBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1903.StraightBevelGearMesh') -> '_3718.StraightBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3718.StraightBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6209.StraightBevelGearMeshLoadCase') -> '_3718.StraightBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3718.StraightBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1905.WormGearMesh') -> '_3733.WormGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3733.WormGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6230.WormGearMeshLoadCase') -> '_3733.WormGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3733.WormGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1907.ZerolBevelGearMesh') -> '_3736.ZerolBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3736.ZerolBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6233.ZerolBevelGearMeshLoadCase') -> '_3736.ZerolBevelGearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ZerolBevelGearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3736.ZerolBevelGearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1889.GearMesh') -> '_3669.GearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3669.GearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6140.GearMeshLoadCase') -> '_3669.GearMeshCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearMeshCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3669.GearMeshCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1915.PartToPartShearCouplingConnection') -> '_3692.PartToPartShearCouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3692.PartToPartShearCouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6176.PartToPartShearCouplingConnectionLoadCase') -> '_3692.PartToPartShearCouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartToPartShearCouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3692.PartToPartShearCouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1909.ClutchConnection') -> '_3637.ClutchConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3637.ClutchConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6087.ClutchConnectionLoadCase') -> '_3637.ClutchConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ClutchConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3637.ClutchConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1911.ConceptCouplingConnection') -> '_3642.ConceptCouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3642.ConceptCouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6092.ConceptCouplingConnectionLoadCase') -> '_3642.ConceptCouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptCouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3642.ConceptCouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1913.CouplingConnection') -> '_3653.CouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3653.CouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6105.CouplingConnectionLoadCase') -> '_3653.CouplingConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CouplingConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3653.CouplingConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1917.SpringDamperConnection') -> '_3712.SpringDamperConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3712.SpringDamperConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6201.SpringDamperConnectionLoadCase') -> '_3712.SpringDamperConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpringDamperConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3712.SpringDamperConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1919.TorqueConverterConnection') -> '_3727.TorqueConverterConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3727.TorqueConverterConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6219.TorqueConverterConnectionLoadCase') -> '_3727.TorqueConverterConnectionCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.TorqueConverterConnectionCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3727.TorqueConverterConnectionCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1996.AbstractAssembly') -> '_3617.AbstractAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AbstractAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3617.AbstractAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6066.AbstractAssemblyLoadCase') -> '_3617.AbstractAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AbstractAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3617.AbstractAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1997.AbstractShaftOrHousing') -> '_3618.AbstractShaftOrHousingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AbstractShaftOrHousingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3618.AbstractShaftOrHousingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6067.AbstractShaftOrHousingLoadCase') -> '_3618.AbstractShaftOrHousingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AbstractShaftOrHousingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3618.AbstractShaftOrHousingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2000.Bearing') -> '_3623.BearingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BearingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3623.BearingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6074.BearingLoadCase') -> '_3623.BearingCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BearingCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3623.BearingCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2002.Bolt') -> '_3634.BoltCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BoltCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3634.BoltCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6086.BoltLoadCase') -> '_3634.BoltCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BoltCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3634.BoltCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2003.BoltedJoint') -> '_3635.BoltedJointCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BoltedJointCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3635.BoltedJointCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6085.BoltedJointLoadCase') -> '_3635.BoltedJointCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BoltedJointCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3635.BoltedJointCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2004.Component') -> '_3640.ComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3640.ComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6091.ComponentLoadCase') -> '_3640.ComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3640.ComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2007.Connector') -> '_3651.ConnectorCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConnectorCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3651.ConnectorCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6104.ConnectorLoadCase') -> '_3651.ConnectorCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConnectorCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3651.ConnectorCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2008.Datum') -> '_3662.DatumCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.DatumCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3662.DatumCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6119.DatumLoadCase') -> '_3662.DatumCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.DatumCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3662.DatumCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2011.ExternalCADModel') -> '_3663.ExternalCADModelCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ExternalCADModelCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3663.ExternalCADModelCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6132.ExternalCADModelLoadCase') -> '_3663.ExternalCADModelCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ExternalCADModelCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3663.ExternalCADModelCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2012.FlexiblePinAssembly') -> '_3667.FlexiblePinAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FlexiblePinAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3667.FlexiblePinAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6136.FlexiblePinAssemblyLoadCase') -> '_3667.FlexiblePinAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FlexiblePinAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3667.FlexiblePinAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1995.Assembly') -> '_3622.AssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3622.AssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6073.AssemblyLoadCase') -> '_3622.AssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3622.AssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2013.GuideDxfModel') -> '_3671.GuideDxfModelCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GuideDxfModelCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3671.GuideDxfModelCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6144.GuideDxfModelLoadCase') -> '_3671.GuideDxfModelCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GuideDxfModelCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3671.GuideDxfModelCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2016.ImportedFEComponent') -> '_3675.ImportedFEComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ImportedFEComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3675.ImportedFEComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6156.ImportedFEComponentLoadCase') -> '_3675.ImportedFEComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ImportedFEComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3675.ImportedFEComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2020.MassDisc') -> '_3686.MassDiscCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MassDiscCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3686.MassDiscCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6168.MassDiscLoadCase') -> '_3686.MassDiscCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MassDiscCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3686.MassDiscCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2021.MeasurementComponent') -> '_3687.MeasurementComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MeasurementComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3687.MeasurementComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6169.MeasurementComponentLoadCase') -> '_3687.MeasurementComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MeasurementComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3687.MeasurementComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2022.MountableComponent') -> '_3688.MountableComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MountableComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3688.MountableComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6171.MountableComponentLoadCase') -> '_3688.MountableComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.MountableComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3688.MountableComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2024.OilSeal') -> '_3689.OilSealCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.OilSealCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3689.OilSealCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6173.OilSealLoadCase') -> '_3689.OilSealCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.OilSealCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3689.OilSealCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2026.Part') -> '_3690.PartCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3690.PartCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6175.PartLoadCase') -> '_3690.PartCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PartCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3690.PartCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2027.PlanetCarrier') -> '_3696.PlanetCarrierCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetCarrierCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3696.PlanetCarrierCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6182.PlanetCarrierLoadCase') -> '_3696.PlanetCarrierCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetCarrierCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3696.PlanetCarrierCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2029.PointLoad') -> '_3697.PointLoadCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PointLoadCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3697.PointLoadCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6185.PointLoadLoadCase') -> '_3697.PointLoadCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PointLoadCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3697.PointLoadCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2030.PowerLoad') -> '_3698.PowerLoadCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PowerLoadCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3698.PowerLoadCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6186.PowerLoadLoadCase') -> '_3698.PowerLoadCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PowerLoadCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3698.PowerLoadCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2032.RootAssembly') -> '_3703.RootAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RootAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3703.RootAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6192.RootAssemblyLoadCase') -> '_3703.RootAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RootAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3703.RootAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2034.SpecialisedAssembly') -> '_3707.SpecialisedAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpecialisedAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3707.SpecialisedAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6196.SpecialisedAssemblyLoadCase') -> '_3707.SpecialisedAssemblyCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpecialisedAssemblyCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3707.SpecialisedAssemblyCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2035.UnbalancedMass') -> '_3730.UnbalancedMassCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.UnbalancedMassCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3730.UnbalancedMassCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6227.UnbalancedMassLoadCase') -> '_3730.UnbalancedMassCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.UnbalancedMassCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3730.UnbalancedMassCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2036.VirtualComponent') -> '_3731.VirtualComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.VirtualComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3731.VirtualComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6228.VirtualComponentLoadCase') -> '_3731.VirtualComponentCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.VirtualComponentCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3731.VirtualComponentCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2039.Shaft') -> '_3704.ShaftCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3704.ShaftCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6194.ShaftLoadCase') -> '_3704.ShaftCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3704.ShaftCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2077.ConceptGear') -> '_3644.ConceptGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3644.ConceptGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6095.ConceptGearLoadCase') -> '_3644.ConceptGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3644.ConceptGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2078.ConceptGearSet') -> '_3646.ConceptGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3646.ConceptGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6097.ConceptGearSetLoadCase') -> '_3646.ConceptGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3646.ConceptGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2084.FaceGear') -> '_3664.FaceGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3664.FaceGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6133.FaceGearLoadCase') -> '_3664.FaceGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3664.FaceGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2085.FaceGearSet') -> '_3666.FaceGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3666.FaceGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6135.FaceGearSetLoadCase') -> '_3666.FaceGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.FaceGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3666.FaceGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2069.AGMAGleasonConicalGear') -> '_3619.AGMAGleasonConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3619.AGMAGleasonConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6069.AGMAGleasonConicalGearLoadCase') -> '_3619.AGMAGleasonConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3619.AGMAGleasonConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2070.AGMAGleasonConicalGearSet') -> '_3621.AGMAGleasonConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3621.AGMAGleasonConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6071.AGMAGleasonConicalGearSetLoadCase') -> '_3621.AGMAGleasonConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.AGMAGleasonConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3621.AGMAGleasonConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2071.BevelDifferentialGear') -> '_3626.BevelDifferentialGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3626.BevelDifferentialGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6077.BevelDifferentialGearLoadCase') -> '_3626.BevelDifferentialGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3626.BevelDifferentialGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2072.BevelDifferentialGearSet') -> '_3628.BevelDifferentialGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3628.BevelDifferentialGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6079.BevelDifferentialGearSetLoadCase') -> '_3628.BevelDifferentialGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3628.BevelDifferentialGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2073.BevelDifferentialPlanetGear') -> '_3629.BevelDifferentialPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3629.BevelDifferentialPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6080.BevelDifferentialPlanetGearLoadCase') -> '_3629.BevelDifferentialPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3629.BevelDifferentialPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2074.BevelDifferentialSunGear') -> '_3630.BevelDifferentialSunGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialSunGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3630.BevelDifferentialSunGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6081.BevelDifferentialSunGearLoadCase') -> '_3630.BevelDifferentialSunGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelDifferentialSunGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3630.BevelDifferentialSunGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2075.BevelGear') -> '_3631.BevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3631.BevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6082.BevelGearLoadCase') -> '_3631.BevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3631.BevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2076.BevelGearSet') -> '_3633.BevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3633.BevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6084.BevelGearSetLoadCase') -> '_3633.BevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.BevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3633.BevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2079.ConicalGear') -> '_3647.ConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3647.ConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6098.ConicalGearLoadCase') -> '_3647.ConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3647.ConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2080.ConicalGearSet') -> '_3649.ConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3649.ConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6102.ConicalGearSetLoadCase') -> '_3649.ConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3649.ConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2081.CylindricalGear') -> '_3658.CylindricalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3658.CylindricalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6111.CylindricalGearLoadCase') -> '_3658.CylindricalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3658.CylindricalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2082.CylindricalGearSet') -> '_3660.CylindricalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3660.CylindricalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6115.CylindricalGearSetLoadCase') -> '_3660.CylindricalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3660.CylindricalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2083.CylindricalPlanetGear') -> '_3661.CylindricalPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3661.CylindricalPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6116.CylindricalPlanetGearLoadCase') -> '_3661.CylindricalPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.CylindricalPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3661.CylindricalPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2086.Gear') -> '_3668.GearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3668.GearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6138.GearLoadCase') -> '_3668.GearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3668.GearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2088.GearSet') -> '_3670.GearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3670.GearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6143.GearSetLoadCase') -> '_3670.GearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.GearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3670.GearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2090.HypoidGear') -> '_3672.HypoidGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3672.HypoidGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6153.HypoidGearLoadCase') -> '_3672.HypoidGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3672.HypoidGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2091.HypoidGearSet') -> '_3674.HypoidGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3674.HypoidGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6155.HypoidGearSetLoadCase') -> '_3674.HypoidGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.HypoidGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3674.HypoidGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2092.KlingelnbergCycloPalloidConicalGear') -> '_3677.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3677.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6159.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_3677.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3677.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2093.KlingelnbergCycloPalloidConicalGearSet') -> '_3679.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3679.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6161.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_3679.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3679.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2094.KlingelnbergCycloPalloidHypoidGear') -> '_3680.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3680.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6162.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_3680.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3680.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2095.KlingelnbergCycloPalloidHypoidGearSet') -> '_3682.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3682.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6164.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_3682.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3682.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2096.KlingelnbergCycloPalloidSpiralBevelGear') -> '_3683.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3683.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6165.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_3683.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3683.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2097.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_3685.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3685.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_3685.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3685.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2098.PlanetaryGearSet') -> '_3695.PlanetaryGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetaryGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3695.PlanetaryGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6180.PlanetaryGearSetLoadCase') -> '_3695.PlanetaryGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.PlanetaryGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3695.PlanetaryGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2099.SpiralBevelGear') -> '_3708.SpiralBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3708.SpiralBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6198.SpiralBevelGearLoadCase') -> '_3708.SpiralBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3708.SpiralBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2100.SpiralBevelGearSet') -> '_3710.SpiralBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3710.SpiralBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6200.SpiralBevelGearSetLoadCase') -> '_3710.SpiralBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3710.SpiralBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2101.StraightBevelDiffGear') -> '_3714.StraightBevelDiffGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3714.StraightBevelDiffGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6205.StraightBevelDiffGearLoadCase') -> '_3714.StraightBevelDiffGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3714.StraightBevelDiffGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2102.StraightBevelDiffGearSet') -> '_3716.StraightBevelDiffGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3716.StraightBevelDiffGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6207.StraightBevelDiffGearSetLoadCase') -> '_3716.StraightBevelDiffGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelDiffGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3716.StraightBevelDiffGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2103.StraightBevelGear') -> '_3717.StraightBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3717.StraightBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6208.StraightBevelGearLoadCase') -> '_3717.StraightBevelGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3717.StraightBevelGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2104.StraightBevelGearSet') -> '_3719.StraightBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3719.StraightBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6210.StraightBevelGearSetLoadCase') -> '_3719.StraightBevelGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3719.StraightBevelGearSetCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2105.StraightBevelPlanetGear') -> '_3720.StraightBevelPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3720.StraightBevelPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6211.StraightBevelPlanetGearLoadCase') -> '_3720.StraightBevelPlanetGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelPlanetGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3720.StraightBevelPlanetGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2106.StraightBevelSunGear') -> '_3721.StraightBevelSunGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelSunGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3721.StraightBevelSunGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelSunGearLoadCase') -> '_3721.StraightBevelSunGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.StraightBevelSunGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3721.StraightBevelSunGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2107.WormGear') -> '_3732.WormGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3732.WormGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6229.WormGearLoadCase') -> '_3732.WormGearCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3732.WormGearCompoundParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2108.WormGearSet') -> '_3734.WormGearSetCompoundParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.compound.WormGearSetCompoundParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3734.WormGearSetCompoundParametricStudyTool)(method_result) if method_result else None
