# Generated by Django 3.2.4 on 2021-08-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210809_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
