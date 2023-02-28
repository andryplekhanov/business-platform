from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from DjBusinessPlatform import settings


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('заголовок'))
    text = models.TextField(max_length=4096, verbose_name=_('текст'))
    visible = models.BooleanField(default=False, verbose_name=_('видимый на сайте'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))
    pub_date = models.DateTimeField(verbose_name=_('дата публикации'), blank=True, null=True)
    end_date = models.DateTimeField(verbose_name=_('дата окончания'), blank=True, null=True)

    def __str__(self):
        return self.title

    def count_choices(self):
        return self.choice_set.count()

    def get_choices(self):
        return self.choice_set.all()

    def is_finished(self):
        return self.end_date < timezone.now()

    def count_total_votes(self):
        result = 0
        for choice in self.choice_set.all():
            result += choice.count_votes()
        return result

    def get_absolute_url(self):
        return reverse('polls-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-pub_date']
        verbose_name = _("вопрос")
        verbose_name_plural = _("вопросы")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('вопрос'))
    text = models.CharField(max_length=255, verbose_name=_('текст'))
    votes = models.IntegerField(default=0, verbose_name=_('количество голосов'))

    def __str__(self):
        return self.text

    def count_votes(self):
        return self.answer_set.count()

    class Meta:
        verbose_name = _("вариант ответа")
        verbose_name_plural = _("варианты ответов")


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('вопрос'))
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name=_('выбор'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата'))

    def __str__(self):
        return self.choice.text

    class Meta:
        ordering = ['-created']
        verbose_name = _("ответ")
        verbose_name_plural = _("ответы")
