# Generated by Django 4.1.6 on 2023-02-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_core',
            field=models.BooleanField(db_index=True, default=False, verbose_name='входит в ядро'),
        ),
    ]