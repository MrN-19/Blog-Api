# Generated by Django 4.1.5 on 2023-02-01 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(null=True, verbose_name='Text Of Blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.FileField(upload_to='blog/pictures', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'), message='This File is not Valid')]),
        ),
    ]