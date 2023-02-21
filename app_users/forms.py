from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.core.validators import validate_slug, validate_email
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    username = forms.SlugField(max_length=55, required=False, label=_('Имя пользователя'), validators=[validate_slug],
                               widget=forms.TextInput(attrs={
                                    'data-validate': 'require',
                                    'placeholder': _('Придумайте псевдоним, который будет отображаться на страницах сайта'),
                                    'maxlength': '55'
                                }))
    email = forms.EmailField(max_length=55, label='email', required=True, validators=[validate_email],
                             widget=forms.TextInput(attrs={
                                 'data-validate': 'require',
                                 'placeholder': _('E-mail'),
                                 'maxlength': '55'
                             }))
    last_name = forms.CharField(max_length=55, label=_('Фамилия'), required=False,
                                widget=forms.TextInput(attrs={
                                     'data-validate': 'require',
                                     'placeholder': _('Фамилия'),
                                     'maxlength': '55'
                                }))
    first_name = forms.CharField(max_length=55, label=_('Имя'), required=False,
                                 widget=forms.TextInput(attrs={
                                     'data-validate': 'require',
                                     'placeholder': _('Имя'),
                                     'maxlength': '55'
                                 }))
    patronymic = forms.CharField(max_length=55, label=_('Отчество'), required=False,
                                 widget=forms.TextInput(attrs={
                                     'data-validate': 'require',
                                     'placeholder': _('Отчество'),
                                     'maxlength': '55'
                                 }))
    country = forms.CharField(max_length=55, label=_('Страна'), required=False,
                              widget=forms.TextInput(attrs={
                                 'data-validate': 'require',
                                 'placeholder': _('Страна'),
                                 'maxlength': '55'
                              }))
    address = forms.CharField(max_length=255, label=_('Адрес'), required=False,
                              widget=forms.TextInput(attrs={
                                 'data-validate': 'require',
                                 'placeholder': _('Адрес'),
                                 'maxlength': '255'
                              }))
    personal_number = forms.CharField(max_length=17, label=_('ИНН или персональный номер'), required=False,
                                      widget=forms.TextInput(attrs={
                                         'data-validate': 'require',
                                         'placeholder': _('ИНН или персональный номер'),
                                         'maxlength': '17'
                                      }))
    phone_number = forms.CharField(max_length=17, label=_('Телефон'), required=False,
                                   widget=forms.TextInput(attrs={
                                       'data-validate': 'require',
                                       'placeholder': _('Телефон'),
                                       'maxlength': '17'
                                   }))
    document = forms.FileField(required=False, label=_('Документ'),
                               widget=forms.ClearableFileInput(attrs={
                                   'class': 'personal-doc-button',
                                   'type': 'file',
                                   'accept': '.jpg,.pdf,.png',
                               }))
    document_number = forms.CharField(max_length=55, label=_('Серия и номер документа'), required=False,
                                      widget=forms.TextInput(attrs={
                                         'data-validate': 'require',
                                         'placeholder': _('Серия и номер документа'),
                                         'maxlength': '55'
                                      }))
    document_issued = forms.CharField(max_length=255, label=_('Когда и кем выдан'), required=False,
                                      widget=forms.TextInput(attrs={
                                         'data-validate': 'require',
                                         'placeholder': _('Когда и кем выдан'),
                                         'maxlength': '255'
                                      }))
    bank_name = forms.CharField(max_length=255, label=_('Наименование банка'), required=False,
                                widget=forms.TextInput(attrs={
                                    'data-validate': 'require',
                                    'placeholder': _('Наименование банка'),
                                    'maxlength': '255'
                                }))
    bank_address = forms.CharField(max_length=255, label=_('Адрес банка'), required=False,
                                   widget=forms.TextInput(attrs={
                                       'data-validate': 'require',
                                       'placeholder': _('Адрес банка'),
                                       'maxlength': '255'
                                   }))
    bank_bic = forms.CharField(max_length=55, label=_('БИК банка'), required=False,
                               widget=forms.TextInput(attrs={
                                   'data-validate': 'require',
                                   'placeholder': _('БИК банка'),
                                   'maxlength': '55'
                               }))
    bank_correspondent_account = forms.CharField(max_length=55, label=_('Корреспондентский счет банка'), required=False,
                                                 widget=forms.TextInput(attrs={
                                                     'data-validate': 'require',
                                                     'placeholder': _('Корреспондентский счет банка'),
                                                     'maxlength': '55'
                                                 }))
    payment_account = forms.CharField(max_length=55, label=_('Расчетный счет'), required=False,
                                      widget=forms.TextInput(attrs={
                                         'data-validate': 'require',
                                         'placeholder': _('Расчетный счет'),
                                         'maxlength': '55'
                                      }))
    recipients_name = forms.CharField(max_length=255, label=_('Имя получателя платежа'), required=False,
                                      widget=forms.TextInput(attrs={
                                         'data-validate': 'require',
                                         'placeholder': _('Имя получателя платежа'),
                                         'maxlength': '255'
                                      }))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'last_name', 'first_name', 'patronymic', 'country', 'address', 'phone_number',
            'personal_number', 'document', 'document_number', 'document_issued', 'bank_name', 'bank_address',
            'bank_bic', 'bank_correspondent_account', 'payment_account', 'recipients_name'
        )


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(max_length=250, required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'require',
                                 'maxlength': '250',
                                 'autocomplete': 'email'
                             }))


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=150, strip=False, required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requirePassword',
                                        'placeholder': _('Введите пароль'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
    new_password2 = forms.CharField(max_length=150, required=True, strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requireRepeatPassword',
                                        'placeholder': _('Введите пароль еще раз'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
