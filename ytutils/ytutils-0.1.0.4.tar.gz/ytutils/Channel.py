import requests
import urllib.parse
import re

class Channel:
    
    def __init__(self, api_key):
        self.__pattern__ = r"^(?:http(?:s)?:\/\/)?(?:www\.)?(?:m\.)?(?:youtu\.be\/|youtube\.com\/channel\/)([^\?&\"'>]+)"
        self.api_key = api_key
        self.__dictChart = {}
    
    def set_key(self, api_key):
        self.api_key= api_key
    
    def start(self, channel_url=None, channel_id=None):
        if channel_url is None and channel_id is None:
            raise SyntaxError('There must be given channel_url or channel_id')
        elif channel_url is None:
            self.channel_id = channel_id
        else:
            id_pattern = re.search(self.__pattern__, channel_url)
            if id_pattern is None:
                raise KeyError('Invalid Channel Url')
            self.channel_id = id_pattern[1]
            
        self.__URL ='https://www.googleapis.com/youtube/v3/channels?part=brandingSettings,statistics,snippet&id='+self.channel_id+'&key='+self.api_key
        try:
            self.__response = requests.get(self.__URL)
        except:
            raise ConnectionError('Network connection failed')
            
        self.__json = self.__response.json()
        if 'error' not in self.__json:
            if int(self.__json['pageInfo']['totalResults']) > 0:
                self.__dictChart['result'] = 'OK'
                self.__dictChart['code'] = 200
                self.__dictChart['message'] = ''
                self.__dictChart['reason'] = ''
                self.__dictChart['extended_help'] = ''
                self.__dictChart['title'] = self.__json['items'][0]['snippet']['title']
                self.__dictChart['des'] = self.__json['items'][0]['snippet']['description']
                self.__dictChart['thumbnails'] = self.__json['items'][0]['snippet']['thumbnails']
                self.__dictChart['channelArt'] = self.__json['items'][0]['brandingSettings']['image']
                self.__dictChart['subHidden'] = False
                if self.__json['items'][0]['statistics']['hiddenSubscriberCount']:
                    self.__dictChart['subHidden'] = True
                self.__dictChart['publishedAt'] = self.__json['items'][0]['snippet']['publishedAt']
                self.__dictChart['subs'] = int(self.__json['items'][0]['statistics']['subscriberCount'])
                self.__dictChart['videos'] = int(self.__json['items'][0]['statistics']['videoCount'])
                if 'country' in self.__json['items'][0]['snippet']:
                    self.__dictChart['country'] = self.__json['items'][0]['snippet']['country']                  

            else:
                self.__dictChart['result'] = 'FAILURE'
                self.__dictChart['code'] = 0
                self.__dictChart['message'] = 'Please check your channel id'
                self.__dictChart['reason'] = 'emptyResult'
                self.__dictChart['extended_help'] = ''
                    
                
        else:
            self.__dictChart['result'] = 'FAILURE'
            self.__dictChart['code'] = int(self.__json['error']['code'])
            self.__dictChart['message'] = self.__json['error']['message']
            self.__dictChart['reason'] = self.__json['error']['errors'][0]['reason']
            self.__dictChart['extended_help'] = 'Use this link to know the meaning of the error code:- https://developers.google.com/youtube/v3/docs/channels/list?hl=en-US#errors_1'
            
    def result(self):
        return self.__dictChart