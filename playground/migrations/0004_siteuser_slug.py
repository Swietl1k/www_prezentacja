# Generated by Django 5.0.3 on 2024-03-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_siteuser_join_date_siteuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
