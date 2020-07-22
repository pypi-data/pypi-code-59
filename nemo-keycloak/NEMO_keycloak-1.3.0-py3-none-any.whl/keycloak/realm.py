from typing import Dict

from NEMO_keycloak.keycloak.admin import KeycloakAdmin
from NEMO_keycloak.keycloak.authz import KeycloakAuthz
from NEMO_keycloak.keycloak.client import KeycloakClient
from NEMO_keycloak.keycloak.openid_connect import KeycloakOpenidConnect
from NEMO_keycloak.keycloak.uma import KeycloakUMA
from NEMO_keycloak.keycloak.uma1 import KeycloakUMA1


class KeycloakRealm(object):

    _server_url = None
    _realm_name = None

    _headers = None
    _client: KeycloakClient = None

    def __init__(self, server_url: str, realm_name: str, headers: Dict = None):
        """
        :param str server_url: The base URL where the Keycloak server can be
            found
        :param str realm_name: REALM name
        :param dict headers: Optional extra headers to send with requests to
            the server
        """
        self._server_url = server_url
        self._realm_name = realm_name
        self._headers = headers

    @property
    def client(self) -> KeycloakClient:
        if self._client is None:
            self._client = KeycloakClient(server_url=self._server_url, headers=self._headers)
        return self._client

    @property
    def realm_name(self):
        return self._realm_name

    @property
    def server_url(self):
        return self._server_url

    @property
    def admin(self) -> KeycloakAdmin:
        return KeycloakAdmin(realm=self)

    def open_id_connect(self, client_id: str, client_secret: str) -> KeycloakOpenidConnect:
        """
        Get OpenID Connect client
        """
        return KeycloakOpenidConnect(realm=self, client_id=client_id, client_secret=client_secret)

    def authz(self, client_id: str) -> KeycloakAuthz:
        """
        Get Authz client
        """
        return KeycloakAuthz(realm=self, client_id=client_id)

    def uma(self) -> KeycloakUMA:
        """
        Get UMA client

        This method is here for backwards compatibility
        """
        return self.uma2

    @property
    def uma2(self) -> KeycloakUMA:
        """
        Starting from Keycloak 4 UMA2 is supported
        """
        return KeycloakUMA(realm=self)

    @property
    def uma1(self) -> KeycloakUMA1:
        return KeycloakUMA1(realm=self)

    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
