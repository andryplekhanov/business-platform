# Generated by Django 4.1.6 on 2023-02-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_personal_account', '0003_remove_transaction_account_transaction_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance_after',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='баланс после транзакции'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='balance_before',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='баланс до транзакции'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reason',
            field=models.CharField(choices=[('NR', 'Нет причины'), ('СP', 'Оплата сделки'), ('DF', 'Фонд развития'), ('CF', 'Фонд потребления'), ('TUBT', 'Пополнение переводом (вручную)'), ('WDBT', 'Вывод переводом (вручную)'), ('TU', 'Пополнение'), ('WD', 'Вывод'), ('1LС', 'Рефералы 1го уровня - сделка'), ('2LС', 'Рефералы 2го уровня - сделка'), ('3LС', 'Рефералы 3го уровня - сделка'), ('1LE', 'Рефералы 1го уровня - вступление'), ('2LE', 'Рефералы 2го уровня - вступление'), ('3LE', 'Рефералы 3го уровня - вступление')], default='NR', max_length=5, verbose_name='причина'),
        ),
    ]