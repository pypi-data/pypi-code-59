#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pathlib
import sys
import argparse
from user_tools import util_json

ROOT_DIR = pathlib.Path(__file__).parent
sys.path.append(ROOT_DIR.__str__())

from util_zabbix import pyzabbix
