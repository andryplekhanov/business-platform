# Generated by Django 4.1.6 on 2023-02-13 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_alter_customuser_referer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='referer',
        ),
    ]