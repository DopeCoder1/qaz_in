# Generated by Django 4.1.3 on 2022-12-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory2',
            name='article',
        ),
        migrations.AddField(
            model_name='strategyarticles',
            name='subcategory2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.subcategory2', verbose_name='Категория'),
        ),
    ]
