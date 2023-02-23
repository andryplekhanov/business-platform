from django.db import transaction

from app_personal_account.models import Transaction


@transaction.atomic
def do_entrance_fee(user, consumption_fund, development_fund):
    Transaction.objects.create(user=user, reason="CF", direction="DEB", amount=1000)  # 1000 р. списывается в Фонд Потребления
    Transaction.objects.create(user=consumption_fund, reason="CF", direction="CRE", amount=1000, comment=user)  # 1000 р. зачисляется в Фонд Потребления
    Transaction.objects.create(user=user, reason="DF", direction="DEB", amount=999)  # 999 р. списывается в Фонд Развития
    Transaction.objects.create(user=development_fund, reason="DF", direction="CRE", amount=999, comment=user)  # 999 р. зачисляется в Фонд Развития
