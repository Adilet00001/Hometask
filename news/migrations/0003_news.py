# Generated by Django 4.1.3 on 2022-11-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images')),
                ('details', models.TextField(verbose_name='Подробности')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
            ],
        ),
    ]
