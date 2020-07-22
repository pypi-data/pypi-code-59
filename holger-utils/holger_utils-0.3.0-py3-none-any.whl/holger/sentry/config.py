import sentry_sdk
from django.conf import settings
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration

SENTRY_ALLOWED_ALL = getattr(settings, 'SENTRY_ALLOWED_ALL', False)
SENTRY_ALLOWED_STATUS = getattr(settings, 'SENTRY_ALLOWED_STATUS', [])


def init():
    key = getattr(settings, 'SENTRY_KEY', None)
    organization = getattr(settings, 'SENTRY_ORGANIZATION', None)
    project = getattr(settings, 'SENTRY_PROJECT', None)
    if key and organization and project:
        sentry_sdk.init(
            dsn=F"https://{key}@{organization}.ingest.sentry.io/{project}",
            integrations=[DjangoIntegration(), CeleryIntegration()],
            send_default_pii=True
        )
    else:
        raise Exception('sentry config is not provided')
