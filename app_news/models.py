from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from app_static_pages.models import StaticPage


class News(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_('заголовок'))
    text = models.TextField(blank=True, verbose_name=_('текст'), db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'), db_index=True)
    pub_date = models.DateTimeField(verbose_name=_('дата публикации'), blank=True, null=True)
    visible = models.BooleanField(default=False, verbose_name=_('видимый на сайте'))
    for_all = models.BooleanField(default=False, verbose_name=_('для всех – на странице «Заказы»'))
    for_registered = models.BooleanField(default=False, verbose_name=_('для всех зарегистрированных пользователей в ЛК'))
    for_contractors = models.BooleanField(default=False, verbose_name=_('для заказчиков в ЛК'))
    for_freelancers = models.BooleanField(default=False, verbose_name=_('для фрилансеров в ЛК'))
    for_new_freelancers = models.BooleanField(default=False, verbose_name=_('для новых фрилансеров в ЛК'))
    for_new_contractors = models.BooleanField(default=False, verbose_name=_('для новых заказчиков в ЛК'))
    for_core = models.BooleanField(default=False, verbose_name=_('для участников ядра в ЛК'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _('новость')
        verbose_name_plural = _('новости')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class NewsLink(models.Model):
    text = models.CharField(max_length=255, db_index=True, verbose_name=_('текст ссылки'))
    link = models.ForeignKey(StaticPage, on_delete=models.DO_NOTHING, verbose_name=_('ссылка на статическую страницу'), db_index=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('новость'))

    class Meta:
        verbose_name = _('ссылка на статическую страницу')
        verbose_name_plural = _('ссылки на статические страницы')

    def __str__(self):
        return self.text
