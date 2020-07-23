#!/usr/bin/env python
import sys
import getpass
import json
import builtins
from . import servicedefs
from infinstor_mlflow_plugin.tokenfile import read_token_file, write_token_file
from requests.exceptions import HTTPError
import requests
from os.path import expanduser
from os.path import sep as separator
import datetime

def get_creds():
    if sys.stdin.isatty():
        print("Enter your InfinStor service username and password")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
    else:
        username = sys.stdin.readline().rstrip()
        password = sys.stdin.readline().rstrip()
    return username, password

def login_and_update_token_file(username, password):
    postdata = dict()
    auth_parameters = dict()
    auth_parameters['USERNAME'] = username
    auth_parameters['PASSWORD'] = password
    postdata['AuthParameters'] = auth_parameters
    postdata['AuthFlow'] = "USER_PASSWORD_AUTH"
    postdata['ClientId'] = builtins.clientid

    payload = json.dumps(postdata)

    url = 'https://cognito-idp.us-east-1.amazonaws.com:443/'
    headers = {
            'Content-Type': 'application/x-amz-json-1.1',
            'X-Amz-Target' : 'AWSCognitoIdentityProviderService.InitiateAuth'
            }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise
    except Exception as err:
        print(f'Other error occurred: {err}')
        raise
    else:
        authres = response.json()['AuthenticationResult']
        token = authres['IdToken']
        refresh_token = authres['RefreshToken']
        token_time = round(datetime.datetime.timestamp(datetime.datetime.utcnow()))
        tokfile = expanduser("~") + separator + '.infinstor' + separator + '/token'
        write_token_file(tokfile, token_time, token, refresh_token, builtins.clientid,\
                builtins.service)
        return True

def main():
    username, password = get_creds()
    return login_and_update_token_file(username, password)

if __name__ == "__main__":
    if (main()):
        exit(0)
    else:
        exit(255)
