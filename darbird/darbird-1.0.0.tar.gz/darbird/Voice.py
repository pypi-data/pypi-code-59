from . Service import APIService, validate_phone


class VoiceService(APIService):
    def __init__(self, username, api_key):
        super(VoiceService, self).__init__(username, api_key)

    def _init_service(self):
        super(VoiceService, self)._init_service()
        self._baseUrl = self._baseUrl

    def send(self, message, recipients, sender_id=None, unicodes=False, callback=None):


        url = '/sms/api'
        data = {
            'action' : 'send-sms',
            'to': recipients,
            'sms': message,
            'voice':'1'
        }

        if sender_id is not None:
            data['from'] = sender_id

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)