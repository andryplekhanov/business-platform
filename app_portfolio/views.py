from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def portfolio_best(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_best',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_best.html',
        context=context
    )


def portfolio_current(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_current',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_current.html',
        context=context
    )


def portfolio_rating(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_rating',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_rating.html',
        context=context
    )


def portfolio_reviews(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_reviews',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_reviews.html',
        context=context
    )


def portfolio_settings(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'portfolio_settings',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio'},
    }
    return render(
        request,
        'app_portfolio/portfolio_settings.html',
        context=context
    )


def add_portfolio_item(request):
    context = {
        'user': request.user, 'title': _('Портфолио'), 'current_elem': 'portfolio', 'current_section': 'add_portfolio_item',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Портфолио'): 'portfolio', _('Добавление работы'): 'add_portfolio_item'},
    }
    return render(
        request,
        'app_portfolio/add_portfolio_item.html',
        context=context
    )

