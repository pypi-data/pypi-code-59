import collections
import json
import os.path
import struct
import serial
import time
import threading
import tempfile
import shutil
import queue

from roktools import logger

from . import core
from . import constants
from . import helpers
from . import SERIAL_PORT_STR

CONFIG_GROUPS_DEFAULT = [constants.CONSTELLATIONS_STR, constants.SIGNALS_STR, 
                            constants.RATES_STR, constants.MEAS_PROP_STR]

# ------------------------------------------------------------------------------

def get(serial_stream, config_groups=CONFIG_GROUPS_DEFAULT):

    key_ids = []

    for config_group in config_groups:
        key_ids += CONFIG_OPTIONS[config_group].key_ids

    config = {}

    try:
        key_values = core.submit_valget_packet(key_ids, serial_stream)
        for group in config_groups:
            config[group] = CONFIG_OPTIONS[group].config_builder(key_values)

    except:
        pass

    return config

def set_from_ucenter_file(serial_stream, fh):

    res = False

    if fh.readable():
        for line in fh:
            submit_res = core.submit_valset_from_valget_line(line, serial_stream)
            if submit_res:
                logger.info('Applied config line [ {} ]'.format(line))
            else:
                logger.warning('Could not apply config line [ {} ]'.format(line))

            res = res or submit_res
            time.sleep(0.2)

    return res

def set_from_json_file(serial_stream, fh):

    res = False

    if fh.readable():
        res = set_from_dict(serial_stream, json.loads(fh.read()))
        time.sleep(0.2)

    return res


def set_from_dict(serial_stream, config_dict):

    logger.debug(f'Incoming configuration parameters {config_dict}')
    config = {}

    group_config = config_dict.get(constants.RATES_STR, None)
    if group_config:
        logger.debug(f'Incoming configuration parameters (rates) {group_config}')

        solution = group_config.get(constants.SOLUTION_STR, None)
        measurements = group_config.get(constants.MEASUREMENTS_STR, None)
        ephemeris = group_config.get(constants.EPHEMERIS_STR, None)
        rate_config = __build_dict_with_rate_config__(solution=solution, measurements=measurements, ephemeris=ephemeris)
        config.update(rate_config)

    group_config = config_dict.get(constants.SIGNALS_STR, None)
    if group_config:
        for key_id, signal_props in SIGNAL_PROPERTIES.items():
            constellation = signal_props.constellation
            channel = signal_props.channel

            config[key_id] = constellation in group_config and channel in group_config[constellation]

    group_config = config_dict.get(constants.CONSTELLATIONS_STR, None)
    if group_config:
        for key_id, constellation in KEY_ID_TO_CONSTELLATION.items():
            config[key_id] = constellation in group_config

    group_config = config_dict.get(constants.MEAS_PROP_STR, None)
    if group_config:
        smoothing_enabled = group_config.get('smoothing', False)
        config[core.KeyId.CFG_NAVSPG_USE_PPP] = smoothing_enabled 
                
    if config:
        logger.debug(f'Configuration to apply {config}')
        core.submit_valset_packet(config, serial_stream)
        return True
    
    else:
        logger.warning('No configuration has been applied')
        return False

def __build_dict_with_rate_config__(solution=None, measurements=None, ephemeris=None):

    config = {}

    logger.debug(f'__build_dict_with_rate_config__ [{solution}] [{measurements}] [{ephemeris}]')

    min_meas_rate_s = None

    if measurements:
        key_id = core.KeyId.CFG_RATE_MEAS
        value = measurements
        value = max(value, min_meas_rate_s) if min_meas_rate_s else value
        config[key_id] = int(value * 1000) # s -> ms
        config[core.KeyId.CFG_MSGOUT_UBX_RXM_RAWX_USB] = 1

    if solution:
        key_id = core.KeyId.CFG_RATE_NAV
        ratio = max(1, int(solution / measurements) if measurements else 1)
        logger.debug(f'Solution ration meas: [ {measurements} ], solution [{solution} ], ratio [{ratio}]')
        config[key_id] = ratio
        config[core.KeyId.CFG_MSGOUT_UBX_NAV_POSECEF_USB] = 1        

    if ephemeris:
        config[core.KeyId.CFG_MSGOUT_UBX_RXM_SFRBX_USB] = 1
    logger.debug(f'__build_dict_with_rate_config__ [{config}]')

    return config

def __build_constellation__(key_values):

    constellations = []

    keys = key_values.keys()
    config_key_ids = CONFIG_OPTIONS[constants.CONSTELLATIONS_STR].key_ids
    for key_id in list(set(keys) & set(config_key_ids)):
        value = key_values[key_id]
        constellation_enabled = core.parse_key_id_value(key_id, value)

        if constellation_enabled:
            constellations.append(KEY_ID_TO_CONSTELLATION[key_id])

    return constellations


def __build_signals__(key_values):

    signals = {}

    keys = key_values.keys()
    config_key_ids = CONFIG_OPTIONS[constants.SIGNALS_STR].key_ids
    for key_id in list(set(keys) & set(config_key_ids)):

        active = core.parse_key_id_value(key_id, key_values[key_id])
        if active:
            signal_properties = SIGNAL_PROPERTIES[key_id]
            constellation = signal_properties.constellation
            if constellation not in signals:
                signals[constellation] = []

            signals[constellation].append(signal_properties.channel)
            
    return signals


def __build_rates__(key_values):

    values = {}
    for key_id in CONFIG_OPTIONS[constants.RATES_STR].key_ids:
        values[key_id] = core.parse_key_id_value(key_id, key_values[key_id])

    rates = {
        constants.MEASUREMENTS_STR : 
            values[core.KeyId.CFG_RATE_MEAS] * 
            values[core.KeyId.CFG_MSGOUT_UBX_RXM_RAWX_USB] / 1.0e3,
        constants.SOLUTION_STR : 
            values[core.KeyId.CFG_RATE_NAV] *
            values[core.KeyId.CFG_MSGOUT_UBX_NAV_POSECEF_USB],
        constants.EPHEMERIS_STR : 
            values[core.KeyId.CFG_MSGOUT_UBX_RXM_SFRBX_USB]
    }

    return rates


def __build_meas_prop__(key_values):

    props = {}

    keys = key_values.keys()
    config_key_ids = CONFIG_OPTIONS[constants.MEAS_PROP_STR].key_ids
    for key_id in list(set(keys) & set(config_key_ids)):
        if key_id == core.KeyId.CFG_NAVSPG_USE_PPP:
            props['smoothing'] = core.parse_key_id_value(key_id, key_values[key_id]) 

    return props

#def get_constellations(serial_stream):
#
#    key_ids = CONSTELLATION_KEY_IDS
#
#    config_constellations = core.submit_valget_packet(key_ids, serial_stream)
#
#    config_signals = get_signals(serial_stream)
#
#    return __
#
#
#    for key_id in key_ids:
#        value = config_constellations[key_id]
#        constellation_enabled = core.parse_key_id_value(key_id, value)
#
#        constellation = KEY_ID_TO_CONSTELLATION[key_id]
#
#        if constellation_enabled and constellation in config_signals:
#            constellations.append(constellation)
#
#    return constellations


ConfigOptions = collections.namedtuple('ConfigOptions', ['key_ids', 'config_builder'])
CONFIG_OPTIONS = {
    constants.CONSTELLATIONS_STR : ConfigOptions([
        core.KeyId.CFG_SIGNAL_GPS_ENA,
        core.KeyId.CFG_SIGNAL_GAL_ENA,
        core.KeyId.CFG_SIGNAL_BDS_ENA,
        core.KeyId.CFG_SIGNAL_QZSS_ENA,
        core.KeyId.CFG_SIGNAL_GLO_ENA
    ], __build_constellation__),

    constants.SIGNALS_STR : ConfigOptions([
        core.KeyId.CFG_SIGNAL_GPS_L1CA_ENA,  core.KeyId.CFG_SIGNAL_GPS_L2C_ENA,   
        core.KeyId.CFG_SIGNAL_GAL_E1_ENA,    core.KeyId.CFG_SIGNAL_GAL_E5B_ENA,   
        core.KeyId.CFG_SIGNAL_BDS_B1_ENA,    core.KeyId.CFG_SIGNAL_BDS_B2_ENA,    
        core.KeyId.CFG_SIGNAL_QZSS_L1CA_ENA, core.KeyId.CFG_SIGNAL_QZSS_L2C_ENA,  
        core.KeyId.CFG_SIGNAL_GLO_L1_ENA,    core.KeyId.CFG_SIGNAL_GLO_L2_ENA,    
    ], __build_signals__),

    constants.RATES_STR : ConfigOptions([
        core.KeyId.CFG_RATE_MEAS,
        core.KeyId.CFG_RATE_NAV,
        core.KeyId.CFG_MSGOUT_UBX_RXM_RAWX_USB,
        core.KeyId.CFG_MSGOUT_UBX_NAV_POSECEF_USB,
        core.KeyId.CFG_MSGOUT_UBX_RXM_SFRBX_USB
    ], __build_rates__),

    constants.MEAS_PROP_STR : ConfigOptions([
        core.KeyId.CFG_NAVSPG_USE_PPP
    ], __build_meas_prop__)

}


SignalProperties = collections.namedtuple('SignalProperties', ['constellation', 'channel'])
SIGNAL_PROPERTIES = {
    core.KeyId.CFG_SIGNAL_GPS_L1CA_ENA: SignalProperties(constants.GPS_STR, '1C'),
    core.KeyId.CFG_SIGNAL_GPS_L2C_ENA: SignalProperties(constants.GPS_STR,'2C'),
    core.KeyId.CFG_SIGNAL_GAL_E1_ENA: SignalProperties(constants.GAL_STR,'1C'),
    core.KeyId.CFG_SIGNAL_GAL_E5B_ENA: SignalProperties(constants.GAL_STR,'7B'),   
    core.KeyId.CFG_SIGNAL_BDS_B1_ENA: SignalProperties(constants.BDS_STR,'2I'),
    core.KeyId.CFG_SIGNAL_BDS_B2_ENA: SignalProperties(constants.BDS_STR,'7I'),    
    core.KeyId.CFG_SIGNAL_QZSS_L1CA_ENA: SignalProperties(constants.QZSS_STR,'1C'),
    core.KeyId.CFG_SIGNAL_QZSS_L2C_ENA: SignalProperties(constants.QZSS_STR,'2L'),  
    core.KeyId.CFG_SIGNAL_GLO_L1_ENA: SignalProperties(constants.GLO_STR,'1C'),
    core.KeyId.CFG_SIGNAL_GLO_L2_ENA: SignalProperties(constants.GLO_STR,'2C'),
}

KEY_ID_TO_CONSTELLATION = {
    core.KeyId.CFG_SIGNAL_GPS_ENA:  constants.GPS_STR,
    core.KeyId.CFG_SIGNAL_GAL_ENA:  constants.GAL_STR,
    core.KeyId.CFG_SIGNAL_BDS_ENA:  constants.BDS_STR,
    core.KeyId.CFG_SIGNAL_QZSS_ENA: constants.QZSS_STR,
    core.KeyId.CFG_SIGNAL_GLO_ENA:  constants.GLO_STR 
}
