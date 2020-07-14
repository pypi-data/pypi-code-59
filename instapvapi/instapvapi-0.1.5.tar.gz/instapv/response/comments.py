# from dataclasses import dataclass


# @dataclass
# class UserInfo:
#     pk: int
#     username: str
#     full_name: str
#     is_private: bool
#     profile_pic_url: str
#     profile_pic_id: str
#     is_verified: bool
#     is_mentionable: bool
#     latest_reel_media: int
#     latest_besties_reel_media: int


# @dataclass
# class CommentInfo(UserInfo):
#     pk: int
#     user_id: int
#     text: str
#     type: 0
#     created_at: int
#     created_at_utf: int
#     content_type: str
#     status: str
#     bit_flags: int
#     did_report_as_spam: bool
#     share_enabled: bool
#     child_comment_count: int
#     preview_child_comments: list
#     other_preview_users: list
#     inline_composer_display_condition: str


# @dataclass
# class MediaCommentsResponse(CommentInfo):
#     status: str

from instapv.utils.auto_mapper import AutoMapper
class MediaCommentsResponse(AutoMapper):

    def __init__(self, data: dict):
        self.response = self._auto_mapper(data)
        self.as_json = data