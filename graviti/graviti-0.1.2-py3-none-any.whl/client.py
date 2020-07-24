#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file define class Client and function read_data_from_file.
"""

import logging
from typing import Any, Dict, Optional

import requests

from .exceptions import GASDataCenterError, GASOSSError, GASRequestError, GASResponseError
from .log import dump_request_and_response

logger = logging.getLogger(__name__)


def post(
    url: str,
    *,
    data: Optional[bytes] = None,
    json_data: Optional[Dict[str, Any]] = None,
    content_type: Optional[str] = None,
    access_key: Optional[str] = None,
) -> Any:
    """Send a POST requests

    :param url: URL for the request
    :param data: bytes data to send in the body of the request
    :param json_data: json data to send in the body of the request
    :param content_type: Content-Type to send in the header of the request
    :param token: X-Token to send in the header of the request
    :raises GASRequestError: When post request failed
    :raises GASResponseError: When response.ok is False
    :raises GASResult: When response content 'success' is False
    :return: response of the request
    """
    headers: Dict[str, str] = {}
    if access_key:
        headers["X-Token"] = access_key
    if content_type:
        headers["Content-Type"] = content_type

    try:
        response = requests.post(url, data=data, json=json_data, headers=headers)
    except requests.RequestException as error:
        raise GASRequestError(error)

    if not response.ok:
        raise GASResponseError(response)

    content_type = response.headers["Content-Type"]
    if not content_type.startswith("application/json"):
        logger.debug(dump_request_and_response(response))
        return response.content

    result = response.json()

    if response.headers.get("Server", None) == "AliyunOSS":
        if result["status"] != "OK":
            raise GASOSSError(response)
        logger.debug(dump_request_and_response(response))
        return result

    if not result["success"]:
        raise GASDataCenterError(response)

    logger.debug(dump_request_and_response(response))
    return result["data"]
