# Generated by Django 3.2.6 on 2021-08-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_profile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='user.svg', upload_to='%y%m%d'),
        ),
    ]
