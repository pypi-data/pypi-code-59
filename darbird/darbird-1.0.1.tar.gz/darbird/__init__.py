from . SMS import SMSService
from . Voice import VoiceService
from . MMS import MmsService
from . Authy import AuthyService


SMS = None
Voice = None
MMS = None
Authy = None


def initialize(username, api_key):

    if username is None or api_key is None:
        raise RuntimeError('Invalid username and/or api_key')

    globals()['SMS'] = SMSService(username, api_key)
    globals()['Voice'] = VoiceService(username, api_key)
    globals()['MMS'] = MmsService(username, api_key)
    globals()['Authy'] = AuthyService(username, api_key)
