'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1807 import Design
    from ._1808 import ComponentDampingOption
    from ._1809 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._1810 import DesignEntity
    from ._1811 import DesignEntityId
    from ._1812 import DutyCycleImporter
    from ._1813 import DutyCycleImporterDesignEntityMatch
    from ._1814 import ExternalFullFELoader
    from ._1815 import HypoidWindUpRemovalMethod
    from ._1816 import IncludeDutyCycleOption
    from ._1817 import MemorySummary
    from ._1818 import MeshStiffnessModel
    from ._1819 import PowerLoadDragTorqueSpecificationMethod
    from ._1820 import PowerLoadInputTorqueSpecificationMethod
    from ._1821 import PowerLoadPIDControlSpeedInputType
    from ._1822 import PowerLoadType
    from ._1823 import RelativeComponentAlignment
    from ._1824 import RelativeOffsetOption
    from ._1825 import SystemReporting
    from ._1826 import TransmissionTemperatureSet
