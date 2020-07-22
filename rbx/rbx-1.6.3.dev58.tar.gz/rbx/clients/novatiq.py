import logging
import os

from . import Client, HttpAuth

logger = logging.getLogger('rbx.clients.novatiq')


class NovatiqClient(Client):
    """Client for Novatiq CreatOR API.

    The API documentation can be found on the Platform wiki:
    https://github.com/rockabox/rbx/wiki/Novatiq

    """
    AUTH_PATH = 'auth'
    ENDPOINT = 'https://cpdemo.awsdev.smartpipesolutions.com/api/v1/'
    LIVE_ENDPOINT = 'https://access.cp.novatiq.com/api/v1/'
    TOKEN = 'accessToken'

    def __new__(cls, *args, **kwargs):
        if os.getenv('RBX_ENVIRONMENT', 'dev') == 'live':
            cls.ENDPOINT = cls.LIVE_ENDPOINT

        return object.__new__(cls)

    @property
    def auth(self):
        """Novatiq uses Digest Authentication."""
        return HttpAuth(self.token, key='Authorization')

    def list_segments(self):
        """List all segments available.

        According to the documentation, there is no pagination on this endpoint, so we expect the
        full list to be returned with a single call.

        See: https://cpdemo.awsdev.smartpipesolutions.com/api/docs/index.html#/segment/getSegments
        """
        path = 'segments'
        response = self.request('get', path)

        return [{
            'id': segment['id'],
            'name': segment['name'],
            'country': segment['countryIso'],
            'expression': segment['expression'],
            'segmentPrice': segment['segmentPrice'],
            'creationDate': segment['creationDate'],
            'size': segment['size'],
            'sevenDayValue': segment['sevenDayValue'],
            'thirtyDayValue': segment['thirtyDayValue'],
        } for segment in response]
