# Generated by Django 4.1.6 on 2023-02-09 09:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='text_block',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='дополнительный блок текста'),
        ),
    ]