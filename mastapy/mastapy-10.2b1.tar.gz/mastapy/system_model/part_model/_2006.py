'''_2006.py

ConnectedSockets
'''


from mastapy.system_model.connections_and_sockets import (
    _1872, _1853, _1855, _1857,
    _1858, _1859, _1861, _1862,
    _1864, _1865, _1868, _1869,
    _1870, _1851, _1847, _1848,
    _1852, _1860, _1863, _1867,
    _1871
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _1876, _1878, _1880, _1882,
    _1884, _1886, _1888, _1890,
    _1892, _1893, _1897, _1898,
    _1900, _1902, _1904, _1906,
    _1908, _1875, _1877, _1879,
    _1881, _1883, _1885, _1887,
    _1889, _1891, _1894, _1895,
    _1896, _1899, _1901, _1903,
    _1905, _1907
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1910, _1912, _1914, _1916,
    _1918, _1920, _1921, _1909,
    _1911, _1913, _1915, _1917,
    _1919
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ConnectedSockets')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectedSockets',)


class ConnectedSockets(_0.APIBase):
    '''ConnectedSockets

    This is a mastapy class.
    '''

    TYPE = _CONNECTED_SOCKETS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectedSockets.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def socket_a(self) -> '_1872.Socket':
        '''Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1872.Socket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cvt_pulley_socket(self) -> '_1853.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1853.CVTPulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1853.CVTPulleySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_socket(self) -> '_1855.CylindricalSocket':
        '''CylindricalSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1855.CylindricalSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1855.CylindricalSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_electric_machine_stator_socket(self) -> '_1857.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1857.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1857.ElectricMachineStatorSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_connecting_socket(self) -> '_1858.InnerShaftConnectingSocket':
        '''InnerShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1858.InnerShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1858.InnerShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_socket(self) -> '_1859.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1859.InnerShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1859.InnerShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_connecting_socket(self) -> '_1861.OuterShaftConnectingSocket':
        '''OuterShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1861.OuterShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1861.OuterShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_socket(self) -> '_1862.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1862.OuterShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1862.OuterShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_planetary_socket(self) -> '_1864.PlanetarySocket':
        '''PlanetarySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1864.PlanetarySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1864.PlanetarySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_pulley_socket(self) -> '_1865.PulleySocket':
        '''PulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.PulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1865.PulleySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_rolling_ring_socket(self) -> '_1868.RollingRingSocket':
        '''RollingRingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1868.RollingRingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1868.RollingRingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_shaft_connecting_socket(self) -> '_1869.ShaftConnectingSocket':
        '''ShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.ShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1869.ShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_shaft_socket(self) -> '_1870.ShaftSocket':
        '''ShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1870.ShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1870.ShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1876.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1876.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1876.AGMAGleasonConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_differential_gear_teeth_socket(self) -> '_1878.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1878.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1878.BevelDifferentialGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_gear_teeth_socket(self) -> '_1880.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1880.BevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1880.BevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_gear_teeth_socket(self) -> '_1882.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1882.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1882.ConceptGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_conical_gear_teeth_socket(self) -> '_1884.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1884.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1884.ConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_gear_teeth_socket(self) -> '_1886.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1886.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1886.CylindricalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_face_gear_teeth_socket(self) -> '_1888.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1888.FaceGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1888.FaceGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_gear_teeth_socket(self) -> '_1890.GearTeethSocket':
        '''GearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1890.GearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1890.GearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_hypoid_gear_teeth_socket(self) -> '_1892.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1892.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1892.HypoidGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1893.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1893.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1893.KlingelnbergConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_1897.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1897.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1897.KlingelnbergHypoidGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_1898.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1898.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1898.KlingelnbergSpiralBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spiral_bevel_gear_teeth_socket(self) -> '_1900.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1900.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1900.SpiralBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_1902.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1902.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1902.StraightBevelDiffGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_gear_teeth_socket(self) -> '_1904.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1904.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1904.StraightBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_worm_gear_teeth_socket(self) -> '_1906.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1906.WormGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1906.WormGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_zerol_bevel_gear_teeth_socket(self) -> '_1908.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1908.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1908.ZerolBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_clutch_socket(self) -> '_1910.ClutchSocket':
        '''ClutchSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1910.ClutchSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1910.ClutchSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_coupling_socket(self) -> '_1912.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1912.ConceptCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1912.ConceptCouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_coupling_socket(self) -> '_1914.CouplingSocket':
        '''CouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1914.CouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1914.CouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_part_to_part_shear_coupling_socket(self) -> '_1916.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1916.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1916.PartToPartShearCouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spring_damper_socket(self) -> '_1918.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1918.SpringDamperSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1918.SpringDamperSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_pump_socket(self) -> '_1920.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1920.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1920.TorqueConverterPumpSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_turbine_socket(self) -> '_1921.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1921.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1921.TorqueConverterTurbineSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_b(self) -> '_1872.Socket':
        '''Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1872.Socket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cvt_pulley_socket(self) -> '_1853.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1853.CVTPulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1853.CVTPulleySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_socket(self) -> '_1855.CylindricalSocket':
        '''CylindricalSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1855.CylindricalSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1855.CylindricalSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_electric_machine_stator_socket(self) -> '_1857.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1857.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1857.ElectricMachineStatorSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_connecting_socket(self) -> '_1858.InnerShaftConnectingSocket':
        '''InnerShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1858.InnerShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1858.InnerShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_socket(self) -> '_1859.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1859.InnerShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1859.InnerShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_connecting_socket(self) -> '_1861.OuterShaftConnectingSocket':
        '''OuterShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1861.OuterShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1861.OuterShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_socket(self) -> '_1862.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1862.OuterShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1862.OuterShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_planetary_socket(self) -> '_1864.PlanetarySocket':
        '''PlanetarySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1864.PlanetarySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1864.PlanetarySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_pulley_socket(self) -> '_1865.PulleySocket':
        '''PulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.PulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1865.PulleySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_rolling_ring_socket(self) -> '_1868.RollingRingSocket':
        '''RollingRingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1868.RollingRingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1868.RollingRingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_shaft_connecting_socket(self) -> '_1869.ShaftConnectingSocket':
        '''ShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.ShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1869.ShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_shaft_socket(self) -> '_1870.ShaftSocket':
        '''ShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1870.ShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1870.ShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1876.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1876.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1876.AGMAGleasonConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_differential_gear_teeth_socket(self) -> '_1878.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1878.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1878.BevelDifferentialGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_gear_teeth_socket(self) -> '_1880.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1880.BevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1880.BevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_gear_teeth_socket(self) -> '_1882.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1882.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1882.ConceptGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_conical_gear_teeth_socket(self) -> '_1884.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1884.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1884.ConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_gear_teeth_socket(self) -> '_1886.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1886.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1886.CylindricalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_face_gear_teeth_socket(self) -> '_1888.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1888.FaceGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1888.FaceGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_gear_teeth_socket(self) -> '_1890.GearTeethSocket':
        '''GearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1890.GearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1890.GearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_hypoid_gear_teeth_socket(self) -> '_1892.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1892.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1892.HypoidGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1893.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1893.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1893.KlingelnbergConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_1897.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1897.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1897.KlingelnbergHypoidGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_1898.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1898.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1898.KlingelnbergSpiralBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spiral_bevel_gear_teeth_socket(self) -> '_1900.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1900.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1900.SpiralBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_1902.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1902.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1902.StraightBevelDiffGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_gear_teeth_socket(self) -> '_1904.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1904.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1904.StraightBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_worm_gear_teeth_socket(self) -> '_1906.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1906.WormGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1906.WormGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_zerol_bevel_gear_teeth_socket(self) -> '_1908.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1908.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1908.ZerolBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_clutch_socket(self) -> '_1910.ClutchSocket':
        '''ClutchSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1910.ClutchSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1910.ClutchSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_coupling_socket(self) -> '_1912.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1912.ConceptCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1912.ConceptCouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_coupling_socket(self) -> '_1914.CouplingSocket':
        '''CouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1914.CouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1914.CouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_part_to_part_shear_coupling_socket(self) -> '_1916.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1916.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1916.PartToPartShearCouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spring_damper_socket(self) -> '_1918.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1918.SpringDamperSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1918.SpringDamperSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_pump_socket(self) -> '_1920.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1920.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1920.TorqueConverterPumpSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_turbine_socket(self) -> '_1921.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1921.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1921.TorqueConverterTurbineSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def connection(self) -> '_1851.Connection':
        '''Connection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1851.Connection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_belt_connection(self) -> '_1847.BeltConnection':
        '''BeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1847.BeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1847.BeltConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coaxial_connection(self) -> '_1848.CoaxialConnection':
        '''CoaxialConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1848.CoaxialConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CoaxialConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1848.CoaxialConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cvt_belt_connection(self) -> '_1852.CVTBeltConnection':
        '''CVTBeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1852.CVTBeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CVTBeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1852.CVTBeltConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_inter_mountable_component_connection(self) -> '_1860.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1860.InterMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1860.InterMountableComponentConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_planetary_connection(self) -> '_1863.PlanetaryConnection':
        '''PlanetaryConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1863.PlanetaryConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PlanetaryConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1863.PlanetaryConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_rolling_ring_connection(self) -> '_1867.RollingRingConnection':
        '''RollingRingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1867.RollingRingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RollingRingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1867.RollingRingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_shaft_to_mountable_component_connection(self) -> '_1871.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1871.ShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1871.ShaftToMountableComponentConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_1875.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1875.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1875.AGMAGleasonConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_differential_gear_mesh(self) -> '_1877.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1877.BevelDifferentialGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1877.BevelDifferentialGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_gear_mesh(self) -> '_1879.BevelGearMesh':
        '''BevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1879.BevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1879.BevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_gear_mesh(self) -> '_1881.ConceptGearMesh':
        '''ConceptGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1881.ConceptGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1881.ConceptGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_conical_gear_mesh(self) -> '_1883.ConicalGearMesh':
        '''ConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1883.ConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1883.ConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cylindrical_gear_mesh(self) -> '_1885.CylindricalGearMesh':
        '''CylindricalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1885.CylindricalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1885.CylindricalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_face_gear_mesh(self) -> '_1887.FaceGearMesh':
        '''FaceGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1887.FaceGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to FaceGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1887.FaceGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_gear_mesh(self) -> '_1889.GearMesh':
        '''GearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1889.GearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to GearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1889.GearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_hypoid_gear_mesh(self) -> '_1891.HypoidGearMesh':
        '''HypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1891.HypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to HypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1891.HypoidGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1894.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1894.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1894.KlingelnbergCycloPalloidConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_1895.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1895.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1895.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1896.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1896.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spiral_bevel_gear_mesh(self) -> '_1899.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1899.SpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1899.SpiralBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_1901.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1901.StraightBevelDiffGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1901.StraightBevelDiffGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_gear_mesh(self) -> '_1903.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1903.StraightBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1903.StraightBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_worm_gear_mesh(self) -> '_1905.WormGearMesh':
        '''WormGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1905.WormGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to WormGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1905.WormGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_zerol_bevel_gear_mesh(self) -> '_1907.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1907.ZerolBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1907.ZerolBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_clutch_connection(self) -> '_1909.ClutchConnection':
        '''ClutchConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1909.ClutchConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ClutchConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1909.ClutchConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_coupling_connection(self) -> '_1911.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1911.ConceptCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1911.ConceptCouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coupling_connection(self) -> '_1913.CouplingConnection':
        '''CouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1913.CouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1913.CouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_part_to_part_shear_coupling_connection(self) -> '_1915.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1915.PartToPartShearCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1915.PartToPartShearCouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spring_damper_connection(self) -> '_1917.SpringDamperConnection':
        '''SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1917.SpringDamperConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpringDamperConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1917.SpringDamperConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_torque_converter_connection(self) -> '_1919.TorqueConverterConnection':
        '''TorqueConverterConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1919.TorqueConverterConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1919.TorqueConverterConnection)(self.wrapped.Connection) if self.wrapped.Connection else None
