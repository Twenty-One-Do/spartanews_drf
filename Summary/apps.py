from django.apps import AppConfig


class SummaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Summary'

    def ready(self):
        import nltk
        nltk.download('punkt')
