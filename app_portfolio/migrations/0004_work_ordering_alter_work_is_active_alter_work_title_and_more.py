# Generated by Django 4.1.6 on 2023-02-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0003_work_file1_work_file2_work_file3_work_file4'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='ordering',
            field=models.CharField(choices=[('1', 'Первая'), ('-1', 'Последняя'), ('0', 'По счёту')], db_index=True, default='0', max_length=3, verbose_name='сортировка'),
        ),
        migrations.AlterField(
            model_name='work',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='отображать на сайте'),
        ),
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='заголовок'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]