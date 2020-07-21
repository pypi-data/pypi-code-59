#!/usr/bin/env python
# encoding=utf-8
import random

def RandomChar(num):
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    randomStr = ''
    for i in range(num):
      randomStr += string[random.randint(0, 25)]
    return randomStr
 

def version():
    print('version: 1.0.0')
