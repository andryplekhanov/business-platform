# Generated by Django 4.1.6 on 2023-02-26 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('NR', 'Нет причины'), ('ERR', 'Ошибка'), ('СP', 'Оплата сделки'), ('DF', 'Фонд развития - вступительный взнос'), ('CF', 'Фонд потребления - вступительный взнос'), ('TUBT', 'Пополнение переводом (вручную)'), ('WDBT', 'Вывод переводом (вручную)'), ('TU', 'Пополнение'), ('WD', 'Вывод'), ('1LС', 'Рефералы 1го уровня - сделка'), ('2LС', 'Рефералы 2го уровня - сделка'), ('3LС', 'Рефералы 3го уровня - сделка'), ('1LE', 'Рефералы 1го уровня - вступление'), ('2LE', 'Рефералы 2го уровня - вступление'), ('3LE', 'Рефералы 3го уровня - вступление')], default='NR', max_length=9, verbose_name='причина')),
                ('direction', models.CharField(choices=[('CRE', 'Зачисление'), ('DEB', 'Списание')], max_length=9, verbose_name='тип операции')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='сумма')),
                ('balance_before', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='баланс до транзакции')),
                ('balance_after', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='баланс после транзакции')),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата транзакции')),
                ('exist', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='комментарий')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'транзакции',
                'ordering': ('-datetime',),
            },
        ),
    ]
