# Generated by Django 4.1 on 2022-10-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0009_habilitaciones_alter_estudiante_masivo_acciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilitaciones',
            name='Cerrado',
            field=models.BooleanField(default=False),
        ),
    ]
