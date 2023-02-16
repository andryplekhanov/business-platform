from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import gettext_lazy as _


class StaticPage(models.Model):
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    description = RichTextUploadingField(verbose_name=_('основной текстовый контент страницы'), default='', blank=True)
    text_block = RichTextUploadingField(verbose_name=_('дополнительный блок текста'), default='', blank=True)

    def __str__(self):
        return self.flatpage.title

    class Meta:
        verbose_name = _("содержание страницы")
        verbose_name_plural = _("содержание страницы")
