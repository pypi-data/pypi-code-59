from . import *

import os
import hashlib

from base64 import b64encode
from functools import partial

def getModel(file):
    return file + '.bob'

def getCollideModel(file):
    return file + '.cob'

def getTexture(file):
    return file + '.texture'

def getSound(file):
    return file + '.ogg'

class Material(LoopBack): pass

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def genPayloadInfo():
    files = []
    for root, subdirs, files_in_dir in os.walk(".", topdown=True, followlinks=False):
        for file in files_in_dir:
            if file.startswith('.') or file == 'payload_info': continue
            files.append(os.path.join(root, file))

    payloadStr = "{}\n1\n".format(len(files))
    for file in files:
        payloadStr += "{} {}\n".format(file.strip("./"), md5sum(file))

    with open('payload_info', 'w') as f:
        f.write(payloadStr)
        f.close()

def makeTree(path=''):
    tree = {}
    for p in os.listdir(path):
        if os.path.isdir(os.path.join(path, p)):
            for name, path in makeTree(os.path.join(path, p)):
                tree[name] = path
        else:
            tree[p] = os.path.join(path, p)
    return tree

def encodeFile(source):
    ff = open('coded-'+source,'wb')
    ff.write('import base64;exec(base64.b64decode('+repr(b64encode(open(source).read()))+'))')
    ff.flush()
