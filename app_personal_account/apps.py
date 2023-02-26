from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppPersonalAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_personal_account'
    verbose_name = _('пользовательские счета')
