from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(max_length=150, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requirePassword',
                                    'placeholder': _('Введите пароль'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'}))
    password2 = forms.CharField(max_length=150, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requireRepeatPassword',
                                    'placeholder': _('Введите пароль еще раз'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'}))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'avatar', 'phone_number', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


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
