class Channel(object):

    def __init__(self, id, avatar, last_post_id):

        self.id = id
        self.avatar = avatar
        self.last_post_id = last_post_id

    def __repr__(self):

        return f"<nindo.api.Channel '{self.id}'>"