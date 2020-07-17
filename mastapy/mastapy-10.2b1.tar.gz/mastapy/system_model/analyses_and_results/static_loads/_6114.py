'''_6114.py

CylindricalGearSetHarmonicLoadData
'''


from mastapy.system_model.analyses_and_results.static_loads import _6142
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetHarmonicLoadData',)


class CylindricalGearSetHarmonicLoadData(_6142.GearSetHarmonicLoadData):
    '''CylindricalGearSetHarmonicLoadData

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
