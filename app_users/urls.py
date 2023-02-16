from django.urls import path

from app_users.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("signup/<int:pk>/", SignUp.as_view(), name="signup"),
    path("signup_error/", signup_error, name="signup_error"),
    path("login/", LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', account_view, name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/balance/', balance, name='balance'),
    path('profile/topup_withdrawal/', topup_withdrawal, name='topup_withdrawal'),
    path('profile/portfolio/', portfolio, name='portfolio'),
    path('profile/contracts/', contracts, name='contracts'),
    path('profile/contests/', contests, name='contests'),
    path('profile/place_contract/', place_contract, name='place_contract'),
    path('profile/announce_contest/', announce_contest, name='announce_contest'),
    path('profile/search_contractor/', search_contractor, name='search_contractor'),
    path('profile/chat/', chat, name='chat'),
    path('profile/support/', support, name='support'),

]
