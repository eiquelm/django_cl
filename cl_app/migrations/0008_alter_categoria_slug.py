# Generated by Django 5.0.6 on 2024-05-25 14:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0007_categoria_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='nombre', unique=True),
        ),
    ]
