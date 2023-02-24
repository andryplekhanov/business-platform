from django.urls import path

from app_users.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("signup/<int:personal_account>/", SignUp.as_view(), name="signup"),
    path("signup_error/", signup_error, name="signup_error"),
    path("login_user/", login_user, name="login_user"),
    path('logout/', LogOutView.as_view(), name='logout'),

    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),

    path('invalid_verify/', TemplateView.as_view(template_name='app_users/profile/invalid_verify.html'), name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='app_users/profile/confirm_email.html'), name='confirm_email'),

    path('profile/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/notifications/', account_notification_view, name='notifications'),
    path('profile/verification/', account_verification_view, name='verification'),
    path('profile/agreement/', account_agreement_view, name='agreement'),
    path('profile/password-security/', account_security_view, name='password_and_security'),

    path('profile/balance/', balance, name='balance'),
    path('profile/balance/shareholders-book/', shareholders_book, name='shareholders_book'),
    path('profile/topup_withdrawal/', topup_withdrawal, name='topup_withdrawal'),
    path('profile/contracts/', contracts, name='contracts'),
    path('profile/contests/', contests, name='contests'),
    path('profile/place_contract/', place_contract, name='place_contract'),
    path('profile/announce_contest/', announce_contest, name='announce_contest'),
    path('profile/search_contractor/', search_contractor, name='search_contractor'),
    path('profile/chat/', chat, name='chat'),
    path('profile/support/', support, name='support'),

]
