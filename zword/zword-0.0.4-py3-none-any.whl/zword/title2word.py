#!/usr/bin/env python3

from fire import Fire
import zd
import re

RE_SIGN = re.compile(r"[\s/\.\-]")
RE_SPLIT = re.compile(r"：/")


# print(RE_SIGN.sub("", "debian gnu/kfreebsd"))
# raise
def iterword(filepath):
  for line in zd.open(filepath):
    line = line.rstrip("\n")
    line = line.replace("（", "(")
    line = line.split("(", 1)[0].lower()
    if RE_SIGN.sub("", line).isalnum():
      continue
    if len(line) == 1:
      continue
    for i in RE_SPLIT.split(line):
      yield i


@Fire
def main(filepath):
  for i in iterword(filepath):
    print(i)
