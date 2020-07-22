from __future__ import unicode_literals

import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http.response import HttpResponseBadRequest
from django.shortcuts import resolve_url, redirect
from django.urls.base import reverse
from django.views.generic.base import RedirectView, TemplateView

from NEMO_keycloak.models import Nonce


logger = logging.getLogger(__name__)


class Login(RedirectView):
    def get_redirect_url(self, *args, **kwargs):

        nonce = Nonce.objects.create(
            redirect_uri=self.request.build_absolute_uri(location=reverse("keycloak_login_complete")),
            next_path=self.request.GET.get("next"),
        )

        self.request.session["oidc_state"] = str(nonce.state)

        authorization_url = self.request.realm.client.openid_api_client.authorization_url(
            redirect_uri=nonce.redirect_uri, scope="openid", state=str(nonce.state)
        )

        if self.request.realm.server.internal_url:
            authorization_url = authorization_url.replace(
                self.request.realm.server.internal_url, self.request.realm.server.url, 1
            )

        logger.debug(authorization_url)

        return authorization_url


class LoginComplete(RedirectView):
    def get(self, *args, **kwargs):
        request = self.request

        if "error" in request.GET:
            messages.add_message(request, messages.ERROR, request.GET["error"])
            logger.error(request.GET["error"])
            return redirect("keycloak_error")

        if "code" not in request.GET and "state" not in request.GET:
            logger.error('code and state need to be present in the request parameters')
            return HttpResponseBadRequest()

        if "oidc_state" not in request.session or request.GET["state"] != request.session["oidc_state"]:
            # Missing or incorrect state; login again.
            messages.add_message(request, messages.ERROR, "Missing or incorrect state, try logging in again")
            logger.error("Missing or incorrect state, try logging in again")
            return redirect("keycloak_error")

        nonce = Nonce.objects.get(state=request.GET["state"])

        try:
            user = authenticate(request=request, code=request.GET["code"], redirect_uri=nonce.redirect_uri)
        except get_user_model().DoesNotExist:
            nonce.delete()
            messages.add_message(request, messages.ERROR, "The user does not exists in the database")
            logger.error("The keycloak user does not exists in the application database")
            return redirect("keycloak_error")
        except Exception as e:
            nonce.delete()
            messages.add_message(request, messages.ERROR, f"An error occurred: {str(e)}")
            logger.exception(e)
            return redirect("keycloak_error")

        if user:
            login(request, user)
            nonce.delete()
            return redirect(nonce.next_path or "/")
        else:
            nonce.delete()
            messages.add_message(request, messages.ERROR, "Could not authenticate user")
            logger.error("Could not authenticate user")
            return redirect("keycloak_error")


class Logout(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if hasattr(self.request.user, "oidc_profile"):
            self.request.realm.client.openid_api_client.logout(self.request.user.oidc_profile.refresh_token)
            self.request.user.oidc_profile.access_token = None
            self.request.user.oidc_profile.expires_before = None
            self.request.user.oidc_profile.refresh_token = None
            self.request.user.oidc_profile.refresh_expires_before = None
            self.request.user.oidc_profile.does_not_expire = False
            self.request.user.oidc_profile.save(
                update_fields=["access_token", "expires_before", "refresh_token", "refresh_expires_before", "does_not_expire"]
            )

        logout(self.request)

        if settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)

        return reverse("keycloak_login")


class SessionIframe(TemplateView):
    template_name = "NEMO_keycloak/session_iframe.html"

    @property
    def op_location(self):
        realm = self.request.realm
        if realm.server.internal_url:
            return realm.well_known_oidc["check_session_iframe"].replace(realm.server.internal_url, realm.server.url, 1)
        return realm.server.url

    @property
    def client_id(self):
        if not hasattr(self.request, "realm"):
            return None

        realm = self.request.realm
        return realm.client.client_id

    def get_context_data(self, **kwargs):
        return super(SessionIframe, self).get_context_data(
            client_id=self.client_id,
            identity_server=self.request.realm.server.url,
            op_location=self.op_location,
            cookie_name=getattr(settings, "KEYCLOAK_SESSION_STATE_COOKIE_NAME", "session_state"),
        )


class ErrorView(TemplateView):
    template_name = "NEMO_keycloak/error.html"
