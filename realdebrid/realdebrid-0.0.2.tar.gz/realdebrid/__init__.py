import requests
import json

_api_token = ''
_url = 'https://api.real-debrid.com/rest/1.0'


class RealDebrid(object):
    def __init__(self, api_token):
        global _api_token
        _api_token = api_token

    @staticmethod
    def request_executor(method, uri, **args):
        headers = {"Authorization": f'Bearer {_api_token}'}
        # Merge incoming 'headers' arg if it exists
        args['headers'] = {**args.get('headers'), **headers} if args.get('headers') else headers
        return requests.request(method=method, url=f'{_url}{uri}', **args)

    def disable_access_token(self):
        result = RealDebrid.request_executor(method='GET', uri='/disable_access_token')
        success_code = 204
        return result.status_code == success_code

    def time(self, format=None):
        uri = '/time/iso' if format.upper() == 'ISO' else '/time'
        result = RealDebrid.request_executor(method='GET', uri=uri)
        return result.text

    def user(self):
        result = RealDebrid.request_executor(method='GET', uri='/user')
        return json.loads(result.text)

    @property
    def unrestrict(self):
        return Unrestrict()

    @property
    def traffic(self):
        return Traffic()

    @property
    def streaming(self):
        return Streaming()

    @property
    def downloads(self):
        return Downloads()

    @property
    def torrent(self):
        return Torrent()

    @property
    def hosts(self):
        return Hosts()

    @property
    def forum(self):
        return Forum()

    @property
    def settings(self):
        return Settings()


class Unrestrict(object):
    @staticmethod
    def check(link, password=None):
        result = RealDebrid.request_executor(method='POST', uri='/unrestrict/check',
                                             data={'link': link, 'password': password})
        return json.loads(result.text)

    @staticmethod
    def link(link, password=None, remote=None):
        result = RealDebrid.request_executor(method='POST', uri='/unrestrict/link',
                                             data={'link': link, 'password': password, 'remote': remote})
        return json.loads(result.text)

    @staticmethod
    def folder(link):
        result = RealDebrid.request_executor(method='POST', uri='/unrestrict/folder', data={'link': link})
        return json.loads(result.text)

    @staticmethod
    def container_file(container_path):
        result = RealDebrid.request_executor(method='PUT', uri='/unrestrict/containerFile',
                                             headers={'Content-Type': 'application/octet-stream'},
                                             data=open(container_path, 'rb').read())
        return json.loads(result.text)

    @staticmethod
    def container_link(link):
        result = RealDebrid.request_executor(method='POST', uri='/unrestrict/containerLink', data={'link': link})
        return json.loads(result.text)


class Traffic(object):
    @staticmethod
    def list():
        result = RealDebrid.request_executor(method='GET', uri='/traffic')
        return json.loads(result.text)

    @staticmethod
    def details(start=None, end=None):
        result = RealDebrid.request_executor(method='GET', uri='/traffic/details', data={'start': start, 'end': end})
        return json.loads(result.text)


class Streaming(object):
    @staticmethod
    def transcode(id):
        result = RealDebrid.request_executor(method='GET', uri=f'/streaming/transcode/{id}')
        return json.loads(result.text)

    @staticmethod
    def media_infos(id):
        result = RealDebrid.request_executor(method='GET', uri=f'/streaming/mediaInfos/{id}')
        return json.loads(result.text)


class Downloads(object):
    @staticmethod
    def list(offset=None, page=None, limit=None):
        result = RealDebrid.request_executor(method='GET', uri='/downloads',
                                             data={'offset': offset, 'page': page, 'limit': limit})
        return json.loads(result.text)

    @staticmethod
    def delete(id):
        result = RealDebrid.request_executor(method='DELETE', uri=f'/downloads/delete/{id}')
        success_code = 204
        return result.status_code == success_code


class Torrent(object):
    @staticmethod
    def list(offset=None, page=None, limit=None, filter=None):
        result = RealDebrid.request_executor(method='GET', uri='/torrents',
                                             data={'offset': offset, 'page': page, 'limit': limit, 'filter': filter})
        return json.loads(result.text)
    
    @staticmethod
    def info(id):
        result = RealDebrid.request_executor(method='GET', uri=f'/torrents/info/{id}')
        return json.loads(result.text)

    @staticmethod
    def instant_availability(sha1):
        if not isinstance(sha1, list):
            sha1 = [sha1]
        hashes = '/'.join(sha1)
        result = RealDebrid.request_executor(method='GET', uri=f'/torrents/instantAvailability/{hashes}')
        return json.loads(result.text)

    @staticmethod
    def active_count():
        result = RealDebrid.request_executor(method='GET', uri='/torrents/activeCount')
        return json.loads(result.text)

    @staticmethod
    def available_hosts():
        result = RealDebrid.request_executor(method='GET', uri='/torrents/availableHosts')
        return json.loads(result.text)

    @staticmethod
    def add_torrent(torrent_path):
        result = RealDebrid.request_executor(method='PUT', uri='/torrents/addTorrent',
                                             headers={'Content-Type': 'application/octet-stream'},
                                             data=open(torrent_path, 'rb').read())
        return json.loads(result.text)

    @staticmethod
    def add_magnet(magnet):
        result = RealDebrid.request_executor(method='POST', uri='/torrents/addMagnet', data={'magnet': magnet})
        return json.loads(result.text)

    @staticmethod
    def select_files(id, files='all'):
        result = RealDebrid.request_executor(method='POST', uri=f'/torrents/selectFiles/{id}', data={'files': files})
        success_code = 204
        return result.status_code == success_code

    @staticmethod
    def delete(id):
        result = RealDebrid.request_executor(method='DELETE', uri=f'/torrents/delete/{id}')
        return json.loads(result.text)


class Hosts(object):
    @staticmethod
    def list():
        result = RealDebrid.request_executor(method='GET', uri='/hosts')
        return json.loads(result.text)

    @staticmethod
    def status():
        result = RealDebrid.request_executor(method='GET', uri='/hosts/status')
        return json.loads(result.text)

    @staticmethod
    def regex():
        result = RealDebrid.request_executor(method='GET', uri='/hosts/regex')
        return json.loads(result.text)

    @staticmethod
    def domains():
        result = RealDebrid.request_executor(method='GET', uri='/hosts/domains')
        return json.loads(result.text)


class Forum(object):
    @staticmethod
    def list():
        result = RealDebrid.request_executor(method='GET', uri='/forum')
        return json.loads(result.text)

    @staticmethod
    def list_topics(id, offset=None, page=None, limit=None, meta=None):
        result = RealDebrid.request_executor(method='GET', uri=f'/forum/{id}',
                                             data={'offset': offset, 'page': page, 'limit': limit, 'meta': meta})
        return json.loads(result.text)


class Settings(object):
    @staticmethod
    def list():
        result = RealDebrid.request_executor(method='GET', uri='/settings')
        return json.loads(result.text)

    @staticmethod
    def update(setting_name, setting_value):
        valid_settings = ['download_port', 'locale', 'streaming_language_preference', 'streaming_quality',
                          'mobile_streaming_quality', 'streaming_cast_audio_preference']

        assert setting_name in valid_settings, \
            f'Not a valid setting: {setting_name}. Valid settings are: {valid_settings}'

        result = RealDebrid.request_executor(method='POST', uri='/settings/update', data={setting_name: setting_value})
        success_code = 204
        return result.status_code == success_code

    @staticmethod
    def convert_points():
        result = RealDebrid.request_executor(method='POST', uri='/settings/convertPoints')
        success_code = 204
        return result.status_code == success_code

    @staticmethod
    def change_password():
        result = RealDebrid.request_executor(method='POST', uri='/settings/changePassword')
        success_code = 204
        return result.status_code == success_code

    @staticmethod
    def avatar_file(image_path):
        result = RealDebrid.request_executor(method='PUT', uri='/settings/avatarFile',
                                             headers={'Content-Type': 'application/octet-stream'},
                                             data=open(image_path, 'rb').read())
        success_code = 204
        return result.status_code == success_code

    @staticmethod
    def avatar_delete():
        result = RealDebrid.request_executor(method='DELETE', uri='/settings/avatarDelete')
        success_code = 204
        return result.status_code == success_code
