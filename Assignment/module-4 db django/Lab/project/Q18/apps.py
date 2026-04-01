from django.apps import AppConfig


class Q18Config(AppConfig):
    name = 'Q18'

    def ready(self):
        import Q18.signals
