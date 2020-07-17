import os
import datetime
import exifread

def calculate_days(file_path, *, birthday=datetime.datetime(1970, 1, 1), offset=datetime.timedelta(), methods=('exif',)):
    photo_taken = _get_date_time(file_path, methods)
    if photo_taken is None:
        return None
    delta = photo_taken - (birthday + offset)
    return delta.days


def _get_date_time(file_path, methods):
    if 'exif' in methods:
        date_time = _get_date_time_from_exif(file_path)
    if date_time is None and 'stat' in methods:
        date_time = _get_date_time_from_stat(file_path)
    return date_time


def _get_date_time_from_exif(file_path):
    keys = [
        'EXIF DateTimeOriginal',
        'EXIF DateTimeDigitized',
        'Image DateTime',
    ]
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        for key in keys:
            if key in tags:
                tag = tags[key]
                return datetime.datetime.strptime(tag.values, '%Y:%m:%d %H:%M:%S')


def _get_date_time_from_stat(file_path):
    stat = os.stat(file_path)
    try:
        timestamp = stat.st_birthtime
        return datetime.datetime.fromtimestamp(timestamp)
    except AttributeError:
        return None
