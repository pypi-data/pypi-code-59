import logging
from os import getenv, path
import shelve

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

    def __init__(self, destination='/tmp'):
        super().__init__()
        if getenv('RBX_ENVIRONMENT', 'dev') == 'live':
            self.ENDPOINT = self.LIVE_ENDPOINT

        self.shelf = path.join(destination, 'novatiq.segments')

    @property
    def auth(self):
        """Novatiq uses Digest Authentication."""
        return HttpAuth(self.token, key='Authorization')

    def get_segments(self, country_code=None):
        """Get segments from local cache."""
        with shelve.open(self.shelf) as shelf:
            try:
                segments = shelf['segments']
            except KeyError:
                # The cache is empty
                segments = []

        segment_list = []
        for segment in segments:
            if country_code and country_code not in [segment['country'], 'ZZ']:
                continue
            segment_list.append(segment)

        return segment_list

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

    def store_segments(self):
        """Retrieve the list of segments, and then cache the results on a shelf.

        As no caching mechanism exists on the API, we simply override the content of the cache
        with the results from the list_segments() call.
        """
        segments = self.list_segments()
        with shelve.open(self.shelf) as shelf:
            shelf['segments'] = segments
