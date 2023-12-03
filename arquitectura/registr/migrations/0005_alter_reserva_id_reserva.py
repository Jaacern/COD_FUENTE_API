# Generated by Django 4.2.7 on 2023-11-16 22:18

from django.db import migrations, models
import registr.models


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0004_remove_usuario_id_alter_usuario_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id_reserva',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[registr.models.validate_duplicate]),
        ),
    ]