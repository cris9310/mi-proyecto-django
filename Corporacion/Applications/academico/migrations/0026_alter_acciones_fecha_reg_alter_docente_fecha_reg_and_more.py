# Generated by Django 4.1 on 2023-01-16 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0025_alter_acciones_fecha_reg_alter_docente_fecha_reg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acciones',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 631794), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 628804), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 629794), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 630795), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 627795), max_length=50),
        ),
        migrations.AlterField(
            model_name='materias',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 628804), max_length=50),
        ),
        migrations.AlterField(
            model_name='pensum',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 627795), max_length=50),
        ),
        migrations.AlterField(
            model_name='periodos',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 626794), max_length=50),
        ),
        migrations.AlterField(
            model_name='programas',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 19, 38, 13, 626794), max_length=50),
        ),
    ]
