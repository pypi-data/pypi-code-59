'''_4914.py

GearMeshCompoundModalAnalysis
'''


from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4921
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'GearMeshCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundModalAnalysis',)


class GearMeshCompoundModalAnalysis(_4921.InterMountableComponentConnectionCompoundModalAnalysis):
    '''GearMeshCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _GEAR_MESH_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
