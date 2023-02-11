from django.urls import path

from app_users.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', account_view, name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
