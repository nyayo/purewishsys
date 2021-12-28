from django.apps import AppConfig


class PurewishConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purewish'

    def ready(self):
        import purewish.signals
