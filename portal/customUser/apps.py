from django.apps import AppConfig


class CustomuserConfig(AppConfig):
    name = 'customUser'

    def ready(self):
            import customUser.signals