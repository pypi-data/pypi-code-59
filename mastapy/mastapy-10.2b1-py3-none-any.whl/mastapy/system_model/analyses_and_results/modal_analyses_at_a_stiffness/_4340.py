'''_4340.py

TorqueConverterConnectionModalAnalysisAtAStiffness
'''


from mastapy.system_model.connections_and_sockets.couplings import _1919
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6219
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4264
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'TorqueConverterConnectionModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionModalAnalysisAtAStiffness',)


class TorqueConverterConnectionModalAnalysisAtAStiffness(_4264.CouplingConnectionModalAnalysisAtAStiffness):
    '''TorqueConverterConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1919.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1919.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6219.TorqueConverterConnectionLoadCase':
        '''TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6219.TorqueConverterConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
