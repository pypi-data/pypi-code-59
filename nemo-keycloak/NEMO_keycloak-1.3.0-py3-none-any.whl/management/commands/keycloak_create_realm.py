import logging

from django.core.management import BaseCommand

from NEMO_keycloak.models import Server, Realm, Client

import NEMO_keycloak.services.realm


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create a new Realm and Server"

    def add_arguments(self, parser):
        parser.add_argument("realm", type=str, help="the keycloak REALM name")
        parser.add_argument("server_url", type=str, help="the Keycloak server URL")
        parser.add_argument("server_internal_url", type=str, help="they Keycloak internal server URL (optional)")
        parser.add_argument("client_id", type=str, help="the Keycloak client id")
        parser.add_argument("client_secret", type=str, help="the Keycloak client secret")

    def handle(self, *args, **options):
        server = None
        realm = None
        client = None
        try:
            server = Server(url=options["server_url"], internal_url=options.get("server_internal_url", None))
            server.save()
            realm = Realm(server=server, name=options["realm"])
            realm.save()
            client = Client(realm=realm, client_id=options["client_id"], secret=options["client_secret"])
            client.save()
        except Exception as e:
            if server and server.id:
                server.delete()
            if realm and realm.id:
                realm.delete()
            if client and client.id:
                client.delete()
            logger.exception(str(e))
            self.stderr.write(self.style.ERROR("Error creating Realm"))
        try:
            if realm:
                realm.well_known_oidc = NEMO_keycloak.services.realm.refresh_well_known_oidc(realm=realm)
                realm.certs = NEMO_keycloak.services.realm.refresh_certs(realm=realm)
                realm.save(update_fields=["_well_known_oidc", "_certs"])
                self.stdout.write(self.style.SUCCESS('Successfully updated oidc and certs for Realm "%s"' % realm.name))
        except Exception as e:
            logger.exception(str(e))
            self.stderr.write(self.style.WARNING("Error updating oidc and certs for Realm"))
        self.stdout.write(self.style.SUCCESS('Successfully created Realm "%s"' % realm.name))
