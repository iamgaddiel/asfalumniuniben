# Generated by Django 3.2.6 on 2021-08-30 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210830_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='thumbnail',
            new_name='thumbnail_image',
        ),
    ]
