# Generated by Django 5.0.3 on 2024-03-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_playground_siteuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='join_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
