# Generated by Django 4.1 on 2023-01-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='observacion',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
