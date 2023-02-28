from django.urls import path

from app_tickets.views import *

urlpatterns = [
    path('', tickets, name='tickets'),

]
