# Generated by Django 4.1.2 on 2022-11-13 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]