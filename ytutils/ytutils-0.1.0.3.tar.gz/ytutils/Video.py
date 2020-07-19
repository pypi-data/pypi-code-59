import requests
import urllib.parse
import re

class Video:
    
    def __init__(self, api_key):
        self.__pattern__ = r"^(?:http(?:s)?:\/\/)?(?:www\.)?(?:m\.)?(?:youtu\.be\/|youtube\.com\/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed)\/))([^\?&\"'>]+)"
        self.api_key = api_key
        self.__dictChart = {}
        
        
    def set_key(self, api_key):
        self.api_key= api_key
        
    def start(self, video_url=None, video_id=None):
        if video_url is None and video_id is None:
            raise SyntaxError('There must be given video_url or video_id')
        elif video_url is None:
            self.video_id = video_id
        else:
            id_pattern = re.search(self.__pattern__, video_url)
            if id_pattern is None:
                raise KeyError('Invalid Video Url')
            self.video_id = id_pattern[1]
            
        self.__URL ='https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id='+self.video_id+'&key='+self.api_key
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
                self.__dictChart['channelId'] = self.__json['items'][0]['snippet']['channelId']
                self.__dictChart['publishedAt'] = self.__json['items'][0]['snippet']['publishedAt']
                self.__dictChart['channelTitle'] = self.__json['items'][0]['snippet']['channelTitle']
                self.__dictChart['viewCount'] = self.__json['items'][0]['statistics']['viewCount']
                self.__dictChart['commentCount'] = self.__json['items'][0]['statistics']['commentCount']
                self.__dictChart['likeCount'] = self.__json['items'][0]['statistics']['likeCount']
                self.__dictChart['dislikeCount'] = self.__json['items'][0]['statistics']['dislikeCount']
                    

            else:
                self.__dictChart['result'] = 'FAILURE'
                self.__dictChart['code'] = 0
                self.__dictChart['message'] = 'Please check your video id'
                self.__dictChart['reason'] = 'emptyResult'
                self.__dictChart['extended_help'] = ''
                    
                
        else:
            self.__dictChart['result'] = 'FAILURE'
            self.__dictChart['code'] = int(self.__json['error']['code'])
            self.__dictChart['message'] = self.__json['error']['message']
            self.__dictChart['reason'] = self.__json['error']['errors'][0]['reason']
            self.__dictChart['extended_help'] = 'Use this link to know the meaning of the error code:- https://developers.google.com/youtube/v3/docs/videos/list?hl=en-US#errors_1'
            
    def result(self):
        return self.__dictChart
        
        