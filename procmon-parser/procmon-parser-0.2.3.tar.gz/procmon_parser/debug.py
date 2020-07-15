from procmon_parser.logs import *
from procmon_parser.logs_format import *
from procmon_parser import *
from procmon_parser.logs import EventClass
from tests.test_logs_format import check_pml_equals_csv
from io import BytesIO

from csv import DictReader
from procmon_parser import ProcmonLogsReader
from itertools import chain
import glob
import time

import cProfile


with open(r"C:\Temp\LogFileLocalTestMy-2.PML", "rb") as f:
    data = f.read()

start = time.time()
logs_reader = ProcmonLogsReader(BytesIO(data))
print(f"took {time.time() - start} fucking seconds to load")
print(logs_reader[554953])
print(logs_reader[554954])
for i, event in enumerate(logs_reader):
    pass
