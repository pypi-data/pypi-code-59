'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1909 import ClutchConnection
    from ._1910 import ClutchSocket
    from ._1911 import ConceptCouplingConnection
    from ._1912 import ConceptCouplingSocket
    from ._1913 import CouplingConnection
    from ._1914 import CouplingSocket
    from ._1915 import PartToPartShearCouplingConnection
    from ._1916 import PartToPartShearCouplingSocket
    from ._1917 import SpringDamperConnection
    from ._1918 import SpringDamperSocket
    from ._1919 import TorqueConverterConnection
    from ._1920 import TorqueConverterPumpSocket
    from ._1921 import TorqueConverterTurbineSocket
