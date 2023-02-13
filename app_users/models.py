from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .managers import CustomUserManager
from .validators import avatar_size_validate


class CustomUser(AbstractBaseUser, MPTTModel, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, db_index=True)
    full_name = models.CharField(_('ФИО'), max_length=255, blank=True, db_index=True)
    date_joined = models.DateTimeField(_('дата регистрации'), auto_now_add=True, db_index=True)
    is_active = models.BooleanField(_('является активным'), default=True)
    is_verified = models.BooleanField(_('прошел верификацию личности'), default=False)
    is_staff = models.BooleanField(default=False, verbose_name=_('является сотрудником'))
    is_freelancer = models.BooleanField(default=False, verbose_name=_('является фрилансером'), db_index=True)
    can_invite_referrals = models.BooleanField(default=False, verbose_name=_('может приглашать рефералов'), db_index=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name=_('родитель'))
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png')
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True,
                               validators=[image_validator, avatar_size_validate])
    phone_regex = RegexValidator(regex=r'^\+\d{11,15}',
                                 message=_("Номер телефона должен быть в формате: '+79012345678'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name=_('номер телефона'), db_index=True)
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
        if self.can_invite_referrals:
            return reverse('signup', args=[self.pk])
        return None

    @property
    def level_1_referrals(self):
        return CustomUser.objects.filter(parent=self)

    @property
    def level_2_referrals(self):
        return CustomUser.objects.filter(parent__in=self.level_1_referrals)

    @property
    def level_3_referrals(self):
        return CustomUser.objects.filter(parent__in=self.level_2_referrals)
