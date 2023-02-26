# Generated by Django 4.1.6 on 2023-02-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysettings',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='companysettings',
            name='phone_number1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='номер телефона1'),
        ),
        migrations.AddField(
            model_name='companysettings',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='номер телефона2'),
        ),
        migrations.AddField(
            model_name='companysettings',
            name='phone_number3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='номер телефона3'),
        ),
    ]