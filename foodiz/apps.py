from django.apps import AppConfig


class FoodizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodiz'


# def ready(self):
#     import foodiz.signals
#     pass