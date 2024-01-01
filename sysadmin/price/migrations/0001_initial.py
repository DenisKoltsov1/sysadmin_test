# Generated by Django 4.0.6 on 2023-10-31 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Цены',
            },
        ),
    ]