# Generated by Django 4.2.7 on 2023-11-16 21:06

from django.db import migrations, models
import registr.models


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0002_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='id',
        ),
        migrations.AddField(
            model_name='reserva',
            name='correo',
            field=models.EmailField(default='correo@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(validators=[registr.models.validate_fecha_posterior]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='id_reserva',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
