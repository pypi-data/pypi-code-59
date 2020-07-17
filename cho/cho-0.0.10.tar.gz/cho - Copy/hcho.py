import os
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from pathlib import Path

def retrieve_hcho(date_range, download_folder = "data/hcho"):
    pass