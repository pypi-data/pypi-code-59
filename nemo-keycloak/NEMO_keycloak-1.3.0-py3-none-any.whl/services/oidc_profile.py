from datetime import timedelta, datetime

import logging
from typing import Dict, Optional

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from NEMO_keycloak.models import OpenIdConnectProfile, Client
from NEMO_keycloak.services.exceptions import TokensExpired, InactiveUser

import NEMO_keycloak.services.realm

logger = logging.getLogger(__name__)


def get_or_create_from_id_token(client: Client, id_token: str) -> OpenIdConnectProfile:
    """
	Get or create OpenID Connect profile from given id_token.
	"""
    issuer = NEMO_keycloak.services.realm.get_issuer(client.realm)

    id_token_object = client.openid_api_client.decode_token(
        token=id_token,
        key=client.realm.certs,
        algorithms=client.openid_api_client.well_known["id_token_signing_alg_values_supported"],
        issuer=issuer,
    )

    return update_or_create_user_and_oidc_profile(client=client, id_token_object=id_token_object)


def update_or_create_user_and_oidc_profile(client: Client, id_token_object: Dict) -> Optional[OpenIdConnectProfile]:
    with transaction.atomic():
        UserModel = get_user_model()
        email_field_name = UserModel.get_email_field_name()
        token_username = id_token_object[settings.KEYCLOAK_TOKEN_USERNAME_FIELD]

        try:
            user = UserModel.objects.get(username=token_username)
            if not user.is_active:
                logger.warning(
                    f"User {token_username} successfully authenticated with Keycloak, but that user is marked inactive in the database. The user was denied access."
                )
                raise InactiveUser(f"User {token_username} is inactive")
            defaults = {}
            if id_token_object.get("email", None):
                defaults[email_field_name] = id_token_object["email"]
            if id_token_object.get("given_name", None):
                defaults["first_name"] = id_token_object["given_name"]
            if id_token_object.get("family_name", None):
                defaults["last_name"] = id_token_object["family_name"]
            if settings.KEYCLOAK_UPDATE_DJANGO_USER:
                logger.debug(f"Updating user {user} with defaults {defaults}")
                user = UserModel.objects.update(username=token_username, defaults=defaults)
        except UserModel.DoesNotExist:
            if settings.KEYCLOAK_CREATE_DJANGO_USER:
                logger.debug(f"Creating user with username {token_username} and defaults {defaults}")
                user = UserModel.objects.create(username=token_username, defaults=defaults)
                logger.warning(
                    f"Username {token_username} attempted to authenticate with Keycloak, but that username does not exist in the database. User was created."
                )
            else:
                logger.warning(
                    f"Username {token_username} attempted to authenticate with Keycloak, but that username does not exist in the database. User was denied access."
                )
                raise

        oidc_profile, _ = OpenIdConnectProfile.objects.update_or_create(
            sub=id_token_object["sub"], defaults={"realm": client.realm, "user": user, "does_not_expire": id_token_object.get("does_not_expire", False)}
        )

    return oidc_profile


def update_or_create_from_code(code: str, client: Client, redirect_uri: str) -> OpenIdConnectProfile:
    # Define "initiate_time" before getting the access token to calculate
    # before which time it expires.
    initiate_time = timezone.now()
    token_response = client.openid_api_client.authorization_code(code=code, redirect_uri=redirect_uri)

    return _update_or_create(client=client, token_response=token_response, initiate_time=initiate_time)


def update_or_create_from_password_credentials(username: str, password: str, client: Client) -> OpenIdConnectProfile:
    # Define "initiate_time" before getting the access token to calculate
    # before which time it expires.
    initiate_time = timezone.now()
    token_response = client.openid_api_client.password_credentials(username=username, password=password)

    return _update_or_create(client=client, token_response=token_response, initiate_time=initiate_time)


def _update_or_create(client: Client, token_response: Dict, initiate_time: datetime) -> OpenIdConnectProfile:
    """
	Update or create an user based on a token response.

	`token_response` contains the items returned by the OpenIDConnect Token API
	end-point:
	 - id_token
	 - access_token
	 - expires_in
	 - refresh_token
	 - refresh_expires_in

	"""
    issuer = NEMO_keycloak.services.realm.get_issuer(client.realm)

    token_response_key = "id_token" if "id_token" in token_response else "access_token"

    token_object = client.openid_api_client.decode_token(
        token=token_response[token_response_key],
        key=client.realm.certs,
        algorithms=client.openid_api_client.well_known["id_token_signing_alg_values_supported"],
        issuer=issuer,
    )

    try:
        oidc_profile = update_or_create_user_and_oidc_profile(client=client, id_token_object=token_object)
    except Exception as e:
        # we need to logout the openid client in case of error
        client.openid_api_client.logout(token_response["refresh_token"])
        raise

    return update_tokens(oidc_profile=oidc_profile, token_response=token_response, initiate_time=initiate_time)


def update_tokens(
    oidc_profile: OpenIdConnectProfile, token_response: Dict, initiate_time: datetime
) -> OpenIdConnectProfile:
    """
	Update tokens on the OpenID Connect profile
	"""
    expires_before = initiate_time + timedelta(seconds=token_response["expires_in"])
    refresh_expires_before = initiate_time + timedelta(seconds=token_response["refresh_expires_in"])

    oidc_profile.access_token = token_response["access_token"]
    oidc_profile.expires_before = expires_before
    oidc_profile.refresh_token = token_response["refresh_token"]
    oidc_profile.refresh_expires_before = refresh_expires_before

    oidc_profile.save(update_fields=["access_token", "expires_before", "refresh_token", "refresh_expires_before"])
    return oidc_profile


def get_active_access_token(oidc_profile: OpenIdConnectProfile) -> str:
    """
	Give access_token and refresh when required.
	"""
    initiate_time = timezone.now()

    if oidc_profile.refresh_expires_before is None or initiate_time > oidc_profile.refresh_expires_before:
        raise TokensExpired()

    if initiate_time > oidc_profile.expires_before:
        # Refresh token
        token_response = oidc_profile.realm.client.openid_api_client.refresh_token(
            refresh_token=oidc_profile.refresh_token
        )

        oidc_profile = update_tokens(
            oidc_profile=oidc_profile, token_response=token_response, initiate_time=initiate_time
        )

    return oidc_profile.access_token


def get_entitlement(oidc_profile: OpenIdConnectProfile) -> Dict:
    """
	Get entitlement.

	http://www.keycloak.org/docs/latest/authorization_services/index.html#_service_entitlement_api
	"""
    access_token = get_active_access_token(oidc_profile=oidc_profile)

    rpt = oidc_profile.realm.client.authz_api_client.entitlement(token=access_token)

    rpt_decoded = oidc_profile.realm.client.openid_api_client.decode_token(
        token=rpt["rpt"],
        key=oidc_profile.realm.certs,
        options={"verify_signature": True, "exp": True, "iat": True, "aud": True},
    )
    return rpt_decoded


def get_decoded_jwt(oidc_profile: OpenIdConnectProfile):
    client = oidc_profile.realm.client

    active_access_token = get_active_access_token(oidc_profile=oidc_profile)

    return client.openid_api_client.decode_token(
        token=active_access_token,
        key=client.realm.certs,
        algorithms=client.openid_api_client.well_known["id_token_signing_alg_values_supported"],
    )
