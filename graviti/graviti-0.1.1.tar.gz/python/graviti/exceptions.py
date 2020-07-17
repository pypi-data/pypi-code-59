#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines some exceptions about data center."""

from requests import RequestException
from requests.models import Response

from .log import dump_request_and_response


class GASException(Exception):
    """This is the parent class to the following specified error classes.
    """


class GASRequestError(GASException):
    """Through this class which inherits from GASException,
    we can raise GASRequestError specifically.

    :param error: RequestException message
    """

    def __init__(self, error: RequestException) -> None:
        super().__init__()
        self._error = error

    def __str__(self) -> str:
        return str(self._error)


class GASResponseException(GASException):
    """Through this class which inherits from GASException,
    we can raise GASResponseException specifically.
    This is the parent class to response-related errors.

    :param response: The response of the request
    """

    def __init__(self, response: Response) -> None:
        super().__init__()
        self._response = response
        self.status_code = response.status_code

    def __str__(self) -> str:
        return dump_request_and_response(self._response)


class GASResponseError(GASResponseException):
    """Through this class which inherits from GASError,
    we can raise GASResponseError specifically.

    :param response: The response of the request
    """


class GASOSSError(GASResponseException):
    """Exception for OSS response error

    :param response: The response of the request
    """

    def __init__(self, response: Response) -> None:
        super().__init__(response)
        response_json = response.json()
        self.status = response_json["status"]


class GASDataCenterError(GASResponseException):
    """Exception for graviti datacenter response error

    :param response: The response of the request
    """

    def __init__(self, response: Response) -> None:
        super().__init__(response)
        response_json = response.json()
        self.code = response_json["code"]
        self.message = response_json["message"]
        self.success = response_json["success"]


class GASParameterError(GASException):
    """Through this class which inherits from KeyError,
    we can raise GASParameterError specifically.

    :param message: The message of the error
    """

    def __init__(self, message: str) -> None:
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        return self._message


class GASDataSetError(GASException):
    """Through this class which inherits from RuntimeError,
    we can raise GASDataSetError specifically.

    :param data_set_name: The name of the missing data_set
    """

    def __init__(self, data_set_name: str) -> None:
        super().__init__()
        self._data_set_name = data_set_name

    def __str__(self) -> str:
        return f"Data set '{self._data_set_name}' does not exist"


class GASDataSetTypeError(GASException):
    """Through this class which inherits from GASException,
    we can raise GASDataSetTypeError specifically.

    :param data_set_name: The name of the data set whose requested type is wrong
    :param request_type: the requested type
    """

    def __init__(self, data_set_name: str, request_type: str) -> None:
        super().__init__()
        self._data_set_name = data_set_name
        self._request_type = request_type

    def __str__(self) -> str:
        return f"Data set '{self._data_set_name}' is not {self._request_type}"
