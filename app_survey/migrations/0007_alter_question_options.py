# Generated by Django 4.1.6 on 2023-02-16 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_survey', '0006_alter_choice_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pub_date'], 'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
    ]