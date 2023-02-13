from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppAdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_ads'
    verbose_name = _('объявления')
