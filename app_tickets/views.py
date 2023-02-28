from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


@login_required
def tickets(request):
    context = {
        'user': request.user, 'title': _('Тикеты'), 'current_elem': 'tickets',
        'breadcrumbs': {_('Главная'): 'home', _('Личный кабинет'): 'edit_profile', _('Помощь'): 'support', _('Тикеты'): 'tickets'}
    }
    return render(
        request,
        'app_tickets/tickets.html',
        context=context
    )
