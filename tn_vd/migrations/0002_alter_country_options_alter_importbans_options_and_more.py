# Generated by Django 4.1.3 on 2022-12-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tn_vd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='importbans',
            options={'verbose_name': 'Запрет', 'verbose_name_plural': 'Запреты'},
        ),
        migrations.AlterModelOptions(
            name='singlecustoms',
            options={'verbose_name': 'Единая таможенная пошлина', 'verbose_name_plural': 'Единая таможенные пошлины'},
        ),
        migrations.AlterModelOptions(
            name='tnvd',
            options={'verbose_name': 'ТН ВД', 'verbose_name_plural': 'ТН ВД'},
        ),
    ]