# Generated by Django 4.1 on 2023-02-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0006_remove_facturas_consecutivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturassub',
            name='consecutivo',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
