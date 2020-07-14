import json
from instapv.response.media_info import MediaInfoResponse
from instapv.response.send_comment import SendCommentInfoResponse
from instapv.response.generic import GenericResponse
from instapv.response.comments import MediaCommentsResponse
from requests_toolbelt import MultipartEncoder
from time import time
import json as _json

# Fix Python3 Import Error.
try:
    from ImageUtils import getImageSize
except:
    from instapv.utils.ImageUtils import getImageSize


class Media:

    def __init__(self, ig):
        self.ig = ig

    def info(self, media_id: str):
        query = self.ig.request(f'media/{media_id}/info/?')
        return MediaInfoResponse(query)

    def likers(self, media_id: str):
        query = self.ig.request(f'media/{media_id}/likers/?')
        return query

    def comment(self, media_id, comment_text, reply_comment_id = None, module = 'comments_v2', carousel_index = 0, feed_position = 0, feed_bumped = False):
        data = {
            'user_breadcrumb': comment_text,
            'idempotence_token': self.ig.tools.generate_uuid(True),
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'comment_text': comment_text,
            'container_module': module,
            'radio_type': 'wifi-none',
            'device_id': self.ig.device_id,
            'carousel_index': carousel_index,
            'feed_position': feed_position,
            'is_carousel_bumped_post': feed_bumped
        }
        if reply_comment_id != None:
            data.update({
                'replied_to_comment_id': reply_comment_id
            })
        
        query = self.ig.request(f'media/{media_id}/comment/', params=data, signed_post=False)
        return SendCommentInfoResponse(query)

    def get_comment_infos(self, media_ids):
        if isinstance(media_ids, list):
            media_ids = ','.join(media_ids)
        data = {
            'media_ids': media_ids
        }
        query = self.ig.request(f'media/comment_infos', get_params=data)
        return query

    def delete_comment(self, media_id, comment_id):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            
        }
        query = self.ig.request(f'media/{media_id}/comment/{comment_id}/delete/', params=data, signed_post=False)
        return query

    def enable_comments(self, media_id):
        data = {
            '_csrftoken': self.ig._csrftoken,
            '_uuid': self.ig._uuid,
        }
        query = self.ig.request(
            f'media/{media_id}/enable_comments/', params=data, signed_post=False)
        return query

    def disable_comments(self, media_id):
        data = {
            '_csrftoken': self.ig._csrftoken,
            '_uuid': self.ig._uuid,
        }
        query = self.ig.request(
            f'media/{media_id}/disable_comments/', params=data, signed_post=False)
        return query

    def edit(self, media_id: str, caption_text):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'caption_text': caption_text
        }
        query = self.ig.request(f'media/{media_id}_{self.ig._uid}/edit_media/', params=data)
        return query

    def delete(self, media_id: str, media_type: str = 'PHOTO'):
        data = {
            'media_type': media_type,
            'igtv_feed_preview': False,
            '_csrftoken': self.ig._csrftoken,
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            'media_id': media_id
        }
        return self.ig.request(f'media/{media_id}/delete/', params=data)

    def like(self, media_id: str):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'media_id': media_id
        }
        query = self.ig.request(f'media/{media_id}/like/', params=data)
        return GenericResponse(query)

    def unlike(self, media_id: str):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'media_id': media_id
        }
        query = self.ig.request(f'media/{media_id}/unlike/', params=data)
        return GenericResponse(query)

    def save(self, media_id: str):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'media_id': media_id
        }
        query = self.ig.request(f'media/{media_id}/save/', params=data)
        return GenericResponse(query)

    def unsave(self, media_id: str):
        data = {
            '_uuid': self.ig._uuid,
            '_uid': self.ig._uid,
            '_csrftoken': self.ig._csrftoken,
            'media_id': media_id
        }
        query = self.ig.request(f'media/{media_id}/unsave/', params=data)
        return GenericResponse(query)

    def get_comments(self, media_id, max_id = None, min_id = None):
        data = {
            'can_support_threading': True,
        }
        if max_id:
            data['max_id'] = max_id
        if min_id:
            data['min_id'] = min_id
        query = self.ig.request(f'media/{media_id}/comments/', params=data)
        return MediaCommentsResponse(query)

    def get_comment_replais(self, media_id, comment_id):
        if not isinstance(comment_id, int):
            raise ValueError('comment_id must be integers.')
        query = self.ig.request(
            f'media/{media_id}/comments/{comment_id}/inline_child_comments/')
        return query


    def upload_photo(self, photo, caption=None, upload_id=None, is_sidecar=None):
        if upload_id is None:
            upload_id = self.ig.tools.generate_upload_id()
        data = {
            'upload_id': upload_id,
            '_uuid': self.ig._uuid,
            '_csrftoken': self.ig._csrftoken,
            'image_compression': '{"lib_name":"jt","lib_version":"1.3.0","quality":"87"}',
            'xsharing_user_ids': _json.dumps([]),
            'retry_context': json.dumps({
                'num_step_auto_retry': 0,
                'num_reupload': 0,
                'num_step_manual_retry': 0,
            }   ),
            'media_type': '1',
            'photo': ('pending_media_%s.jpg' % upload_id, open(photo, 'rb'))
        }
        print(data)
        if is_sidecar:
            data['is_sidecar'] = '1'
        encoder = MultipartEncoder(
            fields=data,
            boundary=self.ig._uuid
        )
        self.ig.req.headers.update({
            'X-IG-Capabilities': '3Q4=',
            'X-IG-Connection-Type': 'WIFI',
            'Cookie2': '$Version=1',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate',
            'Content-type': encoder.content_type,
            'Connection': 'close',
            'User-Agent': self.ig.device.build_user_agent()
        })
        response = self.ig.request(
            "upload/photo/", params=encoder.to_string(), signed_post=False)
        if self.ig.last_response.status_code == 200:
            print(response)
            if self.ig.configure(upload_id, photo, caption):
                self.ig.expose()
        return response


    def configure(self, upload_id, photo, caption=''):
        (w, h) = getImageSize(photo)
        data = json.dumps({
            '_csrftoken': self.ig._csrftoken,
            'media_folder': 'Instagram',
            'source_type': 4,
            '_uid': self.ig._uid,
            '_uuid': self.ig._uuid,
            'caption': caption,
            'upload_id': upload_id,
            'device': self.ig.device.generate_device(),
            'edits': {
                'crop_original_size': [w * 1.0, h * 1.0],
                'crop_center': [0.0, 0.0],
                'crop_zoom': 1.0
            },
            'extra': {
                'source_width': w,
                'source_height': h
            }
        })
        return self.ig.request('media/configure/?', params=data)

    def code_to_media_id(self, short_code: str):
        media_id = 0
        for i in short_code:
            media_id = (media_id*64) + self.ig.config.ALPHABET.index(i)
        return media_id

    def media_id_to_code(self, media_id: int):
        short_code = ''
        while media_id > 0:
            remainder = media_id % 64
            media_id = (media_id-remainder)/64
            short_code = self.ig.config.ALPHABET[remainder] + short_code
        return short_code
