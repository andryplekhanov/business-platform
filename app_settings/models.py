from django.db import models
from django.utils.translation import gettext_lazy as _

from .singleton_model import SingletonModel
from .validators import icon_validator, icon_size_validate


# class ContactSettings(SingletonModel):
#     pass
#
#     def __str__(self):
#         return str(_('контакты'))
#
#     class Meta:
#         verbose_name = _('контакты')
#         verbose_name_plural = _('контакты')
#
#
# class ContactGrop(models.Model):
#     contact_settings = models.ForeignKey('ContactSettings', related_name='group', on_delete=models.CASCADE, verbose_name=_('настройки контактов'))
#     department = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('название отдела'))
#     email = models.EmailField('email', null=True, blank=True)
#     phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона'))
#     address = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('адрес'))
#
#     class Meta:
#         verbose_name = _('группа контактов')
#         verbose_name_plural = _('группы контактов')
#
#     def __str__(self):
#         return f'Contact group {self.id}'


class CompanySettings(SingletonModel):
    company = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('название компании'))
    slogan = models.TextField(null=True, blank=True, verbose_name=_('слоган'))
    description = models.TextField(null=True, blank=True, verbose_name=_('краткое описание'))
    email = models.EmailField('email', null=True, blank=True)
    phone_number1 = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона1'))
    phone_number2 = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона2'))
    phone_number3 = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('номер телефона3'))
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('адрес'))

    def __str__(self):
        return str(_('компания'))

    class Meta:
        verbose_name = _('компания')
        verbose_name_plural = _('компания')


# class FooterPagesRightSet(SingletonModel):
#     footer_pages = models.ManyToManyField('app_static_pages.StaticPage', verbose_name=_('статичные страницы для футера (справа)'))
#
#     class Meta:
#         verbose_name = _('статичные страницы для футера (справа)')
#         verbose_name_plural = _('статичные страницы для футера (справа)')
#
#     def __str__(self):
#         return f'Pages set right'
#
#
# class FooterPagesLeftSet(SingletonModel):
#     footer_pages = models.ManyToManyField('app_static_pages.StaticPage', verbose_name=_('статичные страницы для футера (слева)'))
#
#     class Meta:
#         verbose_name = _('статичные страницы для футера (слева)')
#         verbose_name_plural = _('статичные страницы для футера (слева)')
#
#     def __str__(self):
#         return f'Pages set left'


class SocialMedia(SingletonModel):
    pass

    def __str__(self):
        return str(_('социальные сети'))

    class Meta:
        verbose_name = _('социальные сети')
        verbose_name_plural = _('социальные сети')


class SocialMediaItem(models.Model):
    social_media = models.ForeignKey('SocialMedia', related_name='social_media_item', on_delete=models.CASCADE, verbose_name=_('социальные сети'))
    name = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('название'))
    link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('ссылка'), unique=True)
    icon = models.FileField(upload_to='social_media/', null=True, blank=True, verbose_name=_('иконка'), db_index=True,
                            validators=[icon_validator, icon_size_validate])

    class Meta:
        verbose_name = _('соцсеть')
        verbose_name_plural = _('соцсети')

    def __str__(self):
        return f'SocialMedia {self.name}'
