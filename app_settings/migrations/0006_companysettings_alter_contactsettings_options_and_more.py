# Generated by Django 4.1.6 on 2023-02-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0005_remove_contactsettings_address1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=55, null=True, verbose_name='название компании')),
                ('slogan', models.TextField(blank=True, null=True, verbose_name='слоган')),
                ('description', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
            ],
            options={
                'verbose_name': 'компания',
            },
        ),
        migrations.AlterModelOptions(
            name='contactsettings',
            options={'verbose_name': 'контакты'},
        ),
        migrations.RenameField(
            model_name='contactgrop',
            old_name='сontact_settings',
            new_name='contact_settings',
        ),
    ]
