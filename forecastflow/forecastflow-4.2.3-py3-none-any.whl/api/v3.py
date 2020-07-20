import json
import logging
from pathlib import Path
from typing import Optional, Union

import requests

from forecastflow import config
from forecastflow.enums import DataSourceLabel
from forecastflow.firebase_api import storage
from forecastflow.training import TrainingSettings

logger = logging.getLogger(__name__)


def create_data_source(uid: str, id_token: str, pid: str, path_to_file: Union[Path, str],
                       name: str, description: str, label: DataSourceLabel):
    if type(path_to_file) == str:
        path_to_file = Path(path_to_file)
    if not path_to_file.exists():
        raise Exception("Path '{}' does not exist.".format(path_to_file))
    size = path_to_file.stat().st_size
    api_base_url = config.forecastflow['api_base_url']
    res_create = requests.post(
        f"{api_base_url}/v3/createdatasource",
        data=json.dumps({
            'idToken': id_token,
            'pid': pid,
            'name': name,
            'desc': description,
            'label': label.value,
            'size': size,
            'type': 'text/csv'  # TODO: Don't hard code
        })
    )
    if res_create.json().get('status') != 0:
        raise Exception(res_create.text)
    logger.info('Successfully created data source')

    did = json.loads(res_create.text)['message']['did']
    storage.upload(str(path_to_file),
                   f"{uid}/rawData/{did}",
                   id_token)
    logger.info('Successfully uploaded the data')

    res_profile = requests.post(
        f"{api_base_url}/v3/profile",
        data=json.dumps({
            'idToken': id_token,
            'pid': pid,
            'did': did
        })
    )
    if res_profile.json().get('status') != 0:
        raise Exception(res_create.text)
    logger.info('ForecastFlow profiler is starting')
    return did


def create_model(id_token: str,
                 name: str,
                 train_settings: Union[dict, 'TrainingSettings'],
                 train_pid: str, train_did: str,
                 test_pid: Optional[str]=None, test_did: Optional[str]=None,
                 test_frac: Optional[float]=None,
                 description: str=''
                 ):
    if isinstance(train_settings, TrainingSettings):
        train_settings = train_settings.to_dict()
    if not isinstance(train_settings, dict):
        raise TypeError('train_settings must be dict or TrainingSettings')

    data = {
            'idToken': id_token,
            'name': name,
            'trainData': {
                'pid': train_pid,
                'did': train_did
            },
            'trainSettings': train_settings,
    }
    if description is not None:
        data['desc'] = description

    if isinstance(test_frac, float):
        data['percentTest'] = int(100 * test_frac)
    elif test_pid is not None and test_did is not None:
        data['testData'] = {
            'pid': test_pid,
            'did': test_did
        }
    else:
        raise ValueError('Lack of information for test data')

    response = requests.post(
        f'{config.forecastflow["api_base_url"]}/v3/createmodel',
        data=json.dumps(data)
    )
    try:
        response_json = response.json()
        if response_json.get('status') != 0:
            raise Exception(
                f'status={response_json["status"]}, '
                f'message="{response_json["message"]}"'
            )
    except json.decoder.JSONDecodeError:
        raise Exception(response.text)
    return response_json['mid']


def create_prediction(id_token: str, name: str, description: str, pid: str, did: str, mid: str):
    api_base_url = config.forecastflow['api_base_url']
    res = requests.post(
        f"{api_base_url}/v3/createpredict",
        data=json.dumps({
            'idToken': id_token,
            'name': name,
            'desc': description,
            'did': did,
            'mid': mid,
            'pid': pid
        })
    )
    if res.json().get('status') != 0:
        raise Exception(res.text)
    return json.loads(res.text)['rid']
