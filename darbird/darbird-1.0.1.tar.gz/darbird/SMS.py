from . Service import APIService, validate_phone


class SMSService(APIService):
    def __init__(self, username, api_key):
        super(SMSService, self).__init__(username, api_key)

    def _init_service(self):
        super(SMSService, self)._init_service()
        self._baseUrl = self._baseUrl

    def send(self, message, recipients, sender_id=None, unicodes=False, callback=None):


        url = '/sms/api'
        data = {
            'action' : 'send-sms',
            'to': recipients,
            'sms': message,
        }

        if sender_id is not None:
            data['from'] = sender_id

        if unicodes:
            data['unicode'] = '1'

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)


    def sendschedule(self, message, recipients, schedule, sender_id=None, unicodes=False, callback=None):


        url = '/sms/api'
        data = {
            'action' : 'send-sms',
            'to': recipients,
            'sms': message,
            'schedule': schedule,
        }

        if sender_id is not None:
            data['from'] = sender_id

        if unicodes:
            data['unicode'] = '1'

        return self._make_request(url, 'POST', headers=self._headers, params=None, data=data, callback=callback)