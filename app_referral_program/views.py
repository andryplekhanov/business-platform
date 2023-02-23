from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import Error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from app_referral_program.transactions import do_entrance_fee

User = get_user_model()


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


@login_required
def pay_ent_fee(request):
    if request.user.balance < 2000:
        return render(request, 'app_referral_program/entrance_fee_err.html')
    consumption_fund = User.objects.filter(groups__name='consumption_fund').first()
    development_fund = User.objects.filter(groups__name='development_fund').first()
    if not consumption_fund or not development_fund:
        return render(request, 'app_referral_program/entrance_fee_err.html')

    try:
        do_entrance_fee(request.user, consumption_fund, development_fund)
    except Error as exc:
        return render(request, 'app_referral_program/entrance_fee_err.html')
    else:
        request.user.paid_entrance_fee = True
        if User.objects.filter(is_core=True).count() < 500:
            request.user.is_core = True
        request.user.save(update_fields=['paid_entrance_fee', 'is_core'])
    return HttpResponseRedirect(reverse('referral_program'))
