# Generated by Django 4.1.6 on 2023-02-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='visible',
            field=models.BooleanField(default=False, verbose_name='видимый на сайте'),
        ),
    ]