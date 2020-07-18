import logging
import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from pytodd import settings
from pytodd.download import Download, DEFAULT_CHUNK_SIZE


class GDrive:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/drive']
        self.credentials_path = os.path.join(settings.root_dir, 'config', 'credentials.json')
        self.token_path = os.path.join(settings.root_dir, 'tokens', 'token.pickle')

        self.service = None

    def setup(self):

        credentials = None

        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                credentials = pickle.load(token)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)
                credentials = flow.run_local_server(port=0)

            os.makedirs(os.path.dirname(self.token_path), exist_ok=True)
            with open(self.token_path, 'wb') as token:
                pickle.dump(credentials, token)

        self.service = build('drive', 'v3', credentials=credentials)

    def get_file(self, file_id):
        try:
            return self.service.files().get(fileId=file_id, fields='id, name, size, mimeType').execute()
        except Exception as exp:
            logging.exception(exp)
            logging.info(f'Please ensure that file {file_id} exists and is accessible.')

        return None

    def download(self, file_id, bytes_io=None, start_byte_pos=None, last_byte_pos=None, chunk_size=DEFAULT_CHUNK_SIZE):

        file = self.get_file(file_id)
        if file is None:
            logging.error('File not found, abort.')

        size = int(file['size'])

        if start_byte_pos is None:
            start_byte_pos = 0
        elif start_byte_pos > size - 1:
            start_byte_pos = size - 1

        if last_byte_pos is None:
            last_byte_pos = size - 1
        elif last_byte_pos > size - 1:
            last_byte_pos = size - 1

        request = self.service.files().get_media(fileId=file_id)
        downloader = Download(bytes_io, request, start_byte_pos, last_byte_pos, chunk_size=chunk_size)

        if bytes_io is not None:
            done = False
            while done is False:
                content, done = downloader.next_chunk()
        else:
            return downloader
