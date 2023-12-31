# Generated by Django 4.2.4 on 2023-08-18 17:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='intro',
            field=ckeditor.fields.RichTextField(verbose_name='Intro'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Content'),
        ),
    ]
