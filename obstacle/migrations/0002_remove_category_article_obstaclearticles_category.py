# Generated by Django 4.1.3 on 2022-12-09 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obstacle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='article',
        ),
        migrations.AddField(
            model_name='obstaclearticles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obstacle.category', verbose_name='Категория'),
        ),
    ]
