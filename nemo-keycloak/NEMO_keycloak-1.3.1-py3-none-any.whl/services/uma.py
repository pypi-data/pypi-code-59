from typing import List

from django.apps import AppConfig
from django.apps.registry import apps
from django.db.models.options import Options
from django.utils.text import slugify

import NEMO_keycloak.services.client
from NEMO_keycloak.keycloak.exceptions import KeycloakClientError
from NEMO_keycloak.models import Client


def synchronize_client(client: Client):
    """
    Synchronize all models as resources for a client.
    """
    for app_config in apps.get_app_configs():
        synchronize_resources(client=client, app_config=app_config)


def synchronize_resources(client: Client, app_config: AppConfig):
    """
    Synchronize all resources (models) to the Keycloak server for given client and Django App.
    """

    if not app_config.models_module:
        return

    uma1_client = client.uma1_api_client

    access_token = NEMO_keycloak.services.client.get_access_token(client=client)

    for klass in app_config.get_models():
        scopes = _get_all_permissions(klass._meta)

        try:
            uma1_client.resource_set_create(
                token=access_token,
                name=klass._meta.label_lower,
                type="urn:{client}:resources:{model}".format(
                    client=slugify(client.client_id), model=klass._meta.label_lower
                ),
                scopes=scopes,
            )
        except KeycloakClientError as e:
            if e.original_exc.response.status_code != 409:
                raise


def _get_all_permissions(meta: Options) -> List:
    return meta.default_permissions
