from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_duplicate(value):
    if Usuario.objects.filter(rut=value).exists():
        raise ValidationError('El rut ya se encuentra registrado')

def validate_fecha_posterior(value):
    fecha_limite = date(2022, 12, 30)
    if value < fecha_limite:
        raise ValidationError('No se pueden hacer reservas para fechas anteriores al 2022-12-30')

class Usuario(models.Model):
    rut = models.CharField(max_length=100,primary_key=True )
    password = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username  


class reserva (models.Model):
    id_reserva = models.CharField(max_length=100, primary_key=True, validators=[validate_duplicate])
    rut = models.CharField(max_length=100)
    fecha = models.DateField(validators=[validate_fecha_posterior])
    hora = models.TimeField()
    medico = models.CharField(max_length=100)
    correo= models.EmailField(default='correo@gmail.com')
    def __str__(self):
        return self.id_reserva 