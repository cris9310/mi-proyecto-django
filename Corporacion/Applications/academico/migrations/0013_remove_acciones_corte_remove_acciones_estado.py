# Generated by Django 4.1 on 2022-10-24 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0012_habilitaciones_cf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acciones',
            name='corte',
        ),
        migrations.RemoveField(
            model_name='acciones',
            name='estado',
        ),
    ]
