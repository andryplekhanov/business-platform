from django.urls import path

from app_referral_program.views import *

urlpatterns = [
    path("", referral_program, name="referral_program"),
    path("pay_ent_fee", pay_ent_fee, name="pay_ent_fee"),

]