from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from app_ads.validators import image_size_validate

User = get_user_model()
image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif', 'svg'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png .svg')
    )


class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('название'))
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name=_('url-адрес'))
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name=_('родительская категория'))
    image = models.ImageField(blank=True, upload_to='category/%Y/%m/%d/', verbose_name=_('изображение'), db_index=True,
                              validators=[image_validator, image_size_validate])

    class MPTTMeta:
        adv_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        ordering = ('name',)
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

    def get_absolute_url(self):
        return reverse('adv-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Adv(models.Model):
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='category', verbose_name=_('категория'), db_index=True)
    author = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE, verbose_name=_('автор'), db_index=True)
    title = models.CharField(max_length=255, db_index=True, verbose_name=_('заголовок'))
    description = models.TextField(blank=True, verbose_name=_('описание'), db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('цена'), db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'), db_index=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('дата обновления'), db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('объявление')
        verbose_name_plural = _('объявления')

    def get_absolute_url(self):
        return reverse('adv', args=[str(self.id)])
