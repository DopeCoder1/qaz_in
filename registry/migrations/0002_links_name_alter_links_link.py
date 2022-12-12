# Generated by Django 4.1.3 on 2022-12-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
    ]