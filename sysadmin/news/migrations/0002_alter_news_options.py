# Generated by Django 4.0.6 on 2023-10-26 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-time_create'], 'verbose_name_plural': 'Новости'},
        ),
    ]
