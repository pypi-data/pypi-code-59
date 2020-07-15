import os
import hashlib
import logging
from pathlib import Path

from .exception import ZhongkuiParseError, ZhongkuiInvalidFile
from .utils import calculateEntropy
from .parse import exiftool
from .corpus import EXIFTOOL

log = logging.getLogger(__name__)

FILE_CHUNK_SIZE = 16 * 1024


class File(object):
    """zhongkui basic file class"""
    def __init__(self, fpath, chunk_size=FILE_CHUNK_SIZE):
        """
        Args:
            fpath: os.pathLike.
            chuck_size: default is 16 * 1024

        Raise:
            ZhongkuiInvalidFile
        """
        self.fpath = fpath
        self.chunk_size = chunk_size

        # check valid
        if not self.isValidFile():
            raise ZhongkuiInvalidFile(f'{fpath} is not a valid file')

        # for cache property
        self._file_data = None
        self._md5 = None
        self._sha256 = None
        self._sha1 = None
        self._is_probably_packed = None

        # for cache info
        self._basic = None
        try:
            self._exiftool = exiftool(fpath)
        except ZhongkuiParseError:
            raise ZhongkuiInvalidFile(f'{fpath} is not a valid file')

    def isValidFile(self):
        return (Path(self.fpath).exists() and Path(self.fpath).is_file()
                and os.path.getsize(self.fpath) != 0)

    def genChunk(self):
        """Read file contents in chunks (generator)."""

        with open(self.fpath, "rb") as fd:
            while True:
                chunk = fd.read(self.chunk_size)
                if not chunk:
                    break
                yield chunk

    def getChunkEntropy(self):
        entropy = []
        for data in self.genChunk():
            entropy.append(calculateEntropy(data))

        return entropy

    def _calHash(self):
        """Calculate all possible hashes for this file."""
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        for chunk in self.genChunk():
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

        self._md5 = md5.hexdigest()
        self._sha1 = sha1.hexdigest()
        self._sha256 = sha256.hexdigest()

    @property
    def fileName(self):
        return Path(self.fpath).name

    @property
    def fileType(self):
        file_type = self._exiftool.get(EXIFTOOL.FILETYPE)
        if file_type is not None:
            file_type = file_type.replace(' ', '').lower()

        return file_type

    @property
    def fileData(self):
        if self._file_data is None:
            with open(self.fpath, "rb") as f:
                self._file_data = f.read()
        return self._file_data

    @property
    def md5(self):
        if self._md5 is None:
            self._calHash()
        return self._md5

    @property
    def sha1(self):
        if self._sha1 is None:
            self._calHash()
        return self._sha1

    @property
    def sha256(self):
        if self._sha256 is None:
            self._calHash()
        return self._sha256

    @property
    def isProbablyPacked(self) -> bool:
        """A file is probably packed:
        1. entropy of at least 20% data > 7.4.
        """
        if self._is_probably_packed is not None:
            return self._is_probably_packed

        total_file_data = len(self.fileData)
        total_compressed_data = 0

        for data in self.genChunk():
            ck_entropy = calculateEntropy(data)
            ck_length = len(data)
            if ck_entropy > 7.4:
                total_compressed_data += ck_length
        if ((1.0 * total_compressed_data) / total_file_data) > 0.2:
            self._is_probably_packed = True
        else:
            self._is_probably_packed = False

        return self._is_probably_packed

    def fileSize(self, easy_read=True):
        if easy_read:
            return self._exiftool.get(EXIFTOOL.FILESIZE)
        else:
            return os.path.getsize(self.fpath)

    def basicInfo(self):
        """file basic info"""
        if self._basic is None:
            self._basic = {
                'name': self.fileName,
                'md5': self.md5,
                'sha1': self.sha1,
                'sha256': self.sha256,
                'fileType': self.fileType,
                'fileSize': self.fileSize(easy_read=False),
                'isProbablyPacked': self.isProbablyPacked
            }

        return self._basic
