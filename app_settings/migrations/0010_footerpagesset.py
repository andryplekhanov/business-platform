# Generated by Django 4.1.6 on 2023-02-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_static_pages', '0002_alter_staticpage_text_block'),
        ('app_settings', '0009_delete_footerpagesset'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterPagesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_pages', models.ManyToManyField(to='app_static_pages.staticpage', verbose_name='статичные страницы для футера')),
            ],
            options={
                'verbose_name': 'статичные страницы для футера',
                'verbose_name_plural': 'статичные страницы для футера',
            },
        ),
    ]
