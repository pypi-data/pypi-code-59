import json

from instapv.exceptions import InternalException
from instapv.response.create_collection import createCollectionResponse
from instapv.response.generic import GenericResponse
from instapv.response.edit_collection import editCollectionResponse
from instapv.response.collection_feed import CollectionFeedResponse


"""
Functions related to creating and managing collections of your saved media.
WARRNING: To put media in a collection, you must first mark that media item as "saved".
"""
class Collection:

    def __init__(self, ig):
        self.ig = ig

    def get_list(self, max_id: str = None):
        """
        Get a list of all of your collections.
        :param = max_id
        """
        data = {
            'collection_types': '["ALL_MEDIA_AUTO_COLLECTION","MEDIA","PRODUCT_AUTO_COLLECTION"]',
        }
        if max_id:
            data['max_id'] = max_id
        query = self.ig.request('collections/list/', get_params=data)
        return query
    
    def get_feed(self, collection_id: str, max_id: str = None):
        if max_id:
            query = self.ig.request('collections/list/', get_params={'max_id': max_id})
        else:
            query = self.ig.request('collections/list/')
        return CollectionFeedResponse(query)
    
    def create(self, name: str, module_name: str = 'feed_saved_add_to_collection') -> createCollectionResponse:
        data = {
            'module_name': module_name,
            'added_media_ids': '[]',
            'collection_visibility': '0', # Instagram is planning for public collections soon
            '_csrftoken': self.ig._csrftoken,
            '_uid': self.ig._uid,
            'name': name,
            '_uuid': self.ig._uuid
        }
        query = self.ig.request('collections/create/', params=data)
        return createCollectionResponse(query)
    
    def delete(self, collection_id: str):
        data = {
            '_csrftoken': self.ig._csrftoken,
            '_uid': self.ig._uid,
            '_uuid': self.ig._uuid
        }
        query = self.ig.request(f'collections/{collection_id}/delete/', params=data)
        return GenericResponse(query)

    def edit(self, collection_id: str, params: dict):
        data = {
            '_csrftoken': self.ig._csrftoken,
            '_uid': self.ig._uid,
            '_uuid': self.ig._uuid
        }
        if 'name' in params and params['name'] != '':
            data['name'] = params['name']
        if 'cover_media_id' in params:
            data['cover_media_id'] = params['cover_media_id']
        if 'add_media' in params:
            if not isinstance(params['add_media'], list):
                raise ValueError('add_media must be instance of list.')
            data['added_media_ids'] = json.dumps(params['add_media'])
            if 'module_name' in params:
                data['module_name'] = params['module_name']
            else:
                data['module_name'] = 'feed_saved_add_to_collection'
        if len(params.keys()) < 1:
            raise ValueError('You must provide a name or at least one media ID.')

        query = self.ig.request(f'collections/{collection_id}/edit/', params=data)
        return editCollectionResponse(query)