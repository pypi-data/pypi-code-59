'''_6508.py

ConnectionStaticLoadAnalysisCase
'''


from mastapy.system_model.analyses_and_results.analysis_cases import _6505
from mastapy._internal.python_net import python_net_import

_CONNECTION_STATIC_LOAD_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'ConnectionStaticLoadAnalysisCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionStaticLoadAnalysisCase',)


class ConnectionStaticLoadAnalysisCase(_6505.ConnectionAnalysisCase):
    '''ConnectionStaticLoadAnalysisCase

    This is a mastapy class.
    '''

    TYPE = _CONNECTION_STATIC_LOAD_ANALYSIS_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectionStaticLoadAnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
