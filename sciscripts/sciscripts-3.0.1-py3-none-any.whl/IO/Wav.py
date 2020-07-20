#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: T. Malfatti <malfatti@disroot.org>
@date: 20200506
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts
"""

import numpy as np
import os

from glob import glob
from scipy.io import wavfile

def Read(File):
    Rate, Data = wavfile.read(File)
    return(Data, Rate)

def Write(Data, Rate, File):
    if '.' not in File: File +='.dat'
    if '/' in File: os.makedirs('/'.join(File.split('/')[:-1]), exist_ok=True)

    wavfile.write(File, Rate, Data)

