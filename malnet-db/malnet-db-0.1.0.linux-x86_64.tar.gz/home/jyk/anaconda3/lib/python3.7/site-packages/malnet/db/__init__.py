"""malnet db package"""
from .fs import MalnetFS, CollectFS
from .model import (Sample, Task, VirusTotalAnalysis, PackerAnalysis,
                    StaticAnalysis, DynamicAnalysis, MALDB, createSampleTable,
                    dropSampleTable)
from .test import genTestSample, genTestTask
from .utils import md52Bucket, md52Object

__version__ = "0.1.0"
