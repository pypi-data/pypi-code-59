from __future__ import absolute_import
import six

import time
import random
import logging

from googleapiclient.errors import HttpError
from googleapiclient.http import _retry_request

# 25 Mega-Bytes
DEFAULT_CHUNK_SIZE = 25 * 1024 * 1024


class Download:

    def __init__(self, fd, request, start_byte_pos, last_byte_pos, chunk_size=DEFAULT_CHUNK_SIZE):

        self._fd = fd
        self._request = request
        self._uri = request.uri
        self._chunk_size = chunk_size
        self._progress = 0
        self._total_size = None
        self._done = False

        self._headers = {}
        for k, v in six.iteritems(request.headers):
            if not k.lower() in ('accept', 'accept-encoding', 'user-agent'):
                self._headers[k] = v

        self._start_byte_pos = start_byte_pos
        self._last_byte_pos = last_byte_pos

        self._total_size = self._last_byte_pos - self._start_byte_pos + 1

    def next_chunk(self, num_retries=4):
        headers = self._headers.copy()

        chunk_start_byte_pos = min(self._start_byte_pos + self._progress, self._last_byte_pos)
        chunk_end_byte_pos = min(chunk_start_byte_pos + self._chunk_size - 1, self._last_byte_pos)

        logging.debug(f'Download request generated for range - {chunk_start_byte_pos}-{chunk_end_byte_pos}')

        headers['range'] = 'bytes=%d-%d' % (
            chunk_start_byte_pos,
            chunk_end_byte_pos,
        )

        http = self._request.http
        resp, content = _retry_request(
            http,
            num_retries,
            'media download',
            time.sleep,
            random.random,
            self._uri,
            'GET',
            headers=headers,
        )

        if resp.status in [200, 206]:
            if 'content-location' in resp and resp['content-location'] != self._uri:
                self._uri = resp['content-location']
            self._progress += len(content)

            if self._fd is not None:
                self._fd.write(content)

            if self._total_size is None or self._progress == self._total_size:
                self._done = True

            logging.info(f'Download progress: {(self._progress // self._total_size) * 100}%.')
            return content, self._done
        else:
            raise HttpError(resp, content, uri=self._uri)
