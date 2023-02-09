from django.db import models
from django.utils.translation import gettext_lazy as _
from .singleton_model import SingletonModel


class ContactSettings(SingletonModel):
    pass

    def __str__(self):
        return str(_('контакты'))

    class Meta:
        verbose_name = _('контакты')
        verbose_name_plural = _('контакты')


class ContactGrop(models.Model):
    contact_settings = models.ForeignKey('ContactSettings', related_name='group', on_delete=models.CASCADE, verbose_name=_('настройки контактов'))
    department = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('название отдела'))
    email = models.EmailField('email', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона'))
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('адрес'))

    class Meta:
        verbose_name = _('группа контактов')
        verbose_name_plural = _('группы контактов')

    def __str__(self):
        return f'Contact group {self.id}'


class CompanySettings(SingletonModel):
    company = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('название компании'))
    slogan = models.TextField(null=True, blank=True, verbose_name=_('слоган'))
    description = models.TextField(null=True, blank=True, verbose_name=_('краткое описание'))
    email = models.EmailField('email', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона'))
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('адрес'))

    def __str__(self):
        return str(_('компания'))

    class Meta:
        verbose_name = _('компания')
        verbose_name_plural = _('компания')


class FooterPagesSet(SingletonModel):
    footer_pages = models.ManyToManyField('app_static_pages.StaticPage', verbose_name=_('статичные страницы для футера'))

    class Meta:
        verbose_name = _('статичные страницы для футера')
        verbose_name_plural = _('статичные страницы для футера')

    def __str__(self):
        return f'Pages set'
