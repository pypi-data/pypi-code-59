from . import *

import os
import shutil

appearances = {}

class Appearance(Database):
    def __init__(salf, name):
        Database.__init__(self)
        if not name in appearances:
            appearances[name] = self
        else:
            raise Exception(repr(name) + 'already exists.')

def getOutput(file):
    string = ''
    for a in appearances:
        string += 'addCharacter(' + repr(a) + ', cfg=' +str(appearances[a].dict) + ')\n'
    
    with open(file, 'w') as f:
        f.write(string)
        f.flush()

def getMedia(path='', divide=False):
    tree = bs.makeTree(path)
    for name, obj in appearances.items():
        media = os.path.join(path, 'media')
        if not os.path.isdir(media):
            os.mkdir(media)
        if divide:
            media = os.path.join(media, name)
            if not os.path.isdir(media):
              os.mkdir(media)
        tex = os.path.join(media, 'textures')
        texAndroid = os.path.join(tex, 'android')
        texOther = os.path.join(tex, 'other')
        models = os.path.join(media, 'models')
        audios = os.path.join(media, 'audios')
        if not os.path.isdir(tex):
            os.mkdir(tex)
        if not os.path.isdir(texAndroid):
            os.mkdir(texAndroid)
        if not os.path.isdir(texOther):
            os.mkdir(texOther)
        if not os.path.isdir(models):
            os.mkdir(models)
        if not os.path.isdir(audios):
            os.mkdir(audios)

        for key, value in obj.dict.items():
            if type(value) == str:
                medias = [value]
            elif type(value) == list:
                medias = value
            else:
                continue
            for fileName in medias:
                audioFile = fileName + '.ogg'
                bobFile = fileName + '.bob'
                cobFile = fileName + '.cob'
                texAndroidFile = fileName + '.ktx'
                texOtherFile = fileName + '.dds'

                if texAndroidFile in tree:
                        shutil.copy(tree[texAndroidFile], texAndroid)
                if texOtherFile in tree:
                        shutil.copy(tree[texOtherFile], texOther)
                for modelFile in [bobFile, cobFile]:
                    if modelFile in tree:
                        shutil.copy(tree[modelFile], models)
                if audioFile in tree:
                        shutil.copy(tree[audioFile], audios)
