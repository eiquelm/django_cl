# Generated by Django 5.0.6 on 2024-05-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0002_remove_cliente_abreviatura_remove_cliente_reuup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico'),
        ),
    ]