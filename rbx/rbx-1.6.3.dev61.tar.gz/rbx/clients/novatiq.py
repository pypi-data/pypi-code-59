import json
import logging
from os import getenv, path
import shelve

import arrow

from . import Client, ClientException, HttpAuth

logger = logging.getLogger('rbx.clients.novatiq')


class NovatiqClient(Client):
    """Client for Novatiq CreatOR API.

    The API documentation can be found on the Platform wiki:
    https://github.com/rockabox/rbx/wiki/Novatiq

    """
    AUTH_PATH = 'auth'
    CATEGORIES = {
        'Family & Parenting': 'Family',
        'Food & Drink': 'Food and Drink',
        'Law, Government & Politics': 'Law & Govt',
        'News': 'Lifestyle',
        'Style & Fashion': 'Fashion',
        'Religion & Spirituality': 'Lifestyle',
        'Uncategorized': 'Lifestyle',
        'Non-Standard Content': 'Lifestyle',
        'Illegal Content': 'Adult Content',
    }
    ENDPOINT = 'https://cpdemo.awsdev.smartpipesolutions.com/api/v1/'
    LIVE_ENDPOINT = 'https://access.cp.novatiq.com/api/v1/'
    TIME_FORMAT = 'YYYY-MM-DD'
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

    def create_campaign(self, brand, category, country_code, name, segments, start_date, end_date):
        """Create a campaign.

        If the campaign name already exists, we fetch that campaign to return the existing campaign
        ID. Technically this should never happen, except possibly in a development setting.
        """
        try:
            response = self.request('post', 'campaigns', data=[{
                'name': name,
                'clientName': brand,
                'countryIso': country_code,
                'campaignCategory': self.CATEGORIES.get(category, category),
                'startDate': arrow.get(start_date).format(self.TIME_FORMAT),
                'endDate': arrow.get(end_date).format(self.TIME_FORMAT),
                'segments': segments,
            }])
            return response[0]['id']
        except ClientException as e:
            error = json.loads(str(e))
            if error['errorInfo']['errorCode'] == '1200002':
                # Code '1200002' means 'Given name already exists'
                return self.get_campaign(name=name)
            else:
                raise

    def get_campaign(self, name):
        """Retrieve the campaign ID given its name."""
        response = self.request('get', 'campaigns')
        try:
            return [campaign['id'] for campaign in response if campaign['name'] == name][0]
        except IndexError:
            return None

    def get_message(self, response):
        """Extract the message from the requests response object."""
        return self.get_response(response).get('errorInfo', {}).get('errorMessage')

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
        response = self.request('get', 'segments')

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
