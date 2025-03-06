from django.apps import AppConfig


class EcousersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecousers'

    def ready(self):
        import ecousers.signals  # Import the signals
