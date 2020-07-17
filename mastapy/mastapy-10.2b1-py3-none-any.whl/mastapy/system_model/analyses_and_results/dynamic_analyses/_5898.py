'''_5898.py

PowerLoadDynamicAnalysis
'''


from mastapy.system_model.part_model import _2030
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6186
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5931
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'PowerLoadDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadDynamicAnalysis',)


class PowerLoadDynamicAnalysis(_5931.VirtualComponentDynamicAnalysis):
    '''PowerLoadDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2030.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2030.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6186.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6186.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
