from instapv.response.user_response import UserResponse
from dataclasses import dataclass

@dataclass
class UserFollowersResponse:
    sections: list
    global_blacklist_sample: list
    users: UserResponse
    big_list: bool
    page_size: int
    status: str
    friend_requests: str = None
    next_max_id: str = None