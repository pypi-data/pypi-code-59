class Milestone(object):

    def __init__(self, currentSubs, expected_time, surpassed, channel, artist):

        self.current_subs = currentSubs
        self.expected_time = expected_time
        self.surpassed = surpassed

        self.channel = channel
        self.artist = artist

    def __repr__(self):
        return f"<nindo.api.Milestone '{self.current_subs}'>"