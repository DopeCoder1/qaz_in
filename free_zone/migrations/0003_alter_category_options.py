# Generated by Django 4.1.3 on 2022-12-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free_zone', '0002_remove_category_article_freezonearticles_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
