# Generated by Django 4.2.7 on 2023-11-06 15:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
