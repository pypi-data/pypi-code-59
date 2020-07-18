from . Service import APIService, validate_phone


class AuthyService(APIService):
    def __init__(self, username, api_key):
        super(AuthyService, self).__init__(username, api_key)

    def _init_service(self):
        super(AuthyService, self)._init_service()
        self._baseUrl = self._baseUrl

    def send(self, recipients, token_lenght, msg_type, sender_id=None, unicodes=False, callback=None):


        url = '/auth/autity'
        data = {
            'to_number' : recipients,
            'token_lenght': token_lenght,
            'msg_type': msg_type,
        }

        if sender_id is not None:
            data['from'] = sender_id

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)



    def authverify(self, recipients, code, sender_id=None, unicodes=False, callback=None):

        url = '/auth/confirm-token'
        data = {
            'to_number' : recipients,
            'auth_code': code,
        }

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)