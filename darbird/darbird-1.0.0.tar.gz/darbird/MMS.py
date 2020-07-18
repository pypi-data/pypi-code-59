from . Service import APIService, validate_phone


class MmsService(APIService):
    def __init__(self, username, api_key):
        super(MmsService, self).__init__(username, api_key)

    def _init_service(self):
        super(MmsService, self)._init_service()
        self._baseUrl = self._baseUrl

    def send(self, message, recipients, media_url, sender_id=None, unicodes=False, callback=None):


        url = '/sms/api'
        data = {
            'action' : 'send-sms',
            'to': recipients,
            'sms': message,
            'mms':'1',
            'media_url': media_url,
        }

        if sender_id is not None:
            data['from'] = sender_id

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)