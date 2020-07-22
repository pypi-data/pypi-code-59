#!/usr/bin/env python
from cbapi.response import Sensor, CbResponseAPI
import logging
logging.basicConfig(level=logging.DEBUG)
import sys


cb = CbResponseAPI(timeout=500)

sensor = cb.select(Sensor, "4")
with sensor.lr_session() as session:
    session.list_directory("/Users/bit9qa")
    session.delete_file("/Users/bit9qa/hello.txt")
    session.put_file(open("hello.txt", "rb"), "/Users/bit9qa/hello.txt")
    print(session.get_file("/Users/bit9qa/hello.txt"))
