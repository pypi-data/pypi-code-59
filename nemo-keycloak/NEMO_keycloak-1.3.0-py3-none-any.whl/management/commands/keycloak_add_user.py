from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model

from NEMO_keycloak.models import Realm

logger = logging.getLogger(__name__)


def realm(name):
    try:
        return Realm.objects.get(name=name)
    except Realm.DoesNotExist:
        raise TypeError("Realm does not exist")


def user(username):
    UserModel = get_user_model()
    try:
        return UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        raise TypeError("User does not exist")
