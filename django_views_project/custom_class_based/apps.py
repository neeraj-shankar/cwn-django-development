from django.apps import AppConfig


class CustomClassBasedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_class_based'
