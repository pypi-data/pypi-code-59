import logging

from django.contrib import admin, messages

from NEMO_keycloak.models import Client, OpenIdConnectProfile
import NEMO_keycloak.services.realm
import NEMO_keycloak.services.uma


logger = logging.getLogger(__name__)


def refresh_open_id_connect_well_known(modeladmin, request, queryset):
    for realm in queryset:
        realm.well_known_oidc = NEMO_keycloak.services.realm.refresh_well_known_oidc(realm=realm)
        realm.save(update_fields=["_well_known_oidc"])
    modeladmin.message_user(request=request, message="OpenID Connect .well-known refreshed", level=messages.SUCCESS)


refresh_open_id_connect_well_known.short_description = "Refresh OpenID " "Connect .well-known"


def refresh_certs(modeladmin, request, queryset):
    for realm in queryset:
        realm.certs = NEMO_keycloak.services.realm.refresh_certs(realm=realm)
        realm.save(update_fields=["_certs"])
    modeladmin.message_user(request=request, message="Certificates refreshed", level=messages.SUCCESS)


refresh_certs.short_description = "Refresh Certificates"


def clear_client_tokens(modeladmin, request, queryset):
    OpenIdConnectProfile.objects.filter(realm__in=queryset).update(
        access_token=None, expires_before=None, refresh_token=None, refresh_expires_before=None
    )
    modeladmin.message_user(request=request, message="Tokens cleared", level=messages.SUCCESS)


clear_client_tokens.short_description = "Clear client tokens"


class ClientAdmin(admin.TabularInline):

    model = Client

    fields = ("client_id", "secret")


class RealmAdmin(admin.ModelAdmin):

    inlines = [ClientAdmin]

    actions = [refresh_open_id_connect_well_known, refresh_certs, clear_client_tokens]

    fieldsets = ((None, {"fields": ("name",)}), ("Location", {"fields": ("server", "_well_known_oidc")}))

    readonly_fields = ("_well_known_oidc",)

    def save_model(self, request, obj, form, change):
        try:
            obj.well_known_oidc = NEMO_keycloak.services.realm.refresh_well_known_oidc(realm=obj)
            obj.certs = NEMO_keycloak.services.realm.refresh_certs(realm=obj)
        except Exception as e:
            logger.exception(str(e))
        super(RealmAdmin, self).save_model(request, obj, form, change)
