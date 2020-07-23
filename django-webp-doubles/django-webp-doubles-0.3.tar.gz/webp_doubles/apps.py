from django.apps import AppConfig


class DjangoWebpDoublesConfig(AppConfig):
    name = 'webp_doubles'

    def ready(self):
        from .webp_images import connect_signals
        connect_signals()

