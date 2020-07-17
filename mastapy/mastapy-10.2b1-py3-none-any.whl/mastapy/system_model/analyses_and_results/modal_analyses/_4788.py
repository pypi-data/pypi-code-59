'''_4788.py

MeasurementComponentModalAnalysis
'''


from mastapy.system_model.part_model import _2021
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6169
from mastapy.system_model.analyses_and_results.system_deflections import _2305
from mastapy.system_model.analyses_and_results.modal_analyses import _4838
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'MeasurementComponentModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentModalAnalysis',)


class MeasurementComponentModalAnalysis(_4838.VirtualComponentModalAnalysis):
    '''MeasurementComponentModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2021.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2021.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6169.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6169.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2305.MeasurementComponentSystemDeflection':
        '''MeasurementComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2305.MeasurementComponentSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
