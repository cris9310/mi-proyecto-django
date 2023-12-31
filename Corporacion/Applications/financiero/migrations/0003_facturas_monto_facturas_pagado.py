# Generated by Django 4.1 on 2023-01-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0002_facturas_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='monto',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='facturas',
            name='pagado',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=25),
        ),
    ]
