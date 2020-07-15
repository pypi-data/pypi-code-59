from pathlib import Path
from os.path import join
import os


HOME = str(Path.home())

PATH_OF_GIT = 'Devs/ayuda-docs'
PATH_OF_GIT_REPO = join(HOME, join(PATH_OF_GIT,'.git'))

NAME_DOCS = join(PATH_OF_GIT,'ayuda')

PATH_DOCS=join(HOME,NAME_DOCS)


CONFIG_PATH = join(HOME, '.ayudarc.yml')