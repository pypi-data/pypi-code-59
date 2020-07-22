from __future__ import unicode_literals

import logging

from django.core.management.base import BaseCommand

from NEMO_keycloak.models import Client

import NEMO_keycloak.services.uma

logger = logging.getLogger(__name__)


def client(client_id):
    try:
        return Client.objects.get(client_id=client_id)
    except Client.DoesNotExist:
        raise TypeError("Client does not exist")


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--client", type=client, required=False)

    def handle(self, *args, **options):
        client = options.get("client")

        if client:
            NEMO_keycloak.services.uma.synchronize_client(client=client)
        else:
            for client in Client.objects.all():
                NEMO_keycloak.services.uma.synchronize_client(client=client)
