__all__ = ['ZaleyCashClient']

import requests
import logging

from zaleycash.exceptions import (
    ZaleyCashBadResponse, ZaleyCashNetworkError, ZaleyCashBadRequest, ZaleyCashAuthError,
    ZaleyCashUnauthorizedAccessError, ZaleyCashNotFound, ZaleyCashServerError, ZaleyCashUnknownError)


class ZaleyCashClient:
    _base_url = 'https://zaleycash.com/api/v2/'

    def __init__(self, secret_key, token=None):
        self.secret_key = secret_key
        self.token = token
        self.logger = logging.getLogger('zaleycash')

    def _make_request(self, path, method='GET', params=None, json=None, secret_key=None):
        if secret_key is not None:
            token = secret_key
        else:
            if self.token is None:
                self.logger.debug('Trying to get auth token...')
                self.get_token()
                self.logger.debug('Token is accepted.')
            token = self.token

        headers = {'Authorization': 'Bearer ' + token}
        url = self._build_url(path)
        self.logger.debug('make request: method={} path={} params={} json={} headers={}'.format(
            method,
            url,
            params,
            json,
            headers
        ))

        try:
            response = requests.request(method, url, params=params, json=json, headers=headers, timeout=30)
        except requests.RequestException as e:
            raise ZaleyCashNetworkError(e)

        if response.status_code != 200:
            self.logger.info('request method={} path={} params={} json={} headers={} failed {}: {}'.format(
                method,
                url,
                params,
                json,
                headers,
                response.status_code,
                response.content
            ))
        else:
            self.logger.debug('request method={} path={} params={} json={} headers={} success {}: {}'.format(
                method,
                url,
                params,
                json,
                headers,
                response.status_code,
                response.content
            ))

        try:
            jsn = response.json()
        except (ValueError, TypeError):
            raise ZaleyCashBadResponse('No json in response', 500)

        message = jsn.get('message')
        code = jsn.get('code')
        if not message and 'detail' in jsn:
            message = jsn.get('detail')
        if not code:
            code = response.status_code

        if response.status_code == 400:
            raise ZaleyCashBadRequest(message, code)
        elif response.status_code == 401:
            raise ZaleyCashAuthError(message, code)
        elif response.status_code == 403:
            raise ZaleyCashUnauthorizedAccessError(message, code)
        elif response.status_code == 404:
            raise ZaleyCashNotFound(message, code)
        elif response.status_code == 500:
            raise ZaleyCashServerError(message, code)
        elif response.status_code != 200:
            raise ZaleyCashUnknownError(message, code)

        return jsn['response']

    def _build_url(self, path):
        return self._base_url + path

    def get_token(self):
        data = self._make_request('token', method='POST', secret_key=self.secret_key)
        self.token = data['access_token']

    def get_services(self):
        data = self._make_request('services')
        return data

    def get_user(self, email=None):
        params = dict(email=email) if email is not None else {}
        data = self._make_request('user', params=params)
        return data

    def register_user(self, name, email, password):
        json = {
            'name': name,
            'email': email,
            'plainPassword': password,
        }
        data = self._make_request('user', method='POST', json=json)
        return data

    def get_balance(self):
        data = self._make_request('user/balance')
        return data

    def make_referral(self, user_id):
        data = self._make_request('user/children', method='POST', json=dict(user=user_id))
        return data

    def transfer_money_to_referral(self, user_id, currency, amount, operation_id):
        json = {
            'user_id': user_id,
            'currency': currency,
            'amount': amount,
            'operation_id': str(operation_id),
        }
        data = self._make_request('money/transfer/internal', method='POST', json=json)
        return data

    def get_currencies(self):
        data = self._make_request('money/currencies', method='GET')
        return data
