from django.urls import path

from app_referral_program.views import *

urlpatterns = [
    path("", referral_program, name="referral_program"),
    # path("signup/<int:pk>/", SignUp.as_view(), name="signup"),

]