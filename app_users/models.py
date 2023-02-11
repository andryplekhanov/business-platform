from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from .validators import avatar_size_validate


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    full_name = models.CharField(_('ФИО'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('дата регистрации'), auto_now_add=True)
    is_active = models.BooleanField(_('является активным'), default=True)
    is_verified = models.BooleanField(_('прошел верификацию личности'), default=False)
    is_staff = models.BooleanField(default=False, verbose_name=_('является сотрудником'))
    is_freelancer = models.BooleanField(default=False, verbose_name=_('является фрилансером'))
    can_invite_referrals = models.BooleanField(default=False, verbose_name=_('может приглашать рефералов'))
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png')
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True,
                               validators=[image_validator, avatar_size_validate])
    phone_regex = RegexValidator(regex=r'^\+\d{11,15}',
                                 message=_("Номер телефона должен быть в формате: '+79012345678'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name=_('номер телефона'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')

    def __str__(self):
        return self.email
