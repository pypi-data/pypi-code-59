from django.contrib.auth import HASH_SESSION_KEY, BACKEND_SESSION_KEY, _get_backends
from django.contrib.auth.models import AnonymousUser
from django.middleware.csrf import rotate_token
from django.utils import timezone

import NEMO_keycloak.services.oidc_profile


# Using a different session key than the standard django.contrib.auth to
# make sure there is no cross-referencing between UserModel and RemoteUserModel
REMOTE_SESSION_KEY = "_auth_remote_user_id"


def _get_user_session_key(request):
    return str(request.session[REMOTE_SESSION_KEY])


def get_remote_user(request):
    """

    :param request:
    :return:
    """
    sub = request.session.get(REMOTE_SESSION_KEY)

    user = None

    OpenIdConnectProfile = OpenIdConnectProfile()

    try:
        oidc_profile = OpenIdConnectProfile.objects.get(realm=request.realm, sub=sub)
    except OpenIdConnectProfile.DoesNotExist:
        pass
    else:
        if oidc_profile.refresh_expires_before > timezone.now():
            user = oidc_profile.user

    return user or AnonymousUser()
