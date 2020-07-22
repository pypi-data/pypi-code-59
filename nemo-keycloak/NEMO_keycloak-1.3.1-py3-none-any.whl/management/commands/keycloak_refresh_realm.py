from __future__ import unicode_literals

import logging

from django.core.management.base import BaseCommand

from NEMO_keycloak.models import Realm

import NEMO_keycloak.services.realm

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for realm in Realm.objects.all():
            realm.well_known_oidc = NEMO_keycloak.services.realm.refresh_well_known_oidc(realm=realm)
            realm.certs = NEMO_keycloak.services.realm.refresh_certs(realm=realm)
            realm.save(update_fields=["_certs", "_well_known_oidc"])
            logger.debug("Refreshed: {}".format(realm))
