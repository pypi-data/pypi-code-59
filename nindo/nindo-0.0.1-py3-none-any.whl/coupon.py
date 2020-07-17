from .brand import Brand

class Coupon(object):

    def __init__(self, id, timestamp, discount, code, valid, validUntil, url, terms, artist, brand):

        self.id = id
        self.timestamp = timestamp
        self.discount = discount
        self.code = code
        self.valid = valid
        self.validUntil = validUntil
        self.url = url
        self.terms = terms

        self.artist = artist
        self.brand = brand

    def __repr__(self):

        return f"<nindo.api.Coupon '{self.id}'>"