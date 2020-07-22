from youtubesearchpython import SearchVideos
import youtube_dl
import json
import urllib.request
from urllib.request import Request
import os
from threading import *


class YoutubeHandler:

    def AudioUrl(self, videoId):
        import youtube_dl
        ydl_opts = {
            'format': 'bestaudio',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                f"https://www.youtube.com/watch?v={videoId}", download=False)
            return info['formats'][0]['url']

    def SearchYoutube(self, keyword, offset, mode, maxResults):
        search = SearchVideos(keyword, offset, mode, maxResults)
        return search.result()

    def SaveTrackAssets(self, trackInfo, trackDir):

        trackJson = {}
        trackJson["track_number"] = trackInfo.pop("track_number")
        trackJson["track_name"] = trackInfo.pop("track_name")
        trackJson["track_artists"] = trackInfo.pop("track_artists")
        trackJson["track_duration"] = trackInfo.pop("track_duration")
        trackJson["track_id"] = trackInfo.pop("track_id")

        if os.path.exists(os.path.join(trackDir, "albumAssets.json")):
            assetsFile = open(os.path.join(trackDir, "albumAssets.json"), "r")
            albumAssets = json.loads(assetsFile.read())
            albumAssets["tracks"] += [trackJson]
            assetsFile.close()

            assetsFile = open(os.path.join(trackDir, "albumAssets.json"), "w")
            assetsFile.write(json.dumps(albumAssets, indent=4))
            assetsFile.flush()
            assetsFile.close()

        else:
            assetsFile = open(os.path.join(trackDir, "albumAssets.json"), "w")
            trackInfo["tracks"] = [trackJson]
            assetsFile.write(json.dumps(trackInfo, indent=4))
            assetsFile.flush()
            assetsFile.close()
            
            albumArtRequest = Request(
                url = trackInfo["album_art_640"],
                data = None
            )
            albumArt = urllib.request.urlopen(albumArtRequest).read()
            albumArtFile = open(os.path.join(trackDir, "albumArt.png"), "wb")
            albumArtFile.write(albumArt)
            albumArtFile.flush()
            albumArtFile.close()

    def SaveTrackMain(self, trackInfo, trackDir, trackNumber):
        artists = ""
        for artist in trackInfo["album_artists"]:
            artists+=artist+" "
        videoId = self.SearchYoutube(trackInfo["track_name"] + " " + artists + " " + trackInfo["album_name"], 1, "dict", 1)["search_result"][0]["id"]
        audioUrl = self.AudioUrl(videoId)

        trackRequest = Request(
            url = audioUrl,
            data = None
        )
        track = urllib.request.urlopen(trackRequest).read()
        trackFile = open(os.path.join(trackDir, str(trackNumber) + ".m4a"), "wb")
        trackFile.write(track)
        trackFile.flush()
        trackFile.close()

        self.downloaded = True

    def SaveTrack(self, trackId):
        if not self.downloaded:
            return ("A track is already being downloaded.")
        else:

            self.downloaded = False

            trackInfo = json.loads(self.TrackInfo(trackId))
            trackDir = os.path.join(self.applicationDir, trackInfo["album_id"])
            
            if os.path.exists(trackDir):
                pass
            else:
                os.mkdir(trackDir)
            
            downloadThread = Thread(target=self.SaveTrackMain, args=(trackInfo, trackDir, trackInfo["track_number"], ))
            assetsThread = Thread(target=self.SaveTrackAssets, args=(trackInfo, trackDir, ))
            downloadThread.start()
            assetsThread.start()
            
            return "Downloading..."

    def SaveTrackStatus(self):
        return str(self.downloaded)

    def TrackDownload(self, trackId, trackName):
        if trackName == None:
            trackInfo = json.loads(self.TrackInfo(trackId))
        
            artists = ""
            for artist in trackInfo["album_artists"]:
                artists+=artist+" "

            videoId = self.SearchYoutube(trackInfo["track_name"] + " " + artists + " " + trackInfo["album_name"], 1, "dict", 1)["search_result"][0]["id"]
            audioUrl = self.AudioUrl(videoId)
            
            return json.dumps({"download_url": audioUrl}, indent=4)
        
        elif trackId == None:
            trackId = json.loads(self.SearchSpotify(trackName, "track", 0, 1))["tracks"][0]["track_id"]
            trackInfo = json.loads(self.TrackInfo(trackId))
            artists = ""
            for artist in trackInfo["album_artists"]:
                artists+=artist+" "

            videoId = self.SearchYoutube(trackInfo["track_name"] + " " + artists + " " + trackInfo["album_name"], 1, "dict", 1)["search_result"][0]["id"]
            audioUrl = self.AudioUrl(videoId)
            
            return json.dumps({"download_url": audioUrl}, indent=4)