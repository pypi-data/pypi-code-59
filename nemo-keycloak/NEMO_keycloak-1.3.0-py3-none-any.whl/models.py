import json
import logging
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.functional import cached_property

from NEMO_keycloak.keycloak.admin import KeycloakAdmin
from NEMO_keycloak.keycloak.authz import KeycloakAuthz
from NEMO_keycloak.keycloak.openid_connect import KeycloakOpenidConnect
from NEMO_keycloak.keycloak.realm import KeycloakRealm
from NEMO_keycloak.keycloak.uma1 import KeycloakUMA1

logger = logging.getLogger(__name__)


class Server(models.Model):
    url = models.CharField(max_length=255)

    internal_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="URL on internal netwerk calls. For example when used with "
        "Docker Compose. Only supply when internal calls should go "
        "to a different url as the end-user will communicate with.",
    )

    def __str__(self):
        return self.url


class Realm(models.Model):
    server = models.ForeignKey(Server, related_name="realms", on_delete=models.CASCADE)

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Name as known on the Keycloak server. " "This name is used in the API paths " "of this Realm.",
    )
    _certs = models.TextField()

    @property
    def certs(self):
        return json.loads(self._certs)

    @certs.setter
    def certs(self, content):
        self._certs = json.dumps(content)

    _well_known_oidc = models.TextField(blank=True)

    @property
    def well_known_oidc(self):
        return json.loads(self._well_known_oidc)

    @well_known_oidc.setter
    def well_known_oidc(self, content):
        self._well_known_oidc = json.dumps(content)

    _keycloak_realm = None

    @cached_property
    def realm_api_client(self) -> KeycloakRealm:
        if self._keycloak_realm is None:
            import NEMO_keycloak.services.realm

            self._keycloak_realm = NEMO_keycloak.services.realm.get_realm_api_client(realm=self)
        return self._keycloak_realm

    def __str__(self):
        return self.name


class OpenIdConnectProfile(models.Model):
    access_token = models.TextField(null=True)
    expires_before = models.DateTimeField(null=True)

    refresh_token = models.TextField(null=True)
    refresh_expires_before = models.DateTimeField(null=True)

    does_not_expire = models.BooleanField(default=False)

    sub = models.CharField(max_length=255, unique=True)

    realm = models.ForeignKey(Realm, related_name="openid_profiles", on_delete=models.CASCADE)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="oidc_profile", on_delete=models.CASCADE)

    @property
    def is_active(self):
        if not self.access_token or not self.expires_before:
            return False

        return self.expires_before > timezone.now()

    @property
    def jwt(self):
        if not self.is_active:
            return None
        client = self.realm.client
        return client.openid_api_client.decode_token(
            token=self.access_token,
            key=client.realm.certs,
            algorithms=client.openid_api_client.well_known["id_token_signing_alg_values_supported"],
        )


class Client(models.Model):
    realm = models.OneToOneField(Realm, related_name="client", on_delete=models.CASCADE)

    client_id = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)

    service_account_profile = models.OneToOneField(OpenIdConnectProfile, on_delete=models.CASCADE, null=True)

    @cached_property
    def admin_api_client(self) -> KeycloakAdmin:
        import NEMO_keycloak.services.client

        return NEMO_keycloak.services.client.get_admin_client(client=self)

    @cached_property
    def openid_api_client(self) -> KeycloakOpenidConnect:
        import NEMO_keycloak.services.client

        return NEMO_keycloak.services.client.get_openid_client(client=self)

    @cached_property
    def authz_api_client(self) -> KeycloakAuthz:
        import NEMO_keycloak.services.client

        return NEMO_keycloak.services.client.get_authz_api_client(client=self)

    @cached_property
    def uma1_api_client(self) -> KeycloakUMA1:
        import NEMO_keycloak.services.client

        return NEMO_keycloak.services.client.get_uma1_client(client=self)

    def __str__(self):
        return self.client_id


class Nonce(models.Model):
    state = models.UUIDField(default=uuid.uuid4, unique=True)
    redirect_uri = models.CharField(max_length=255)
    next_path = models.CharField(max_length=255, null=True)
