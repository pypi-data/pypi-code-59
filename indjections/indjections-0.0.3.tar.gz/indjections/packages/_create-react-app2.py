import subprocess
import re
import os
from importlib import import_module
import sys
from django.core.management.base import BaseCommand
from indjections.core import indject_string, parse_toml
# from .indject import execute_installation_file
from indjections.management.commands.indject import execute_installation_file


class Command(BaseCommand):
    help = 'Installs create react app and configures it appropriately'

    def handle(self, *args, **kwargs):
        # print('Installing create-react-app...')
        # rebuild with autoreload hook

        settings = sys.modules[os.environ['DJANGO_SETTINGS_MODULE']]
        urls = sys.modules[settings.ROOT_URLCONF]

        execute_installation_file('create-react-app', settings, urls,
                                  package_path='indjections.commands')
