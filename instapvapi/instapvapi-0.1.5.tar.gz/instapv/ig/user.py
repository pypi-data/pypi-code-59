import json
from instapv.response.user_response import UserResponse
from instapv.response.friendship import FriendShipResponse
from instapv.response.self_user_feed import SelfUserFeedResponse
from instapv.response.following import UserFollowingResponse
from instapv.response.followers import UserFollowersResponse
from instapv.response.user_info_by_name import UserInfoByNameResponse

class User:

    def __init__(self, ig):
        self.ig = ig

    def get_user_feed(self, user_id: str, max_id: str = None, timestamp: str = None):
        data = {
            'max_id': max_id,
            'min_timestamp': timestamp,
            'rank_token': self.ig.tools.generate_uuid(True),
            'ranked_token': 'true'
        }

        query = self.ig.request(f'feed/user/{user_id}/', params=data)
        return UserResponse(query)

    def get_self_user_feed(self, max_id: str = None, timestamp: str = None):
        data = {
            'max_id': max_id,
            'min_timestamp': timestamp,
            'rank_token': self.ig.tools.generate_uuid(True),
            'ranked_token': 'true'
        }

        query = self.ig.request(f'feed/user/{self.ig._uid}/', params=data)
        return SelfUserFeedResponse(query)

    def get_info_by_name(self, username):
        query = self.ig.request(f'users/{username}/usernameinfo/')
        return UserInfoByNameResponse(**query['user'], status=query['status'])

    def follow_request_approve(self, user_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'user_id': user_id,
            '_csrftoken': self.ig._csrftoken
        }
        query = self.ig.request(f'friendships/approve/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def follow_request_ignore(self, user_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'user_id': user_id,
            '_csrftoken': self.ig._csrftoken
        }
        query = self.ig.request(f'friendships/ignore/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def follow(self, user_id, media_id=None):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'user_id': user_id,
            'radio_type': 'wifi-none',
            'device_id': self.ig.device_id
        }
        if media_id:
            data.update({'media_id_attribution': media_id})
        query = self.ig.request(f'friendships/create/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def unfollow(self, user_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'user_id': user_id,
            '_csrftoken': self.ig._csrftoken
        }
        query = self.ig.request(f'friendships/destroy/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def block(self, user_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'user_id': user_id,
            '_csrftoken': self.ig._csrftoken
        }
        query = self.ig.request(f'friendships/block/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def unblock(self, user_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'user_id': user_id,
            '_csrftoken': self.ig._csrftoken
        }
        query = self.ig.request(f'friendships/unblock/{user_id}/', params=data, signed_post=True)
        return FriendShipResponse(query)

    def get_user_followers(self, user_id, max_id: str = None):
        if max_id == None:
            query = self.ig.request(f'friendships/{user_id}/followers/?rank_token={self.ig.tools.generate_uuid(True)}')
        else:
            query = self.ig.request(f'friendships/{user_id}/followers/?rank_token={self.ig.tools.generate_uuid(True)}&max_id={max_id}')
        return UserFollowersResponse(**query)

    def get_pending_follow_requests(self):
        query = self.ig.request('friendships/pending?')
        return UserResponse(query)

    def get_user_following(self, user_id, max_id: str = None):
        if max_id == None:
            query = self.ig.request(f'friendships/{user_id}/following/?rank_token=' + self.ig.tools.generate_uuid(True))
        else:        
            query = self.ig.request(f'friendships/{user_id}/following/?rank_token={self.ig.tools.generate_uuid(True)}&max_id={max_id}')
        return UserFollowingResponse(query)
