# Generated by Django 4.1.5 on 2023-03-26 11:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text Of Blog'),
        ),
    ]
