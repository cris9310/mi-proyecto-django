# Generated by Django 4.1 on 2023-08-03 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0040_docente_tdocument_alter_acciones_fecha_reg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogstypesdocuement',
            name='nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acciones',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='fecha_reg',
            field=models.DateField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), max_length=50),
        ),
        migrations.AlterField(
            model_name='materias',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), max_length=50),
        ),
        migrations.AlterField(
            model_name='pensum',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), max_length=50),
        ),
        migrations.AlterField(
            model_name='periodos',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), max_length=50),
        ),
        migrations.AlterField(
            model_name='programas',
            name='an_creacion',
            field=models.CharField(default=datetime.datetime(2023, 8, 3, 2, 41, 24, 613599), max_length=50),
        ),
    ]
