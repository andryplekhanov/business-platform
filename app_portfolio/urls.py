from django.urls import path

from app_portfolio.views import *

urlpatterns = [
    path('profile/portfolio-best/', portfolio_best, name='portfolio_best'),
    path('profile/portfolio-current/', portfolio_current, name='portfolio_current'),
    path('profile/portfolio-rating/', portfolio_rating, name='portfolio_rating'),
    path('profile/portfolio-reviews/', portfolio_reviews, name='portfolio_reviews'),
    path('profile/portfolio-settings/', portfolio_settings, name='portfolio_settings'),
    path('profile/add-portfolio-item/', add_portfolio_item, name='add_portfolio_item'),
]
