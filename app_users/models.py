from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .managers import CustomUserManager
from .validators import avatar_size_validate, document_size_validate


class CustomUser(AbstractBaseUser, MPTTModel, PermissionsMixin):
    STATUS_CHOICES = (
        ("0", _("Участник Заказчик")),
        ("1", _("Кандидат")),
        ("2", _("Участник Фрилансер")),
    )
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png')
    )
    document_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'pdf'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .pdf .png')
    )

    email = models.EmailField(_('email'), unique=True, db_index=True)
    email_confirmed = models.BooleanField(_('email подтвержден'), default=False)
    username = models.SlugField(max_length=55, db_index=True, unique=True, verbose_name=_('имя пользователя'), null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=55, blank=True, db_index=True)
    first_name = models.CharField(_('Имя'), max_length=55, blank=True, db_index=True)
    patronymic = models.CharField(_('Отчество'), max_length=55, blank=True, db_index=True)
    country = models.CharField(_('Страна'), max_length=55, blank=True, db_index=True)
    address = models.CharField(_('Адрес'), max_length=255, blank=True, db_index=True)
    personal_number = models.CharField(_('ИНН или персональный номер'), max_length=17, blank=True, null=True, db_index=True)
    document = models.FileField(_('документ'), upload_to='documents/', blank=True, validators=[document_validator, document_size_validate])
    document_number = models.CharField(_('Серия и номер документа'), max_length=55, blank=True, db_index=True)
    document_issued = models.CharField(_('Когда и кем выдан'), max_length=255, blank=True, db_index=True)
    paid_entrance_fee = models.BooleanField(_('Оплатил вступительный взнос'), default=False)
    status = models.CharField(_('статус'), max_length=30, choices=STATUS_CHOICES, default="0", db_index=True)
    date_joined = models.DateTimeField(_('дата регистрации'), auto_now_add=True, db_index=True)
    is_active = models.BooleanField(_('является активным'), default=True)
    is_staff = models.BooleanField(default=False, verbose_name=_('является сотрудником'))
    is_core = models.BooleanField(default=False, verbose_name=_('основатель'), db_index=True)
    on_vacation = models.BooleanField(default=False, verbose_name=_('в отпуске'), db_index=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name=_('родитель'))

    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True, validators=[image_validator, avatar_size_validate])
    phone_regex = RegexValidator(regex=r'^\+\d{11,15}', message=_("Номер телефона должен быть в формате: '+79012345678'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name=_('номер телефона'), db_index=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('баланс'), db_index=True)

    bank_name = models.CharField(_('Наименование банка'), max_length=255, blank=True)
    bank_address = models.CharField(_('Адрес банка'), max_length=255, blank=True)
    bank_bic = models.CharField(_('БИК банка'), max_length=55, blank=True, null=True)
    bank_correspondent_account = models.CharField(_('Корреспондентский счет банка'), max_length=55, blank=True, null=True)
    payment_account = models.CharField(_('Расчетный счет'), max_length=55, blank=True, null=True)
    recipients_name = models.CharField(_('Имя получателя платежа'), max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class MPTTMeta:
        user_insertion_by = ['email']

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')

    def __str__(self):
        return self.email

    def get_referral_url(self):
        if self.status == '2':
            return reverse('signup', args=[int(self.personal_account)])
        return None
    #
    # def get_absolute_url(self):
    #     return reverse('portfolio', args=[self.pk, self.username])

    @property
    def referrals(self):
        level1 = CustomUser.objects.filter(parent=self)
        level2 = CustomUser.objects.filter(parent__in=level1)
        level3 = CustomUser.objects.filter(parent__in=level2)
        return {'level1': level1, 'level2': level2, 'level3': level3}

    @property
    def personal_account(self):
        """ лицевой счет """
        return f"{self.date_joined.strftime('%y%m%d')}{self.pk}"

    def save(self, *args, **kwargs):
        # потом добавить в модель поле 'прошел верификацию' и это поле добавить в список условий ниже
        conditions = [
            self.status == '1', self.is_active, self.paid_entrance_fee, self.email_confirmed, self.phone_number,
            self.last_name, self.first_name, self.country, self.address, self.personal_number,
            self.document, self.document_number, self.document_issued,
        ]
        if all(conditions):
            self.status = '2'
        super().save(*args, **kwargs)
