class Post(object):

    def __init__(self, id, platform, timestamp, title, age_restricted, clickbait_score, shitstorm_score, ad_score):

        self.id = id
        self.platform = platform
        self.timestamp = timestamp
        self.title = title
        self.age_restricted = age_restricted
        self.clickbait_score = clickbait_score
        self.shitstorm_score = shitstorm_score
        self.ad_score = ad_score

        self.artist = None
        self.channel = None

    def __repr__(self):

        return f"<nindo.api.Post '{self.id}'>"