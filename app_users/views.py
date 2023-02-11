from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
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
    template_name = "app_users/signup.html"
    extra_context = {'title': _('Регистрация'), 'current_elem': 'signup'}


class LogInView(LoginView):
    template_name = 'app_users/login.html'
    authentication_form = UserLoginForm
    next_page = reverse_lazy('home')
    extra_context = {'title': _('Вход'), 'current_elem': 'login'}


@login_required
def account_view(request):
    return render(
        request,
        'app_users/profile.html',
        {'user': request.user, 'title': _('Регистрация'), 'current_elem': 'profile'}
    )


class EditProfileView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = CustomUserChangeForm
    model = User
    template_name = 'app_users/edit_profile.html'
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
    email_template_name = 'app_users/password_reset_email.html'
    template_name = 'app_users/password_reset_form.html'
    form_class = ResetPasswordForm
    extra_context = {'title': _('Сброс пароля'), 'current_elem': 'password_reset'}


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'app_users/password_reset_done.html'
    extra_context = {'title': _('Сброс пароля'), 'current_elem': 'password_reset_done'}


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'app_users/password_reset_confirm.html'
    form_class = PasswordSetForm
    post_reset_login = False
    extra_context = {'title': _('Создание нового пароля'), 'current_elem': 'password_reset_confirm'}

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'app_users/password_reset_complete.html'
    extra_context = {'title': _('Новый пароль успешно создан'), 'current_elem': 'password_reset_complete'}
