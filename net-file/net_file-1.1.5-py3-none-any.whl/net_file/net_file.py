from typing import Dict
from typing import Tuple
from urllib.parse import urlparse

from net_file.common import NetFile
from net_file.local_file import supported_schemas as local_schemas
from net_file.local_file import open_local_file
from net_file.http_file import supported_schemas as http_schemas
from net_file.http_file import open_http_url
from net_file.sftp_file import supported_schemas as sftp_schemas
from net_file.sftp_file import open_sftp_url


_SCHEMA_HANDLERS = {
    local_schemas(): open_local_file,
    http_schemas(): open_http_url,
    sftp_schemas(): open_sftp_url,
}


def open_url(
        url: str,
        start_bytes: int = None,
        length: int = None,
        host_auth: Dict[str, Tuple[str, str]] = None,
) -> NetFile:
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme.lower()
    for schemas, handler in _SCHEMA_HANDLERS.items():
        if scheme in schemas:
            return handler(
                url=url,
                start_bytes=start_bytes,
                length=length,
                host_auth=host_auth,
            )
    raise ValueError(f'Unknown schema {parsed_url.scheme}')
