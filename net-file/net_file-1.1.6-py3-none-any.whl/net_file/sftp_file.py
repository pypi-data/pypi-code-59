from typing import Dict
from typing import Tuple
from urllib.parse import urlparse

import paramiko

from net_file.common import FileUnavailableError
from net_file.common import InvalidFileRangeError
from net_file.common import InvalidFileRequestError
from net_file.common import NetFile


class SFTPFile(NetFile):
    def __init__(
            self,
            url: str,
            start_bytes: int = None,
            length: int = None,
            host_auth: Dict[str, Tuple[str, str]] = None,
    ):
        super().__init__()
        if start_bytes is not None and start_bytes < 0:
            raise InvalidFileRangeError()
        if length is not None and length < 0:
            raise InvalidFileRangeError()

        self._url = url
        self._start_bytes = start_bytes or 0
        self._length = length
        self._remaining_bytes = 0
        self._host_auth = host_auth
        self._sftp = None
        self._ssh_client = None
        self._sftp_file = None

    def open(self) -> None:
        if self._sftp_file is not None:
            return

        o = urlparse(self._url)
        host_name = o.hostname.strip(':')
        creds = self._host_auth[host_name]

        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(host_name, username=creds[0], password=creds[1])
        self._sftp = self._ssh_client.open_sftp()
        self._sftp_file = self._sftp.open(o.path)

        file_size = self._sftp_file.stat().st_size
        self._remaining_bytes = file_size
        if self._start_bytes or self._length:
            length = (self._length or file_size) - self._start_bytes
            self._remaining_bytes = self._length
            if self._start_bytes + length > file_size:
                raise InvalidFileRangeError(f'Invalid file length/start offset specified ({self._length}/{self._start_bytes}). File length: {file_size}')

        self._sftp_file.prefetch()

        if self._start_bytes:
            self._sftp_file.seek(self._start_bytes)

    def close(self) -> None:
        if self._sftp:
            self._sftp.close()
        if self._ssh_client:
            self._ssh_client.close()

    def read(self, chunk_bytes: int = None) -> bytes:
        if not self._sftp_file:
            raise InvalidFileRequestError('File is closed')

        content = b''
        if self._remaining_bytes:
            try:
                if chunk_bytes is not None:
                    content = self._sftp_file.read(min(self._remaining_bytes, chunk_bytes))
                else:
                    content = self._sftp_file.read(self._remaining_bytes)
            except IOError as exc:
                raise FileUnavailableError(f'File become unavailable ({exc})')

        self._remaining_bytes -= len(content)
        return content


def supported_schemas() -> Tuple[str, ...]:
    return 'ssh',


def open_sftp_url(
        url: str,
        start_bytes: int = None,
        length: int = None,
        host_auth: Dict[str, Tuple[str, str]] = None,
) -> NetFile:
    return SFTPFile(url=url, start_bytes=start_bytes, length=length, host_auth=host_auth)
