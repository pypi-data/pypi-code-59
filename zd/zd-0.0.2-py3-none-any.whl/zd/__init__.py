#!/usr/bin/env python

from zstandard import ZstdCompressor as compressor
from zstandard import ZstdDecompressor as decompressor
from io import TextIOWrapper

_open = open


class Write:
  def __init__(self, file, encoding):
    self.encoding = encoding
    self.file = _open(file, "wb")
    self.ctx = compressor(level=12).stream_writer(
      self.file
    )

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.close()

  def write(self, text):
    encoding = self.encoding
    if encoding:
      if isinstance(text, str):
        text = text.encode(encoding)
    self.ctx.write(text)

  def close(self):
    self.ctx.close()
    self.file.close()


class Read:
  def __init__(self, file, encoding):
    self.encoding = encoding
    self.file = _open(file, "rb")
    self.ctx = decompressor().stream_reader(
      self.file
    )

  def __iter__(self):
    return TextIOWrapper(
      self.ctx,
      encoding=self.encoding
    )

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.ctx.close()
    self.file.close()


def open(file, mode='r', encoding="utf-8"):
  if "w" in mode:
    return Write(file, encoding)
  return Read(file, encoding)
