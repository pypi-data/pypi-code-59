#!/usr/bin/env python3

from fire import Fire
import zs
import re

RE_SIGN = re.compile(r"\s/")


@Fire
def main(filepath):
  for line in zs.open(filepath):
    line = line.rstrip("\n")
    line = line.replace("（", "(")
    line = line.split("(", 1)[0].lower()
    if RE_SIGN.sub(line, "").isalnum():
      continue
    if len(line) == 1:
      continue
    print(line)


if __name__ == "__main__":
  import single_process.init
  # main()
  pass
