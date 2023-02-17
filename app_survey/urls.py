from django.urls import path

from app_survey.views import *

urlpatterns = [
    path('', PollListView.as_view(), name='polls-list'),
    path('<int:pk>/', PollDetailView.as_view(), name='polls-detail'),
    path('<int:pk>/results/', PollResultsView.as_view(), name='polls-results'),
    path('<int:question_id>/vote/', vote, name='polls-vote'),
]
