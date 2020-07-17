# import os
from pathlib import Path

from django.db import models
from django.conf import settings  # noqa

from qary.constants import LARGE_FILES
from qary.etl import netutils

# settings.configure()


class Title(models.Model):
    """ Document title for composing Wikipedia and other web searches

    >>> created, obj = Title.objects.get_or_create(text='this is a test, this is only a test')
    >>> created
    True
    """
    text = models.TextField(default='', null=True, help_text='Article title string')


def load_csv(path=LARGE_FILES['wikipedia_titles']['path']):
    """ Load the wikipidia titles CSV into the Title database table

    >>> load_csv().endswith('enwiki-latest-all-titles-in-ns0.gz')
    True
    """
    path = Path(path)
    if not path.is_file():
        path = netutils.download_if_necessary(path.name)
    return path
