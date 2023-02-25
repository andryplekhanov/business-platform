from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from app_ads.models import Category
from app_portfolio.validators import file_size_validate

User = get_user_model()


class Work(models.Model):
    CURRENCY_CHOICES = (
        ("USD", _("$")),
        ("RUB", _("₽")),
        ("EUR", _("€")),
    )
    TIME_CHOICES = (
        ("h", _("в часах")),
        ("d", _("в днях")),
        ("m", _("в месяцах")),
    )
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .png')
    )

    user = models.ForeignKey(User, related_name='works', on_delete=models.CASCADE, verbose_name=_('пользователь'))
    title = models.CharField(max_length=255, verbose_name=_('заголовок'))
    description = models.TextField(verbose_name=_('описание'))
    image = models.ImageField(upload_to='portfolio/covers/', null=True, blank=True, validators=[image_validator, file_size_validate], verbose_name=_('обложка'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'), db_index=True)
    corrected_at = models.DateTimeField(auto_now=True, verbose_name=_('дата изменения'), db_index=True)
    price = models.DecimalField(_('стоимость'), default=0, max_digits=18, decimal_places=2, null=True, blank=True)
    price_currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, verbose_name=_('валюта'), null=True, blank=True)
    time_spent = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name=_('потрачено времени'))
    time_type = models.CharField(choices=TIME_CHOICES, max_length=3, verbose_name=_('время'), null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name=_('ссылка'), null=True, blank=True)
    video = models.CharField(max_length=255, verbose_name=_('видео'), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_('категория'), on_delete=models.SET_NULL, null=True, related_name='works')
    is_active = models.BooleanField(default=True, verbose_name=_('активна'), db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('работа')
        verbose_name_plural = _('работы')
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('portfolio_best_detail', args=[str(self.id)])


class File(models.Model):
    file = models.FileField(upload_to='portfolio/files/', verbose_name=_('файл'), validators=[file_size_validate])
    work = models.ForeignKey('Work', related_name='files', verbose_name=_('работа'), on_delete=models.CASCADE)

    def __str__(self):
        return f'file{self.id} for {self.work}'

    class Meta:
        verbose_name = _('файл')
        verbose_name_plural = _('файлы')
