# Generated by Django 3.2.6 on 2021-08-30 09:59

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='caption',
            field=ckeditor.fields.RichTextField(help_text='Enter caption text for this blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='this is the main writeup for this blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]