#!/usr/bin/env python3

def encode(s):
  return ''.join(map(_c, s))

def _c(c):
  x = ord(c)
  if  x == 45 or  x == 46  or  x == 95 or  x == 126 or \
     (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
    return c
  return "%{:02x}".format(x).upper()

def decode(s):
  i = 0
  l = len(s)
  t = ""
  while i < l:
    if s[i] == '%':
      t += chr(int(s[i+1:i+3].lower(), 16))
      i += 3
    else:
      t += s[i]
      i += 1
  return t
