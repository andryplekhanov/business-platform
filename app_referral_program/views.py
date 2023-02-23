from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


@login_required
def referral_program(request):
    context = {
        'user': request.user, 'title': _('Реферальная программа'), 'current_elem': 'referral_program',
        'breadcrumbs': {_('Главная'): 'home', _('Реферальная программа'): 'referral_program'}
    }
    return render(
        request,
        'app_referral_program/referral_program.html',
        context=context
    )

