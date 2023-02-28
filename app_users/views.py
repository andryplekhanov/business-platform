from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views import generic
from django.views.generic import TemplateView, UpdateView

from .forms import CustomUserCreationForm, PasswordSetForm, CustomUserChangeForm, ResetPasswordForm
from .utils import send_email_for_verify, get_referrer

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'app_users/home.html'
    extra_context = {'title': _('Главная страница'), 'current_elem': 'home'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Регистрирует кандидатов во фрилансеры по реф. ссылке. НЕ ИСПОЛЬЗОВАТЬ для регистрации заказчиков.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "app_users/profile/signup.html"
    extra_context = {'title': _('Регистрация'), 'current_elem': 'signup'}

    def get(self, request, *args, **kwargs):
        referrer = get_referrer(kwargs.get('personal_account'))
        if not referrer:
            return redirect('signup_error')

        if referrer.status != '2':
            return redirect('signup_error')

        if request.user.id == referrer.id:
            return redirect('home')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        referrer = get_referrer(kwargs.get('personal_account'))
        if not referrer:
            raise ValidationError(_('Данная ссылка-приглашение невалидна'))
        if referrer.status != '2' and not referrer.is_core:
            raise ValidationError(_('Данная ссылка-приглашение невалидна'))

        if form.is_valid():
            instance = form.save(commit=False)
            instance.parent = referrer
            instance.status = '1'
            instance.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)

            return redirect('confirm_email')
        return super().post(request, *args, **kwargs)


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_confirmed = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.email_confirmed:
                send_email_for_verify(request, user)
                return HttpResponseRedirect(reverse('confirm_email'))
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))


def signup_error(request):
    return render(
        request,
        'app_users/profile/signup_error.html',
        {'title': _('Регистрация не возможна'), 'current_elem': 'signup_error'}
    )


class EditProfileView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = CustomUserChangeForm
    model = User
    template_name = 'app_users/profile/edit_profile.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': _('Редактировать профиль'),
        'current_elem': 'edit_profile',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile'}
    }

    def get_success_url(self):
        return reverse('edit_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.info(self.request, _("Профиль успешно сохранен"))
        user = self.request.user

        if form.cleaned_data.get('password1'):
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            logout(self.request)
            user = authenticate(email=email, password=password)
            login(self.request, user)
        return super(EditProfileView, self).form_valid(form)


class LogOutView(LogoutView):
    next_page = '/'


class ResetPasswordView(PasswordResetView):
    email_template_name = 'app_users/profile/password_reset_email.html'
    template_name = 'app_users/profile/password_reset_form.html'
    form_class = ResetPasswordForm
    extra_context = {'title': _('Сброс пароля'), 'current_elem': 'password_reset'}


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'app_users/profile/password_reset_done.html'
    extra_context = {'title': _('Сброс пароля'), 'current_elem': 'password_reset_done'}


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'app_users/profile/password_reset_confirm.html'
    form_class = PasswordSetForm
    post_reset_login = False
    extra_context = {'title': _('Создание нового пароля'), 'current_elem': 'password_reset_confirm'}

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'app_users/profile/password_reset_complete.html'
    extra_context = {'title': _('Новый пароль успешно создан'), 'current_elem': 'password_reset_complete'}


@login_required
def balance(request):
    context = {
        'user': request.user, 'title': _('Баланс'), 'current_elem': 'balance',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Баланс'): 'balance'}
    }

    return render(
        request,
        'app_users/others/balance.html',
        context=context
    )


@login_required
def topup_withdrawal(request):
    context = {
        'user': request.user, 'title': _('Пополнение / Вывод'), 'current_elem': 'topup_withdrawal',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Пополнение / Вывод'): 'topup_withdrawal'}
    }
    return render(
        request,
        'app_users/others/topup_withdrawal.html',
        context=context
    )


# в отдельное приложение
@login_required
def contracts(request):
    context = {
        'user': request.user, 'title': _('Заказы'), 'current_elem': 'contracts',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Заказы'): 'contracts'}
    }
    return render(
        request,
        'app_users/others/contracts.html',
        context=context
    )


# в отдельное приложение
@login_required
def contests(request):
    context = {
        'user': request.user, 'title': _('Конкурсы'), 'current_elem': 'contests',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Конкурсы'): 'contests'}
    }
    return render(
        request,
        'app_users/others/contests.html',
        context=context
    )


# в отдельное приложение
@login_required
def place_contract(request):
    context = {
        'user': request.user, 'title': _('Разместить заказ'), 'current_elem': 'place_contract',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Разместить заказ'): 'place_contract'}
    }
    return render(
        request,
        'app_users/others/place_contract.html',
        context=context
    )


# в отдельное приложение
@login_required
def announce_contest(request):
    context = {
        'user': request.user, 'title': _('Объявить конкурс'), 'current_elem': 'announce_contest',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Объявить конкурс'): 'announce_contest'}
    }
    return render(
        request,
        'app_users/others/announce_contest.html',
        context=context
    )


# в отдельное приложение
@login_required
def search_contractor(request):
    context = {
        'user': request.user, 'title': _('Поиск исполнителя'), 'current_elem': 'search_contractor',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Поиск исполнителя'): 'search_contractor'}
    }
    return render(
        request,
        'app_users/others/search_contractor.html',
        context=context
    )


# в отдельное приложение
@login_required
def chat(request):
    context = {
        'user': request.user, 'title': _('Чат'), 'current_elem': 'chat',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Чат'): 'chat'}
    }
    return render(
        request,
        'app_users/others/chat.html',
        context=context
    )


@login_required
def support(request):
    context = {
        'user': request.user, 'title': _('Помощь'), 'current_elem': 'support',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Помощь'): 'support'}
    }
    return render(
        request,
        'app_users/others/support.html',
        context=context
    )


@login_required
def account_notification_view(request):
    context = {
        'user': request.user, 'title': _('Уведомления'), 'current_elem': 'notifications',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Уведомления'): 'notifications'}
    }
    return render(
        request,
        'app_users/profile/notifications.html',
        context=context
    )


@login_required
def account_verification_view(request):
    context = {
        'user': request.user, 'title': _('Верификация'), 'current_elem': 'verification',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Верификация'): 'verification'}
    }
    return render(
        request,
        'app_users/profile/verification.html',
        context=context
    )


@login_required
def account_agreement_view(request):
    context = {
        'user': request.user, 'title': _('Договор'), 'current_elem': 'agreement',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Договор'): 'agreement'}
    }
    return render(
        request,
        'app_users/profile/agreement.html',
        context=context
    )


@login_required
def account_security_view(request):
    context = {
        'user': request.user, 'title': _('Пароль и безопасность'), 'current_elem': 'password_and_security',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Пароль и безопасность'): 'password_and_security'}
    }
    return render(
        request,
        'app_users/profile/password_security.html',
        context=context
    )


@login_required
def shareholders_book(request):
    context = {
        'user': request.user, 'title': _('Электронная книжка Пайщика'),
    }
    return render(
        request,
        'app_users/others/shareholders_book.html',
        context=context
    )
