'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2043 import ConcentricOrParallelPartGroup
    from ._2044 import ConcentricPartGroup
    from ._2045 import ConcentricPartGroupParallelToThis
    from ._2046 import DesignMeasurements
    from ._2047 import ParallelPartGroup
    from ._2048 import PartGroup
