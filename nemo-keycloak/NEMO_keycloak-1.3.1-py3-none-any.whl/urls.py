from django.conf.urls import url

from NEMO_keycloak import views

urlpatterns = [
    url(r"^login-complete$", views.LoginComplete.as_view(), name="keycloak_login_complete"),
    url(r"^session-iframe", views.SessionIframe.as_view(), name="keycloak_session_iframe"),
    url(r"^error", views.ErrorView.as_view(), name="keycloak_error"),
    url(r"^login$", views.Login.as_view(), name="keycloak_login"),
    url(r"^login$", views.Login.as_view(), name="login"),  # overwrite NEMO's login url
    url(r"^logout$", views.Logout.as_view(), name="keycloak_logout"),
    url(r"^logout$", views.Logout.as_view(), name="logout"),  # overwrite NEMO's logout url
]
