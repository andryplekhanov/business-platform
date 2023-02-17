from django.urls import path

from app_news.views import *

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
    # path("signup/<int:pk>/", SignUp.as_view(), name="signup"),

]