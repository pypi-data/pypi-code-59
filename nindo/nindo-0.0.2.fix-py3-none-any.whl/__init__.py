import requests

from .channel import Channel
from .artist import Artist
from .post import Post
from .viral import Viral
from .charts import Chart

from .coupon import Coupon
from .brand import Brand
from .milestone import Milestone

from .types import TYPES

class NindoApi(object):

    def getVirals(self):

        api_response = requests.request("GET", "https://api.nindo.de/viral")

        response = []
        for post in api_response.json():

            newPost = Post(post["postID"], post["platform"], post["timestamp"], post["_post"]["title"], post["_post"]["FSK18"], post["_post"]["clickbait"], post["_post"]["shitstorm"], post["_post"]["ad"])
            newChannel = Channel(post["_post"]["_channel"]["channelID"], post["_post"]["_channel"]["avatar"], post["_post"]["_channel"]["lastPostID"])
            newArtist = Artist(post["_post"]["_channel"]["_artist"]["name"], post["_post"]["_channel"]["_artist"]["_id"])
            newViral = Viral(post["postID"], post["platform"], post["timestamp"], post["type"], post["value"])

            response.append({"post": newPost, "channel": newChannel, "artist": newArtist, "viral": newViral})

        return response

    def getCharts(self, type):

        if type == TYPES.Charts.INSTAGRAM or type == TYPES.Charts.TIKTOK or type == TYPES.Charts.TWITCH or type == TYPES.Charts.YOUTUBE or type == TYPES.Charts.TWITTER:

            api_response = requests.request("GET", f"https://api.nindo.de/ranks/charts/{type}")
            response = []

            for chart in api_response.json():

                newArtist = Artist(chart["_artist"]["name"], chart["artistID"])
                myChart = Chart(chart["id"], chart["rank"], newArtist, chart["value"], type)
                response.append(myChart)

            return response

    def getCoupons(self):

        api_response = requests.request("GET", f"https://api.nindo.de/coupons")
        response = []

        for currCoupon in api_response.json()["coupons"]:

            newArtist = Artist(currCoupon["_artist"]["name"], currCoupon["_artist"]["id"])
            newBrand = Brand(currCoupon["_brand"]["id"], currCoupon["_brand"]["name"], currCoupon["_brand"]["url"], currCoupon["_brand"]["branch"], currCoupon["_brand"]["color"])

            newCoupon = Coupon(currCoupon["id"], currCoupon["timestamp"], currCoupon["discount"], currCoupon["code"], currCoupon["valid"], currCoupon["validUntil"], currCoupon["url"], currCoupon["terms"], newArtist, newBrand)
            response.append(newCoupon)

        return response

    def getUpcomingMilestones(self):

        api_response = requests.request("GET", f"https://api.nindo.de/ranks/milestones")
        response = []

        for milestone in api_response.json():

            newChannel = Channel(milestone["_channel"]["id"], milestone["_channel"]["avatar"], None)
            newArtist = Artist(milestone["_channel"]["_artist"]["name"], milestone["_channel"]["artist_id"])
            newMilestone = Milestone(milestone["currentSubs"], milestone["expectedTime"], False, newChannel, newArtist)

            response.append(newMilestone)

        return response

    def getPastMilestones(self):

        api_response = requests.request("GET", f"https://api.nindo.de/ranks/pastMilestones")
        response = []

        for milestone in api_response.json():
            newChannel = Channel(milestone["_channel"]["id"], milestone["_channel"]["avatar"], None)
            newArtist = Artist(milestone["_channel"]["_artist"]["name"], milestone["_channel"]["artist_id"])
            newMilestone = Milestone(milestone["currentSubs"], milestone["expectedTime"],
                                     True, newChannel, newArtist)

            response.append(newMilestone)

        return response
