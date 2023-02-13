# Generated by Django 4.1.6 on 2023-02-13 16:55

import app_settings.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_static_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=55, null=True, verbose_name='название компании')),
                ('slogan', models.TextField(blank=True, null=True, verbose_name='слоган')),
                ('description', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='номер телефона')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компания',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'социальные сети',
                'verbose_name_plural': 'социальные сети',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=55, null=True, verbose_name='название')),
                ('link', models.URLField(blank=True, max_length=255, null=True, unique=True, verbose_name='ссылка')),
                ('icon', models.FileField(blank=True, db_index=True, null=True, upload_to='social_media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'svg'], message='Ошибка загрузки: допускаются только файлы с расширением .png .svg'), app_settings.validators.icon_size_validate], verbose_name='иконка')),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_item', to='app_settings.socialmedia', verbose_name='социальные сети')),
            ],
            options={
                'verbose_name': 'соцсеть',
                'verbose_name_plural': 'соцсети',
            },
        ),
        migrations.CreateModel(
            name='FooterPagesRightSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_pages', models.ManyToManyField(to='app_static_pages.staticpage', verbose_name='статичные страницы для футера (справа)')),
            ],
            options={
                'verbose_name': 'статичные страницы для футера (справа)',
                'verbose_name_plural': 'статичные страницы для футера (справа)',
            },
        ),
        migrations.CreateModel(
            name='FooterPagesLeftSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_pages', models.ManyToManyField(to='app_static_pages.staticpage', verbose_name='статичные страницы для футера (слева)')),
            ],
            options={
                'verbose_name': 'статичные страницы для футера (слева)',
                'verbose_name_plural': 'статичные страницы для футера (слева)',
            },
        ),
    ]
