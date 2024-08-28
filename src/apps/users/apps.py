from django.apps import AppConfig
from .services.nationality_service import NationalityService

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        from .signals import create_user_profile
        NationalityService.fetch_and_save_demonyms()
