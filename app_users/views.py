from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.views.generic import TemplateView, UpdateView

from .forms import CustomUserCreationForm, UserLoginForm, PasswordSetForm, CustomUserChangeForm, ResetPasswordForm

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'app_users/home.html'
    extra_context = {'title': _('Главная страница'), 'current_elem': 'home'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "app_users/profile/signup.html"
    extra_context = {'title': _('Регистрация'), 'current_elem': 'signup'}

    def get(self, request, *args, **kwargs):
        try:
            referrer = User.objects.get(id=kwargs.get('pk'))
        except ObjectDoesNotExist:
            return redirect('signup_error')

        if referrer.status != '2' and not referrer.is_core:
            return redirect('signup_error')

        if request.user.id == referrer.id:
            return redirect('home')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        referrer = User.objects.get(id=kwargs.get('pk'))
        if referrer.status != '2' and not referrer.is_core:
            raise PermissionDenied(_('Данная ссылка-приглашение невалидна'))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.parent = referrer
            instance.status = '1'
            if User.objects.filter(is_core=True).count() < 500:
                instance.is_core = True
            instance.save()
            return redirect('login')
        return super().post(request, *args, **kwargs)


class LogInView(LoginView):
    template_name = 'app_users/profile/login.html'
    authentication_form = UserLoginForm
    next_page = reverse_lazy('home')
    extra_context = {'title': _('Вход'), 'current_elem': 'login'}


@login_required
def account_view(request):
    return render(
        request,
        'app_users/profile/profile.html',
        {'user': request.user, 'title': _('Личный кабинет'), 'current_elem': 'profile'}
    )


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
    extra_context = {'title': _('Редактировать профиль'), 'current_elem': 'edit_profile'}

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
    return render(
        request,
        'app_users/profile/balance.html',
        {'user': request.user, 'title': _('Баланс'), 'current_elem': 'balance'}
    )


@login_required
def topup_withdrawal(request):
    return render(
        request,
        'app_users/profile/topup_withdrawal.html',
        {'user': request.user, 'title': _('Пополнение / Вывод'), 'current_elem': 'topup_withdrawal'}
    )


@login_required
def portfolio(request):
    return render(
        request,
        'app_users/profile/portfolio.html',
        {'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio'}
    )


@login_required
def contracts(request):
    return render(
        request,
        'app_users/profile/contracts.html',
        {'user': request.user, 'title': _('Заказы'), 'current_elem': 'contracts'}
    )


@login_required
def contests(request):
    return render(
        request,
        'app_users/profile/contests.html',
        {'user': request.user, 'title': _('Конкурсы'), 'current_elem': 'contests'}
    )


@login_required
def place_contract(request):
    return render(
        request,
        'app_users/profile/place_contract.html',
        {'user': request.user, 'title': _('Разместить заказ'), 'current_elem': 'place_contract'}
    )


@login_required
def announce_contest(request):
    return render(
        request,
        'app_users/profile/announce_contest.html',
        {'user': request.user, 'title': _('Объявить конкурс'), 'current_elem': 'announce_contest'}
    )


@login_required
def search_contractor(request):
    return render(
        request,
        'app_users/profile/search_contractor.html',
        {'user': request.user, 'title': _('Поиск исполнителя'), 'current_elem': 'search_contractor'}
    )


@login_required
def chat(request):
    return render(
        request,
        'app_users/profile/chat.html',
        {'user': request.user, 'title': _('Чат'), 'current_elem': 'chat'}
    )


@login_required
def support(request):
    return render(
        request,
        'app_users/profile/support.html',
        {'user': request.user, 'title': _('Помощь'), 'current_elem': 'support'}
    )
