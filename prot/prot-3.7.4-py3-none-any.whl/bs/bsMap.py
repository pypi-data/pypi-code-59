from . import *

import os
import shutil

maps = {}
depends = []

class Map(object):
    name = "Map"

    @classmethod
    def getPreviewTextureName(cls):
        """
        Return the name of the preview texture for this map.
        """
        return None

    @classmethod
    def onPreload(cls):
        """
        Called when the map is being preloaded;
        it should load any media it requires to
        class attributes on itself.
        """
        return None

def registerMap(map):
    if not map.name in maps:
        maps[map.name] = map
    else:
        raise Exception(repr(map.name) + 'already exists.')

def _import(*args, **kwargs):
    depends.append(args[0])

def record():
    import builtins
    builtins.__import = builtins.__import__
    builtins.__import__ = _import

def end():
    import builtins
    builtins.__import__ = builtins.__import
    del builtins.__import

def getMedia(path='.', divide=False):
    tree = bs.makeTree(path)
    for name, obj in maps.items():
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
        scripts = os.path.join(media, 'scripts')
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
        if not os.path.isdir(scripts):
            os.mkdir(scripts)

        medias = []
        if obj.getPreviewTextureName() is not None:
            medias.append(bs.getTexture(obj.getPreviewTextureName()))
        if obj.onPreload() is not None:
            for key, value in obj.onPreload().items():
                if type(value) == str:
                    medias.append(value)
                elif type(value) in [list, tuple]:
                    medias += list(value)
        for depend in depends:
            medias.append(depend + '.py')
        for fileName in medias:
            if fileName.endswith('.texture') and fileName.split('.')[0] + '.ktx' in tree:
                    shutil.copy(tree[fileName.split('.')[0] + '.ktx'], texAndroid)
            if fileName.endswith('.texture') and fileName.split('.')[0] + '.dds' in tree:
                    shutil.copy(tree[fileName.split('.')[0] + '.dds'], texOther)
            for format in ['.bob', '.cob']:
                if fileName.endswith(format) and fileName.split('.')[0] + format in tree:
                    shutil.copy(tree[fileName.split('.')[0] + format], models)
            if fileName.endswith('.ogg') and fileName in tree:
                    shutil.copy(tree[fileName], audios)
            if fileName.endswith('.py') and fileName in tree:
                    shutil.copy(tree[fileName], scripts)