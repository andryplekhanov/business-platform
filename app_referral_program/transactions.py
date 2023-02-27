from django.db import transaction

from app_personal_account.models import Transaction


@transaction.atomic
def do_entrance_fee(user, consumption_fund, development_fund):
    Transaction.objects.create(user=user, reason="CF", direction="DEB", amount=1000)  # 1000 р. списывается в Фонд Потребления
    Transaction.objects.create(user=consumption_fund, reason="CF", direction="CRE", amount=1000, comment=user)  # 1000 р. зачисляется в Фонд Потребления для последующего перевода реферерам пользователя user (comment)
    Transaction.objects.create(user=user, reason="DF", direction="DEB", amount=999)  # 999 р. списывается в Фонд Развития
    Transaction.objects.create(user=development_fund, reason="DF", direction="CRE", amount=999, comment=user)  # 999 р. зачисляется в Фонд Развития

# TODO: код ниже нужно реализовать через планировщик задач 'django_celery_beat' (установлен). Пересчёт каждые 24 ч.
    father = user.parent
    if father:
        Transaction.objects.create(user=consumption_fund, reason="1LE", direction="DEB", amount=500, comment=father)  # 500 р. списывается рефереру 1го уровня (папе)
        Transaction.objects.create(user=father, reason="1LE", direction="CRE", amount=500)  # 500 р. зачисляется рефереру 1го уровня

    grandfather = father.parent
    if grandfather:
        Transaction.objects.create(user=consumption_fund, reason="2LE", direction="DEB", amount=400, comment=grandfather)  # 400 р. списывается рефереру 2го уровня (дедушке)
        Transaction.objects.create(user=grandfather, reason="2LE", direction="CRE", amount=400)  # 400 р. зачисляется рефереру 2го уровня

    great_grandfather = grandfather.parent
    if great_grandfather:
        Transaction.objects.create(user=consumption_fund, reason="3LE", direction="DEB", amount=100, comment=great_grandfather)  # 100 р. списывается рефереру 3го уровня (прадедушке)
        Transaction.objects.create(user=great_grandfather, reason="3LE", direction="CRE", amount=100)  # 100 р. зачисляется рефереру 3го уровня
