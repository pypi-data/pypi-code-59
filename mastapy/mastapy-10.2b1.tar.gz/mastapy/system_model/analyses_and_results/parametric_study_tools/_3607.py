'''_3607.py

TorqueConverterPumpParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2158
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6221
from mastapy.system_model.analyses_and_results.system_deflections import _2351
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3516
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'TorqueConverterPumpParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpParametricStudyTool',)


class TorqueConverterPumpParametricStudyTool(_3516.CouplingHalfParametricStudyTool):
    '''TorqueConverterPumpParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2158.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2158.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6221.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6221.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2351.TorqueConverterPumpSystemDeflection]':
        '''List[TorqueConverterPumpSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2351.TorqueConverterPumpSystemDeflection))
        return value
