from django.contrib import admin

from NEMO_keycloak.admin.realm import RealmAdmin
from NEMO_keycloak.admin.server import ServerAdmin
from NEMO_keycloak.models import Server, Realm

admin.site.register(Realm, RealmAdmin)
admin.site.register(Server, ServerAdmin)
