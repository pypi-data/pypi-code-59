
import json
import pytest
import random
import os
from pytest_cases import fixture_plus

def get_params_from_file(param):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"params_captured.json")) as fobj:
        params = json.load(fobj)
    for api, params_info in params.items():
        if param in params_info:
            values = params[api][param]
            if None in values:
                values.remove(None)
            #return random.choice(values)
            return values


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("lastUpdateTime"))
def lastUpdateTime(request):
    return request.param
    # return get_params_from_file("lastUpdateTime")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("channels"))
def channels(request):
    return request.param
    # return get_params_from_file("channels")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("updateTemplate"))
def updateTemplate(request):
    return request.param
    # return get_params_from_file("updateTemplate")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("maxStartTime"))
def maxStartTime(request):
    return request.param
    # return get_params_from_file("maxStartTime")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("minEndTime"))
def minEndTime(request):
    return request.param
    # return get_params_from_file("minEndTime")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("stationIds"))
def stationIds(request):
    return request.param
    # return get_params_from_file("stationIds")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("contentId"))
def contentId(request):
    return request.param
    # return get_params_from_file("contentId")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("startTime"))
def startTime(request):
    return request.param
    # return get_params_from_file("startTime")


# @pytest.fixture(scope="session", autouse=True)
@fixture_plus(params=get_params_from_file("stationId"))
def stationId(request):
    return request.param
    # return get_params_from_file("stationId")


