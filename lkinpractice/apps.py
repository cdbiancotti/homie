from django.apps import AppConfig


class LkinpracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lkinpractice'

    def ready(self):
        import lkinpractice.signals
