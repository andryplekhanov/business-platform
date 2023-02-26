from django.urls import path

from app_portfolio.views import *

urlpatterns = [
    path('profile/portfolio-best/', PortfolioBest.as_view(), name='portfolio_best'),
    path('profile/add-work/', CreateWorkView.as_view(), name='add_work'),
    path('profile/portfolio-best/<int:pk>/', PortfolioBestDetailView.as_view(), name='portfolio_best_detail'),
    path('profile/portfolio-best/<int:pk>/edit', EditWorkView.as_view(), name='edit_work'),
    path('profile/portfolio-best/<int:pk>/delete', WorkDeleteView.as_view(), name='delete_work'),

    path('profile/portfolio-current/', portfolio_current, name='portfolio_current'),
    path('profile/portfolio-rating/', portfolio_rating, name='portfolio_rating'),
    path('profile/portfolio-reviews/', portfolio_reviews, name='portfolio_reviews'),
    path('profile/portfolio-settings/', portfolio_settings, name='portfolio_settings'),

]
