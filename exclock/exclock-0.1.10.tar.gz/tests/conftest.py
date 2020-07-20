#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

sys.path.append(str(Path('__file__').resolve().parent))
os.environ['EXCLOCK_CLOCK_DIR'] = str(Path(__file__).parent / "data" / "clock_in_sys")
os.environ['EXCLOCK_SOUND_DIR'] = str(Path(__file__).parent / "data" / "sound_in_sys")

if 'EXCLOCK_RING_FILENAME' in os.environ:
    del os.environ['EXCLOCK_RING_FILENAME']
