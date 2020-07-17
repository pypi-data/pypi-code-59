import django
from django.conf import settings

from qary import constants

settings.configure(**constants.django_settings_dict)
django.setup()
