from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppPortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_portfolio'
    verbose_name = _('портфолио')
