from procmon_parser.logs import *
from procmon_parser.construct_logs_format import *
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


# with open(r"C:\Temp\LogFileLocalTestMy-2.PML", "rb") as f:
#     data = f.read()
#
# start = time.time()
# logs_reader = ProcmonLogsReader(BytesIO(data))
# print(f"took {time.time() - start} fucking seconds to load")
# print(logs_reader[554953])
# print(logs_reader[554954])
# for i, event in enumerate(logs_reader):
#     pass


from procmon_parser.stream_logs_format import PMLStreamReader
from procmon_parser.consts import EventClass
f = open(r"C:\Temp\LogfileTetss64bitUTC.PML", "rb")
reader = PMLStreamReader(f)
# for a in pml._strings_table:
#     print(a)
#
# p = reader._process_table[575]
# print(p.pid)
# print(p.modules[0].base_address)
#
# print(reader._hostnames_table.values())
# print(reader._ports_table.values())

for i in range(reader.number_of_events):
    e = reader.get_event_at_offset(reader.events_offsets[i])
    if e.event_class == EventClass.Process:
        print(e)
