# encoding: utf-8

import os
import time
import logging
import requests
import subprocess

from threading import Timer

from urllib.parse import urlparse


# COMMON OPTION
PROCESS_TIMEOUT = 7200
REQUEST_INTERVAL = 1
REQUEST_TIMEOUT = 10
HEADERS = {}


# DISABLE REQUESTS OPTION
requests.packages.urllib3.disable_warnings()
requests.models.DEFAULT_REDIRECT_LIMIT = 5


def check_alive(url, timeout=REQUEST_TIMEOUT):
    resp = http_get(url, timeout=timeout, redirect=False)
    return False if resp.status_code is None else True


def format_target(url):
    pattern = urlparse(url)
    port = pattern.port
    scheme= pattern.scheme
    host = pattern.hostname
    if not port:
        if scheme.lower() == 'http':
            port = 80
        elif scheme.lower() == 'https':
            port = 443
        elif scheme.lower() == 'ftp':
            port = 21
        else:
            port = 00
    target_fmt = '{scheme}://{host}:{port}'
    return target_fmt.format(scheme=scheme, host=host, port=port)



def http_get(url, params={}, timeout=REQUEST_TIMEOUT, headers=HEADERS, redirect=True, cookies={}, retry=True, stream=False):
    counter = 3
    response = requests.models.Response()
    while counter:
        try:
            return requests.get(
                url=url, params=params, headers=headers, timeout=timeout,
                allow_redirects=redirect, cookies=cookies, verify=False, stream=stream)
        except (requests.ConnectTimeout, requests.ReadTimeout):
            counter -= 1
            logging.warning('ConnectTimeout: {0}'.format(url))
            if not retry:
                return response
            time.sleep(REQUEST_INTERVAL)
        except requests.ConnectionError:
            logging.warning('ConnectionError: {0}'.format(url))
            return response
        except Exception as err:
            counter -= 1
            logging.warning(err)
            if not retry:
                return response
    return response


def http_post(url, data, timeout=REQUEST_TIMEOUT, headers=HEADERS, redirect=True, cookies={}, retry=True):
    counter = 3
    response = requests.models.Response()
    while counter:
        try:
            return requests.post(
                url=url, data=data, headers=headers, timeout=timeout,
                allow_redirects=redirect, cookies=cookies, verify=False)
        except (requests.ConnectTimeout, requests.ReadTimeout) as err:
            counter -= 1
            logging.warning('ConnectTimeout: {0}, Message: {1}'.format(url, err))
            if not retry:
                return response
            time.sleep(REQUEST_INTERVAL)
        except requests.ConnectionError as err:
            logging.error('ConnectionError: {0}, Message: {1}'.format(url, err))
            return response
        except Exception as err:
            counter -= 1
            logging.error(err.message)
            if not retry:
                return response
    return response


def http_head(url, timeout=REQUEST_TIMEOUT, headers=HEADERS, redirect=True, cookies={}, retry=True):
    counter = 3
    response = requests.models.Response()
    while counter:
        try:
            return requests.head(
                url=url, headers=headers, timeout=timeout,
                allow_redirects=redirect, cookies=cookies, verify=False)
        except (requests.ConnectTimeout, requests.ReadTimeout) as err:
            counter -= 1
            logging.warning('ConnectTimeout: {0}, Message: {1}'.format(url, err))
            if not retry:
                return response
            time.sleep(REQUEST_INTERVAL)
        except requests.ConnectionError as err:
            logging.error('ConnectionError: {0}, Message: {1}'.format(url, err))
            return response
        except Exception as err:
            counter -= 1
            logging.error(err.message)
            if not retry:
                return response
    return response


def cmdprocess(cmdline, timeout=PROCESS_TIMEOUT, shell=True, cwd=None):
    logging.debug("cmdprocess call -> {cmdline}".format(cmdline=cmdline))
    pipe = subprocess.Popen(cmdline,
                            shell=shell,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            cwd=cwd,
                            env=os.environ)
    
    timer = Timer(timeout, lambda proc: proc.kill(), [pipe])
    try:
        timer.start()
        output, stderr = pipe.communicate()
        return_code = pipe.returncode
        stderr = stderr.decode(errors='replace')
        output = output.decode(errors='replace')
        return output, stderr, return_code
    finally:
        timer.cancel()