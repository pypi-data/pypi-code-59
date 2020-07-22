#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:15:48 2016

@author: lidar2
"""
import os
from tools.geom_dtf import feature_id, geom_prop, mask_layers
from readers.read_scc_db import read_scc_db
from readers.get_files import database
from readers.parse_config import parse_config
from export.export_nc import export_nc, nc_name
from export.update_scc_db import update
from readers.read_config import config
import warnings
# from export.debug_layers import debug_layers

###############################################################################
# O) Definitions
###############################################################################

#Ignores all warnings --> they are not printed in terminal
warnings.filterwarnings('ignore')

meas_id, cfg_path = parse_config()

#Reading of the configuration file    
cfg = config(cfg_path)

# Threshold to select the sharpest peaks (80% less sharp than the sharpest)
margin = 0.63

# Get array of input files from an scc database query
files, rpath, exts, alphas, det_lims, ids = database(meas_id, cfg = cfg)

# Input/output directories
dir_out = '../output/'


###############################################################################
# A) Preprocessing
###############################################################################
# A.1) Clean output folder
# for root, dirs, files in os.walk(dir_out):
#     for f in files:
#         if len(f) > 0:
#             os.unlink(os.path.join(root,f))
            
# A.2) Reading lidar profiles
# Optical Profiles
print('-- Reading SCC files!')
dt_start_arr, alt_arr, prod_arr, metadata = \
read_scc_db(files, end_fill = alphas)


###############################################################################
# B) Geometrical retrievals
############################################################################### 
print('-- Proceding to layering algorithm!')
list_geom = []
list_dates = []
for i in range(0, len(alt_arr)):
    norm = prod_arr[i]/det_lims[i]
    
# B.1) Identify layers and each base and top
    rl_flag, bases, tops, wct = feature_id(alt_arr[i], norm,
                                           alpha = alphas[i], 
                                           peak_margin = margin)
    
# B.2) Use base and top to the profile to extract aditional 
# geometrical properties
    geom = geom_prop(rl_flag, bases, tops, alt_arr[i], norm)
    
# B.3) Filter out irregular features
    geom = mask_layers(geom)

    
###############################################################################
# C) Exporting
############################################################################### 
    if len(geom) > 0:
# C.1) Export to figures
        # debug_layers(dt_start_arr[i], exts[i], alt_arr[i], wct,
        #              prod_arr[i], geom, det_lims[i], dir_out)
        
# C.2) Export to netcdf
# C.2.i) Netcdf filename
        fname = nc_name(metadata[i], dt_start_arr[i], exts[i])
        
# C.2.ii) Netcdf file        
        geom_dts = export_nc(geom, metadata[i], alphas[i], exts, 
                             det_lims[i], fname, dir_out)
        
# C.3) Save in lists
        list_dates.append(dt_start_arr[i])
        list_geom.append(geom)
        
        fpath = os.path.join(rpath[i],fname)
        update(fpath, meas_id = meas_id, prod_id = ids[i], cfg = cfg)