from django.apps import AppConfig


class ApkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apka'
    def ready(self):
        from . import signals