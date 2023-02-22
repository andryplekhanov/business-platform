from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Transaction(models.Model):
    REASON_CHOICES = (
        ("NR", _("Нет причины")),  # No Reason
        ("СP", _("Оплата сделки")),  # Contract Payment
        ("TUBT", _("Пополнение переводом (вручную)")),  # Top Up Bank Transfer
        ("WDBT", _("Вывод переводом (вручную)")),  # Withdrawal Bank Transfer
        ("TU", _("Пополнение")),  # Top Up
        ("WD", _("Вывод")),  # Withdrawal
        ("1LС", _("Рефералы 1го уровня - сделка")),  # 1 Level Contract
        ("2LС", _("Рефералы 2го уровня - сделка")),  # 2 Level Contract
        ("3LС", _("Рефералы 3го уровня - сделка")),  # 3 Level Contract
        ("1LE", _("Рефералы 1го уровня - вступление")),  # 1 Level Entrance
        ("2LE", _("Рефералы 2го уровня - вступление")),  # 2 Level Entrance
        ("3LE", _("Рефералы 3го уровня - вступление")),  # 3 Level Entrance
    )
    DIRECTION_CHOICES = (
        ("CRE", _("Зачисление")),
        ("DEB", _("Списание")),
    )

    user = models.ForeignKey(User, related_name='transactions', on_delete=models.SET_NULL, verbose_name=_('пользователь'), null=True)
    reason = models.CharField(choices=REASON_CHOICES, max_length=5, default="NR", verbose_name=_('причина'))
    direction = models.CharField(choices=DIRECTION_CHOICES, max_length=5, verbose_name=_('тип операции'))
    amount = models.DecimalField(_('сумма'), default=0, max_digits=18, decimal_places=2)
    datetime = models.DateTimeField(_('дата транзакции'), auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-datetime',)
        verbose_name = _('транзакция')
        verbose_name_plural = _('транзакции')

    def __str__(self):
        return f'#{self.pk}: {self.user} {self.user.personal_account}'

    def save(self, *args, **kwargs):
        if self.direction == 'CRE':
            self.user.increase_balance(self.amount)
        elif self.direction == 'DEB':
            self.user.reduce_balance(self.amount)
        super().save(*args, **kwargs)

