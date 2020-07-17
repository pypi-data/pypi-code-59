'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2111 import BoostPressureInputOptions
    from ._2112 import InputPowerInputOptions
    from ._2113 import PressureRatioInputOptions
    from ._2114 import RotorSetDataInputFileOptions
    from ._2115 import RotorSetMeasuredPoint
    from ._2116 import RotorSpeedInputOptions
    from ._2117 import SuperchargerMap
    from ._2118 import SuperchargerMaps
    from ._2119 import SuperchargerRotorSet
    from ._2120 import SuperchargerRotorSetDatabase
    from ._2121 import YVariableForImportedData
