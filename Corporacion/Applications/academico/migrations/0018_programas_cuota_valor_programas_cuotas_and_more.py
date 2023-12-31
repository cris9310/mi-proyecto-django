# Generated by Django 4.1 on 2023-01-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0017_programas_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='programas',
            name='cuota_valor',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='programas',
            name='cuotas',
            field=models.PositiveIntegerField(default=0, verbose_name='Numero de cuotas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programas',
            name='matricula',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='programas',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
