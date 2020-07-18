import urllib.request
from urllib.error import HTTPError
from collections import namedtuple
from distutils.util import strtobool

from dateutil.parser import parse as date_parse

from epiw import type


def desc(station_type):
    category, period = station_type

    url = f'https://aggregate.epinet.kr/station/{category}/{period}/csv/'
    req = urllib.request.urlopen(url)
    rep = req.read().decode('utf-8')
    rows = rep.splitlines()
    header, body = rows[0], rows[1:]

    Field = namedtuple('Field', header)

    return tuple(Field(*row.split(',')) for row in body)


def convert(field_name, value):
    if not value:
        return None

    converter = {
        'tm': date_parse,
        'ws_gst_tm': date_parse,
        'stn_id': int,
        'src': str,
        'ir': lambda x: bool(strtobool(x)),
        'ix': lambda x: bool(strtobool(x)),
    }.get(field_name, float)

    try:
        return converter(value)
    except ValueError as e:
        raise ValueError(f'Can not found a converter: field_name:{field_name}, value:{value}') from e


def read(category, interval, begin, until, stations='', fields='', lonlat=''):
    if isinstance(fields, str):
        fields = fields.split(',')

    if isinstance(stations, str):
        stations = stations.split(',')
    elif isinstance(stations, int):
        stations = [stations]

    if isinstance(lonlat, str):
        lonlat = lonlat.split(',')

    stations = ','.join(map(str, stations))
    fields = ','.join(map(str, fields))
    lonlat = ','.join(map(str, lonlat))

    url = f'https://aggregate.epinet.kr/station/{category}/{interval}/?begin={begin}&until={until}&stn_id={stations}&field={fields}&lonlat={lonlat}'
    try:
        req = urllib.request.urlopen(url)
    except HTTPError as e:
        content = e.fp.read().decode('utf-8')
        print(f'# URL: {url}')
        print(f'# content: {content}')
        raise e
    rep = req.read().decode('utf-8')
    rows = rep.splitlines()
    header, body = rows[0], rows[1:]

    header = header.split(',')

    Field = namedtuple('Field', header)

    body = [row.split(',') for row in body]
    body = [[convert(*hr) for hr in zip(header, row)] for row in body]

    return tuple(Field(*row) for row in body)


def daily_weather_desc():
    return desc(type.STATION_WEATHER_DAILY)


def hourly_weather_desc():
    return desc(type.STATION_WEATHER_HOURLY)


def hourly_weather(begin, until):
    return read('weather', 'hourly', begin, until)


def daily_weather(begin, until):
    return read('weather', 'daily', begin, until)
