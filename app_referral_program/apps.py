from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppReferralProgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_referral_program'
    verbose_name = _('реферальная программа')
